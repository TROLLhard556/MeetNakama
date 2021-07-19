import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message, Chat, Contact
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatConsumer(WebsocketConsumer):
    def fetch_messages(self, data):
        messages = ""
        content = {'command': 'messages', 'messages': self.messages_to_json(messages)}
        self.send_message(content)

    def new_message(self, data):
        contact = data['from']
        author_user = User.objects.filter(email=contact)[0]
        contact_user = Contact.objects.filter(user=author_user)[0]
        message = Message.objects.create(contact=contact_user, content=data['message'])
        content = {'command': 'new_message', 'message': self.message_to_json(message)}
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            'contact': message.contact.user.first_name,
            'content': message.content,
            'timestamp': str(message.timestamp)
        }

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message
    }

    def connect(self):
        self.chatID = self.scope['url_route']['kwargs']['chatID']
        self.room_group_name = 'chat_%s' % self.chatID

        # join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # receive message from websocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)


    def send_chat_message(self, message):
        # send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    # receive message from room group
    def chat_message(self, event):
        message = event['message']

        #  send message to websocket
        self.send(text_data=json.dumps(message))
