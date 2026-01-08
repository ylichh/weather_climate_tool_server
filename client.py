#!/usr/bin/env python
import pika
import uuid
import json

EXCHANGE_NAME = "climate_exchange"
QUEUE_NAME = "rpc_queue"


class Client(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host="localhost",
                port=5672,
                credentials=pika.PlainCredentials(
                    username="toolUser", password="12341234"
                ),
            )
        )
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue="", exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True,
        )

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call_available_cities(self):
        return self.call_method("get_cities", {})

    def call_climate(self, ciudad):
        body = {"ciudad": ciudad}
        return self.call_method("get_climate_info", body)

    def call_method(self, routing_key, body):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange=EXCHANGE_NAME,
            routing_key=routing_key,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(body).encode("utf-8"),
        )
        while self.response is None:
            self.connection.process_data_events(time_limit=None)
        return json.loads(self.response)


if __name__ == "__main__":
    cliente = Client()
    print(cliente.call_climate("parís"))
