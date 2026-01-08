from src.climate_service.i_climate_service import IClimateService


class ClimateService(IClimateService):
    def __init__(self):
        self.repositorio_climas = {
            "paris": "Clima templado con estaciones marcadas. Veranos suaves y a veces cálidos. Otoños húmedos y frescos. Inviernos fríos con lluvias frecuentes.",
            "berlin": "Clima continental moderado. Veranos cálidos con algunos días muy calurosos. Otoños frescos y nublados. Inviernos fríos con heladas habituales.",
            "roma": "Clima mediterráneo. Veranos muy calurosos y secos. Otoños suaves y agradables. Inviernos templados con lluvias ocasionales.",
            "madrid": "Clima seco y continental. Veranos muy calurosos. Otoños cortos y agradables. Inviernos fríos pero con pocas lluvias.",
            "lisboa": "Clima suave atlántico. Veranos cálidos pero moderados por la brisa. Otoños húmedos y templados. Inviernos suaves con lluvias.",
            "amsterdam": "Clima oceánico. Veranos frescos y lluviosos. Otoños húmedos y ventosos. Inviernos fríos, raramente extremos.",
            "viena": "Clima continental. Veranos cálidos y soleados. Otoños frescos con niebla frecuente. Inviernos fríos con probabilidad de nieve.",
            "praga": "Clima continental templado. Veranos cálidos y agradables. Otoños frescos y nublados. Inviernos fríos con nieve ocasional.",
            "varsovia": "Clima continental frío. Veranos cálidos pero breves. Otoños fríos rápidamente. Inviernos largos, muy fríos y nevados.",
            "copenhague": "Clima oceánico frío. Veranos frescos y algo lluviosos. Otoños ventosos. Inviernos fríos con días muy cortos.",
            "estocolmo": "Clima frío nórdico. Veranos cortos y suaves. Otoños fríos y oscuros. Inviernos largos, muy fríos y nevados.",
            "oslo": "Clima nórdico templado por el mar. Veranos suaves. Otoños fríos y húmedos. Inviernos muy fríos con abundante nieve.",
            "helsinki": "Clima subártico. Veranos cortos y templados. Otoños fríos y ventosos. Inviernos muy largos, oscuros y helados.",
            "bruselas": "Clima oceánico. Veranos suaves y lluviosos. Otoños húmedos y frescos. Inviernos fríos pero no extremos.",
            "zurich": "Clima continental alpino. Veranos cálidos. Otoños frescos y húmedos. Inviernos fríos con mucha probabilidad de nieve.",
            "budapest": "Clima continental. Veranos calurosos y secos. Otoños templados. Inviernos fríos con heladas frecuentes.",
            "atenas": "Clima mediterráneo cálido. Veranos muy calurosos y secos. Otoños suaves. Inviernos templados con pocas lluvias.",
            "dublin": "Clima oceánico húmedo. Veranos frescos. Otoños muy lluviosos. Inviernos fríos pero moderados.",
            "edimburgo": "Clima oceánico frío. Veranos frescos y nublados. Otoños húmedos. Inviernos fríos, ventosos y con escasa nieve.",
            "zagreb": "Clima continental. Veranos cálidos. Otoños frescos con lluvias. Inviernos fríos y ocasionalmente nevados.",
        }
        self.ciudades_disponibles = {
            "ciudades": [
                "paris",
                "berlin",
                "roma",
                "madrid",
                "lisboa",
                "amsterdam",
                "viena",
                "praga",
                "varsovia",
                "copenhague",
                "estocolmo",
                "oslo",
                "helsinki",
                "bruselas",
                "zurich",
                "budapest",
                "atenas",
                "dublin",
                "edimburgo",
                "zagreb",
            ]
        }

    def obtain_climate_information(self, ciudad):
        return self.repositorio_climas.get(ciudad, {})

    def available_cities(self):
        return self.ciudades_disponibles
