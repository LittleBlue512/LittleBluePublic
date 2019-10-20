// Make Socket Connection to Server
const socket = io.connect('http://localhost:5000/');

const sendButton = document.getElementById('sendButton');
sendButton.addEventListener('click', () => {
    let messageBox = document.getElementById('messageBox');
    let nameBox = document.getElementById('nameBox');
    let message = messageBox.value;
    let name = nameBox.value;
    if (name === '' || message === '') {
        alert('Please enter name and message');
    }
    // Empty Input Box
    messageBox.value = '';
    nameBox.value = '';
    // Emit Message
    socket.emit('chat', {
        message: message,
        name: name
    });
});

// Listen on Emit from Server
var firstLoad = true; // Dealing With Chat Scrolling
socket.on('chat', (data) => {
    let messageDisplay = document.getElementById('messageDisplay');
    let name = data.name;
    let message = data.message;
    let messageHTML = `<p id="newChat" class="m-3 text-wrap">${name}: ${message}</p>`;
    let scrollToButtom = false;
    if (firstLoad || messageDisplay.scrollTop >= (messageDisplay.scrollHeight - messageDisplay.offsetHeight)) {
        scrollToButtom = true;
        firstLoad = false;
    }
    messageDisplay.innerHTML += messageHTML;
    if (scrollToButtom) {
        messageDisplay.scrollTop = messageDisplay.scrollHeight;
    }
}); 