import pika
import json
from src.climate_service.i_climate_service import IClimateService

EXCHANGE_NAME = "climate_exchange"
QUEUE_NAME = "rpc_queue"


class RabbitMqController:
    def configure_rabbitmq_controller(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host="localhost",
                port=5672,
                credentials=pika.PlainCredentials(
                    username="toolUser", password="12341234"
                ),
            )
        )
        self.channel = connection.channel()
        self.channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type="direct")
        queue_name = self.channel.queue_declare(
            queue=QUEUE_NAME, exclusive=True
        )  # puede que redundante
        queue_name = queue_name.method.queue

        self.channel.queue_bind(
            exchange=EXCHANGE_NAME, queue=queue_name, routing_key="get_cities"
        )
        self.channel.queue_bind(
            exchange=EXCHANGE_NAME, queue=queue_name, routing_key="get_climate_info"
        )

        self.channel.basic_qos(prefetch_count=1)

        self.channel.basic_consume(
            queue=queue_name, on_message_callback=self.on_request
        )

    def __init__(self, weather_service: IClimateService):
        self.weather_service = weather_service
        self.handlers = {
            "get_cities": self.get_available_cities_handler,
            "get_climate_info": self.get_climate_handler,
        }
        self.configure_rabbitmq_controller()

    def handle_request(self, routing_key, body):
        handler = self.handlers.get(routing_key, self.default_handler)
        jsoned_body = json.loads(body)
        return handler(jsoned_body)

    def get_available_cities_handler(self, body):
        return self.weather_service.available_cities()

    def get_climate_handler(self, body):
        ciudad = body["ciudad"]
        return self.weather_service.obtain_climate_information(ciudad)

    def default_handler(self):
        return {"error": "Método no disponible"}

    def on_request(self, ch, method, props, body):
        respuesta = self.handle_request(method.routing_key, body=body)
        ch.basic_publish(
            exchange="",
            routing_key=props.reply_to,
            properties=pika.BasicProperties(correlation_id=props.correlation_id),
            body=json.dumps(respuesta).encode("utf-8"),
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def run(self):
        print(" [x] Awaiting RPC requests")
        self.channel.start_consuming()
