from datetime import datetime


# -------------------------------
# Message Class
# -------------------------------
class Message:
    message_counter = 1

    def __init__(self, sender, content):
        self.id = Message.message_counter
        Message.message_counter += 1

        self.sender = sender
        self.content = content
        self.timestamp = datetime.now()

    def __str__(self):
        time = self.timestamp.strftime("%I:%M:%S %p")
        return f"[{time}] ({self.id}) {self.sender.username}: {self.content}"


# -------------------------------
# User Class
# -------------------------------
class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in {self.chatroom.name}.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")

    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom.")
        else:
            room_name = self.chatroom.name
            self.chatroom.remove_user(self)
            self.chatroom = None
            print(f"{self.username} left {room_name}")

    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom.")
            return

        # Commands
        if content == "/history":
            self.chatroom.show_chat_history()

        elif content == "/users":
            self.chatroom.show_users()

        else:
            self.chatroom.broadcast(self, content)


# -------------------------------
# ChatRoom Class
# -------------------------------
class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
        else:
            print(f"{user.username} is already in the room.")

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)

    def broadcast(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)
        print(message)

    def show_chat_history(self):
        print(f"\n===== Chat History : {self.name} =====")

        if not self.messages:
            print("No messages yet.")
            return

        for msg in self.messages:
            print(msg)

        print()

    def show_users(self):
        print(f"\n===== Users in {self.name} =====")

        if not self.users:
            print("No users in the room.")
            return

        for user in self.users:
            print("-", user.username)

        print()


# -------------------------------
# Main Program
# -------------------------------
if __name__ == "__main__":

    room = ChatRoom("Python Lounge")
    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    # Users join
    alice.join_chatroom(room)
    bob.join_chatroom(room)
    charlie.join_chatroom(room)

    print()

    # Messages
    alice.send_message("Hello everyone!")
    bob.send_message("Hi Alice!")
    charlie.send_message("Nice to meet you all!")

    print()

    # Commands
    alice.send_message("/users")
    bob.send_message("/history")

    # Leave room
    alice.leave_chatroom()
    bob.leave_chatroom()
    charlie.leave_chatroom()
