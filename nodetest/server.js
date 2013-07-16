var app = require("http").createServer(handler),
    io = require("socket.io").listen(app),
    fs = require("fs"),
    qs = require("querystring")

app.listen(8001)


function handler(req,res){}

var clients = {};

chatClients = new Object();

 
var socketsOfClients = {};
io.sockets.on('connection', function(socket) {
  socket.on('set username', function(user) {
      // Is this an existing user name?
    if (clients[user.username] === undefined) {
      // Does not exist ... so, proceed
      clients[user.username] = { 'socketid': socket.id, 'userid':user.userid };

      socketsOfClients[socket.id] = user.username;
      userNameAvailable(socket.id, user.username);
      userJoined(user.username, user.userid);
      updateList();
      subscribe(socket, { room: 'Lobi' });
      socket.emit('roomslist', { rooms: getRooms() });

    } else
    if (clients[user.username] === socket.id) {
      // Ignore for now
    } else {
      userNameAlreadyInUse(socket.id, user.username);
    }
  });


    socket.on('subscribe', function(data){
      subscribe(socket, data);
     });

  socket.on('message', function(msg) { 
      srcUser = socketsOfClients[socket.id];
      io.sockets.emit('message',
          { "message": msg.message ,
            "source": srcUser}
          );
  })
  socket.on('disconnect', function() {
    var uName = socketsOfClients[socket.id];
    var rooms = io.sockets.manager.roomClients[socket.id];
 
     // unsubscribe from the rooms
    for(var room in rooms){
      if(room && rooms[room]){
       unsubscribe(socket, { room: room.replace('/','') });
      }
    }

    delete socketsOfClients[socket.id];
    delete clients[uName];
 
    userLeft(uName);
    updateList();
  })
})
 
function userJoined(uName, userId) {
    Object.keys(socketsOfClients).forEach(function(sId) {
      io.sockets.sockets[sId].emit('userJoined', { "userName": uName, "userId": userId});
    })
}
 
function userLeft(uName) {
    io.sockets.emit('userLeft', { "userName": uName }); 
}
 
function userNameAvailable(sId, uName) {
  setTimeout(function() {
    console.log('Sending welcome msg to ' + uName + ' at ' + sId);
    io.sockets.sockets[sId].emit('welcome', { "userName" : uName , "currentUsers": JSON.stringify(Object.keys(clients)) });
 
  }, 500);
}

function updateList() {
    io.sockets.emit('updateList', {"currentUsers": JSON.stringify(clients)})
}
 
function userNameAlreadyInUse(sId, uName) {
  setTimeout(function() {
    io.sockets.sockets[sId].emit('error', { "userNameInUse" : true });
  }, 500);
}


function subscribe(socket, data){

 
 // subscribe the client to the room
 socket.join(data.room);
 socket.emit('roomslist', { rooms: getRooms() });
 
 // update all other clients about the online
 // presence
 // updatePresence(data.room, socket, 'online');
 
 // send to the client a list of all subscribed clients
 // in this room
 socket.emit('roomclients', { room: data.room, clients: 
                          getClientsInRoom(socket.id, data.room) });
}

function unsubscribe(socket, data){
 // update all other clients about the offline
 // presence
 //updatePresence(data.room, socket, 'offline');
 
 // remove the client from socket.io room
 socket.leave(data.room);
 
 // if this client was the only one in that room
 // we are updating all clients about that the
 // room is destroyed
 //if(!countClientsInRoom(data.room)){
 
  // with 'io.sockets' we can contact all the
  // clients that connected to the server
  //io.sockets.emit('removeroom', { room: data.room });
 //}
}


function getRooms(){
  return Object.keys(io.sockets.manager.rooms);
}

function getClientsInRoom(socketId, room){
    var roomclients = io.sockets.clients(room); 
    client=new Array();
    roomclients.forEach(function(_client) {
      console.log(_client)
        client.push({username:_client.username})
    });
  console.log(client) 
    return client;
}