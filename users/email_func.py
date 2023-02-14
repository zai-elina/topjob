from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

class ForgotPassword():
    def __init__(self,new_pass):
        self.new_pass = new_pass

    subject = 'TOPJOB Забыли свой пароль'
    def email(self):
        return{
            'title':'Ваш старый пароль был удален',
            'subtitle':'Вы захотели изменить свой пароль',
            'message':'Новый пароль: {} .Если это не вы изменили пароль напишите нам на почту'.format(self.new_pass),
        }

class WelcomeEmail():
    subject = 'TOPJOB Добро пожаловать на наш сайт!'
    email ={
            'title':'Спасибо, что зарегистрировались!',
            'subtitle':'TOPJOB - портал по поиску работы и размещению вакансий',
            'message':'Регистрация на сайте прошла успешно.',
        }


def sendEmail(email,subject,to_email):
    from_email = settings.EMAIL_HOST_USER
    text_content = """
        {}
        {} ,
        Поддержка TOPJOB
        """.format(email['subtitle'], email['message'])

    html_c = get_template('email.html')
    d = {'email': email}
    html_content = html_c.render(d)

    msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()