var app = require("http").createServer(handler),
    io = require("socket.io").listen(app)

app.listen(8001)

function handler(req,res){}

var usernames = {};

var main_room = 'Lobi';

io.sockets.on('connection', function(socket){
  socket.on('adduser', function(username){
    if (usernames[username] === undefined) {
      socket.username = username;
      usernames[username] = socket;
      
      socket.room = main_room;
      socket.join(main_room);

      socket.emit('updatechat', main_room, 'Sunucu', 'Dota-tr lig lobisine hoşgeldin, ' + username + '.');
      socket.broadcast.to(main_room).emit('updatechat', main_room, 'Sunucu', username + ' lig lobisine katıldı.');

      socket.emit('gamelist', getGames() );
      io.sockets.emit('userlist', getUsers(main_room) );
    }
  });

  socket.on('subscribe', function(data){
    current_games = getGames();
    if (current_games.indexOf('/'+data.room) != -1)
    {
      // joins a created game
      console.log(socket.username + " has joined to " +data.room);
      socket.join(data.room);
      socket.room = data.room;
      io.sockets.in(data.room).emit('game_userlist', {'users': getUsers(socket.room), 'room': data.room});
      socket.broadcast.to(data.room).emit('user_connected_to_game', {'room': data.room , 'username': socket.username});

    } else {
      // creates a new game
      console.log(socket.username + " has created " +data.room);
      socket.join(data.room);
      socket.room = data.room;
      io.sockets.in(data.room).emit('game_userlist', {'users': getUsers(socket.room), 'room': data.room});
      io.sockets.emit('gamelist', getGames());
    }
  });

  socket.on('unsubscribe', function(data){
    socket.leave(data.room);
    io.sockets.in(socket.room).emit('game_userlist', {'users': getUsers(socket.room), 'room': socket.room});
    io.sockets.in(socket.room).emit('user_dc_from_game', {'room': socket.room, 'username': socket.username});

    socket.room = main_room;
  });

  socket.on('sendchat', function (room, data) {
    io.sockets.in(room).emit('updatechat', room, socket.username, data);
  });

  socket.on('disconnect', function(){
    delete usernames[socket.username];

    socket.leave(main_room);
    socket.leave(socket.room);
    io.sockets.emit('userlist', getUsers(main_room));
    if(socket.room != main_room) {
      io.sockets.in(socket.room).emit('game_userlist', {'users': getUsers(socket.room), 'room': socket.room});
      io.sockets.in(socket.room).emit('user_dc_from_game', {'room': socket.room, 'username': socket.username});
      io.sockets.emit('gamelist', getGames() );
    }

    socket.broadcast.emit('updatechat', main_room, 'Sunucu', socket.username + ' lig lobisinden ayrıldı.');
  });

  socket.on('update_clients_teams', function(data){
    socket.broadcast.to(data.room).emit('update_player_positions', data.teams);
  })

  socket.on('update_client_teams', function(data){
    console.log(data.name);
    io.sockets.socket(usernames[data.name].id).emit('update_player_positions', data.teams);
  })

});

function getGames(){
  return Object.keys(io.sockets.manager.rooms);
}

function getUsers(room){
  users = io.sockets.clients(room);
  userlist = new Array();
  users.forEach(function(user){
    userlist.push(user.username);
  })

  return userlist;
}