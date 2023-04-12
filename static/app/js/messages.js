let input_message = document.getElementById('input-message')
let message_body = document.querySelector('.msg_card_body')
let send_message_form = document.getElementById('send-message-form')
const USER_ID = document.getElementById('logged-in-user').value

let loc = window.location
let wsStart = 'ws://'

if(loc.protocol === 'https') {
    wsStart = 'wss://'
}
let endpoint = wsStart + loc.host + loc.pathname

var socket = new WebSocket(endpoint)

socket.onopen = async function(e){
    console.log('open', e);
     send_message_form.addEventListener('submit', function (e){
        e.preventDefault()
        let message = input_message.value;
        let  send_to;
        if(USER_ID == 7){
            send_to = 8
        } else{
            send_to = 7
        }
        let data = {
            'message': message,
            'sent_by':USER_ID,
            'send_to':send_to,
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
    newMessage(message, sent_by_id)
}

socket.onerror = async function(e){
    console.log('error', e)
}

socket.onclose = async function(e){
    console.log('close', e)
}


function newMessage(message, sent_by_id) {
	if ($.trim(message) === '') {
		return false;
	}
    let message_element;
    if (sent_by_id == USER_ID){
       message_element = `<li class="d-flex justify-content-end mb-4">
            <div class="card w-100">
              <div class="card-header d-flex justify-content-between p-3">
                <p class="fw-bold mb-0 ">Lara Croft</p>
                <p class="text-muted small mb-0">
                  <i class="far fa-clock"></i> 13 mins ago
                </p>
              </div>
              <div class="card-body">
                <p class="mb-0 ">
                  ${message}
                </p>
              </div>
            </div>
            <img
              src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/avatar-5.webp"
              alt="avatar"
              class="rounded-circle d-flex align-self-start ms-3 shadow-1-strong"
              width="60"
            />
          </li>`
    } else {
        message_element = `<li class="d-flex justify-content-start mb-4">
            <img
              src="https://mdbcdn.b-cdn.net/img/Photos/Avatars/avatar-6.webp"
              alt="avatar"
              class="rounded-circle d-flex align-self-start me-3 shadow-1-strong"
              width="60"
            />
            <div class="card">
              <div class="card-header d-flex justify-content-between p-3">
                <p class="fw-bold mb-0 ">Brad Pitt</p>
                <p class="text-muted small mb-0">
                  <i class="far fa-clock"></i> 10 mins ago
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



	message_body.innerHTML += message_element
    message_body.scrollTop = message_body.scrollHeight;
	input_message.value='';
}
