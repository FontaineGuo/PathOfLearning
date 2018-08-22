from asyncore import dispatcher
from asynchat import async_chat
import asyncore, socket

PORT = 5005
NAME = 'Fontaine\'s chat room'


class EndSession(Exception): pass

class CommandHandler:
    '''
    command handler
    '''    
    def unknown(self, session, cmd):
        'Respond to an unknown command'
        session.push('Unknown command:{}s\r\n'.format(cmd).encode('utf-8'))

    def handle(self, session, line):
        'Handle a received line from a given session'
        if not line.strip():return
        # spilt command and msg
        parts = line.split(' ',1)
        cmd = parts[0]
        try:
            line = parts[1].strip()
        except IndexError:
            line = ''
        meth = getattr(self, 'do_'+cmd, None)
        try:
            meth(session, line)
        except TypeError:
            self.unknown(session, cmd)

class Room(CommandHandler):
    def __init__(self, server):
        self.server = server
        self.sessions = []
    
    def add(self, session):
        self.sessions.append(session)
    
    def remove(self, session):
        self.sessions.remove(session)

    def broadcast(self, line):
        for session in self.sessions:
            session.push(line)
        
    def do_logout(self, session, line):
        raise EndSession

class LoginRoom(Room):
    def add(self, session):
        Room.add(self, session)
        self.broadcast('Welcome to {}\r\n'.format(self.server.name).encode('utf-8'))

    def unknown(self, session, cmd):
        session.push('Please log in \nUse "login <nick>"\r\n'.encode('utf-8'))
    
    def do_login(self, session, line):
        name = line.strip()
        if not name:
            session.push('Please entera a name\r\n'.encode('utf-8'))
        elif name in self.server.users:
            session.push('The name "{}" is taken.\r\n'.format(name).encode('utf-8'))
            session.push('Please try again.\r\n'.encode('utf-8'))
        else:
            session.name = name
            session.enter(self.server.main_room)


class ChatRoom(Room):
    def add(self, session):
        self.broadcast((session.name + 'has entered the room,\r\n').encode('utf-8'))
        self.server.users[session.name] = session
        super().add(session)
    
    def remove(self, session):
        Room.remove(self, session)
        self.broadcast((session.name + ' has left the room.\r\n').encode('utf-8'))
    
    def do_say(self, session, line):
        self.broadcast((session.name + ': ' + line + '\r\n').encode('utf-8'))

    def do_look(self, session, line):
        session.push('The following are in this room:\r\n'.encode('utf-8'))
        for other in self.sessions:
            session.push((other.name + '\r\n').encode('utf-8'))

    def do_who(self, session, line):
        session.push('The folliwing are logger in:\r\n'.encode('utf-8'))
        for name in self.server.users:
            session.push((name + '\r\n').encode('utf-8'))

class LogoutRoom(Room):
    def add(self, session):
        try: del self.server.users[session.name]
        except KeyError: pass

class ChatSession(async_chat):
    def __init__(self, server, sock):
        super().__init__(sock)
        self.server = server
        self.set_terminator(b"\r\n")
        self.data = []
        self.name = None
        self.enter(LoginRoom(server))
    
    def enter(self, room):
        try:
            cur = self.room
        except AttributeError:
            pass
        else:
            cur.remove(self)
        self.room = room
        room.add(self)    

    def collect_incoming_data(self, data):
        self.data.append(data.decode('utf-8'))
    
    def found_terminator(self):
        line = ''.join(self.data)
        self.data = []
        try:self.room.handle(self, line)
        except EndSession: self.handle_close()
    
    def handle_close(self):
        async_chat.handle_close(self)
        self.enter(LogoutRoom(self.server))
    

class ChatServer(dispatcher):
    def __init__(self, port, name):
        super().__init__()
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.name = name
        self.users = {}
        self.main_room = ChatRoom(self)
    

    def handle_accept(self):
        conn, addr = self.accept()
        ChatSession(self, conn)


if __name__ == '__main__':
    s = ChatServer(PORT, NAME)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print()