from abc import ABC, abstractmethod


class IClimateService(ABC):
    @abstractmethod
    def obtain_climate_information(self, ciudad):
        pass

    @abstractmethod
    def available_cities(self):
        pass
