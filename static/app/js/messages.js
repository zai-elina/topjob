let input_message = document.getElementById('input-message')
let send_message_form = $('#send-message-form')
const USER_ID = document.getElementById('logged-in-user').value
$(window).load(function() {
  $(".msg_card_body").animate({ scrollTop: $('.msg_card_body').prop("scrollHeight") }, 1000);
});

let loc = window.location
let wsStart = 'ws://'

if(loc.protocol === 'https') {
    wsStart = 'wss://'
}
let endpoint = wsStart + loc.host + loc.pathname

var socket = new WebSocket(endpoint)



function get_active_other_user_id(){
    let other_user_id = $('.messages-wrapper.is_active').attr('other-user-id')
    other_user_id = $.trim(other_user_id)
    return other_user_id
}


function get_active_thread_id(){
    let chat_id = $('.messages-wrapper.is_active').attr('chat-id')
    let thread_id = chat_id.replace('chat_', '')
    return thread_id
}


socket.onopen = async function(e){
    console.log('open', e);
     send_message_form.on('submit', function (e){
        e.preventDefault();
        let message = input_message.value;
        let send_to = get_active_other_user_id()
        let thread_id = get_active_thread_id()

        let data = {
            'message': message,
            'sent_by':USER_ID,
            'send_to':send_to,
            'thread_id': thread_id,
        }
        data = JSON.stringify(data)
        socket.send(data)
        $(this)[0].reset()
    });
}

socket.onmessage = async function(e){
    console.log('message', e)
    let data =JSON.parse(e.data)
    let message = data['message']
    let sent_by_id = data['sent_by']
    let thread_id = data['thread_id']
    let name = data['name']
    let image = data['image']
    new_message(message, sent_by_id,thread_id,name,image)
}

socket.onerror = async function(e){
    console.log('error', e)
}

socket.onclose = async function(e){
    console.log('close', e)
}
const days = ["Вср","Пон","Вт","Ср","Чт","Пт","Сб"];
function formatDay(day){
    return days[day];
}

function new_message(message, sent_by_id,thread_id,name,image) {
	if ($.trim(message) === '') {
		return false;
	}
    let time =new Date();
    time = `${time.getDate()} ${formatDay(time.getDay())}, ${time.getHours()}:${time.getMinutes()}`

    let message_element;
    let chat_id = 'chat_' + thread_id;
    if (sent_by_id == USER_ID){
       message_element = `<li class="d-flex justify-content-end mb-4">
            <div class="card">
              <div class="card-header d-flex justify-content-between p-3">
                <p class="fw-bold mb-0">${name}</p>
                <p class="text-muted small mb-0">
                  <i class="far fa-clock"></i> ${time}
                </p>
              </div>
              <div class="card-body">
                <p class="mb-0 ">
                  ${message}
                  </p>
              </div>

            </div>
            <img
              src="${image}"
              alt="avatar"
              class="rounded-circle d-flex align-self-start me-3 shadow-1-strong"
              width="60"
            />
          </li>`
    } else {
        message_element = `<li class="d-flex justify-content-start mb-4">
            <img
              src="${image}"
              alt="avatar"
              class="rounded-circle d-flex align-self-start me-3 shadow-1-strong"
              width="60"
            />
            <div class="card">
              <div class="card-header d-flex justify-content-between p-3">
                <p class="fw-bold mb-0 ">${name}</p>
                <p class="text-muted small mb-0">
                  <i class="far fa-clock"></i> ${time}
                </p>
              </div>
              <div class="card-body">
                <p class="mb-0 ">
                  ${message}
                </p>
              </div>
            </div>
          </li>`
    }


    let message_body = $('.messages-wrapper[chat-id="' + chat_id + '"] .msg_card_body')
	message_body.append($(message_element))
    $(".msg_card_body").animate({ scrollTop: $('.msg_card_body').prop("scrollHeight") }, 1000);
	input_message.value = '';
}



$('.contact-li').on('click', function (){
    $('.contacts .active-contact').removeClass('active-contact')
    $(this).addClass('active-contact')

    // message wrappers
    let chat_id = $(this).attr('chat-id')
    $('.messages-wrapper.is_active').removeClass('is_active')
    $('.messages-wrapper[chat-id="' + chat_id +'"]').addClass('is_active')
})

