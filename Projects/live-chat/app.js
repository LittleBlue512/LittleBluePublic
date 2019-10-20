const express = require('express');
const path = require('path');
const socket = require('socket.io');
const app = express();

const port = 5000;
const server = app.listen(port, () => console.log(`Server started on port ${port} .....`));

app.use(express.static(path.join(__dirname, 'public')));

// Setup Socket
const io = socket(server);


// Listen on Socket Connection
io.on('connection', (socket) => {
    console.log(`Soket ID: ${socket.id}`);

    // Emit Data to all Sockets
    socket.on('chat', (data) => {
        io.sockets.emit('chat', data);
    });
});

