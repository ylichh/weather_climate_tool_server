from src.climate_service.climate_service import ClimateService
from src.climate_service.rabbit_mq.rabbit_mq_adapter import RabbitMqController

if __name__ == "__main__":
    climate_service = ClimateService()
    manager = RabbitMqController(climate_service)
    manager.run()
