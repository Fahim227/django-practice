import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.room_group_name = 'test'
        # adding to a group 
        print(self.channel_name)
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        

        # self.send(text_data=json.dumps({"message": "Socket Connected"}))
        # return super().connect()
    
    
    def receive(self, text_data=None, bytes_data=None):
        test_data_json = json.loads(text_data)
        print(text_data)
        message = test_data_json['message']

        print(test_data_json)
        print(self.channel_layer)
        # send to a group 
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message', 
                'data' : test_data_json
            }
        )
        # self.send(text_data=json.dumps(text_data))
        return super().receive(text_data, bytes_data)

    def chat_message(self,event):
        data = event['data']
        self.send(text_data=json.dumps({'type':'realtime_location','data':data}))