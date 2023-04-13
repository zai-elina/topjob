import json

from channels.consumer import AsyncConsumer
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from django.contrib.auth.models import User

from .models import *



class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connected', event)
        user = self.scope['user']
        chat_room = f'user_chatroom_{user.id}'
        self.chat_room = chat_room
        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )
        await self.send({
            'type': 'websocket.accept'
        })

    #Получение данных, отправленных внешним интерфейсом
    async def websocket_receive(self, event):
        print('receive', event)
        received_data = json.loads(event['text'])
        msg = received_data.get('message')
        sent_by_id = received_data.get('sent_by')
        send_to_id = received_data.get('send_to')
        thread_id = received_data.get('thread_id')

        if not msg:
            print('Ошибка: пустое сообщение')
            return False

        sent_by_user = await self.get_user_object(sent_by_id)
        send_to_user = await self.get_user_object(send_to_id)
        thread_object = await self.get_thread(thread_id)

        if not sent_by_user:
            print('Ошибка: id отправляющего неверное')
        if not send_to_user:
            print('Ошибка: id получающего неверное')
        if not thread_object:
            print('Ошибка: id диалога неверное')

        await self.create_chat_message(thread_object, sent_by_user, msg)

        other_user_chat_room = f'user_chatroom_{send_to_id}'
        self_user = self.scope['user']


        user_name = '{} {}'.format(sent_by_user.last_name,sent_by_user.first_name)

        response = {
            'message': msg,
            'sent_by': self_user.id,
            'thread_id': thread_id,
            'name': user_name,
        }

        await self.channel_layer.group_send(
            other_user_chat_room,
            {
                'type': 'chat_message',
                'text': json.dumps(response)
            }
        )

        await self.channel_layer.group_send(
            self.chat_room,
            {
                'type': 'chat_message',
                'text': json.dumps(response)
            }
        )

    async def chat_message(self, event):
        print('chat_message', event)
        await self.send({
            'type': 'websocket.send',
            'text': event['text']
        })

    async def websocket_disconnect(self, event):
        print('disconnect', event)


    #Функция асинхронной синхронизации с базой данной,
    # гарантия правильного открытия и закрытия соединения
    @database_sync_to_async
    def get_user_object(self,user_id):
        qs = User.objects.filter(id=user_id)

        if qs.exists():
            obj = qs.first()
        else:
            obj = None
        return obj

    @database_sync_to_async
    def get_thread(self, user_id):
        qs = Thread.objects.filter(id=user_id)

        if qs.exists():
            obj = qs.first()
        else:
            obj = None
        return obj

    #Сохранение сообщения в бд
    @database_sync_to_async
    def create_chat_message(self, thread, user, msg):
        ChatMessage.objects.create(thread=thread, user=user, message=msg)