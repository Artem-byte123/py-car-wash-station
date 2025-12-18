class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car):
        cost = car.comfort_class * (
                    self.clean_power - car.clean_mark) / self.distance_from_city_center * self.average_rating
        return round(cost, 1)

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def several_cars(self, cars):
        total_inner = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                wash_cost = self.calculate_washing_price(car)
                total_inner += wash_cost
                self.wash_single_car(car)
        return round(total_inner, 1)

    def rate_service(self, new_raiting):
        new_average_rating = (self.average_rating * self.count_of_ratings) + new_raiting
        denominater = self.count_of_ratings + 1
        self.average_rating = (new_average_rating / denominater, 1)
        self.count_of_ratings += 1

# ===================================================
# ТЕСТУВАННЯ КОДУ
# ===================================================

# 1. Створення екземплярів (об'єктів)
# !!! УВАГА: Python використовує __init__, а не init.
#           Я виправив це в прикладі нижче, але перевірте свій код.

# Створення машини: comfort_class=3, clean_mark=1, brand="Toyota"
car1 = Car(comfort_class=3, clean_mark=1, brand="Toyota")

# Створення мийки: distance_from_city_center=10, clean_power=3, average_rating=4.5, count_of_ratings=10
wash_station = CarWashStation(
    distance_from_city_center=10,
    clean_power=3,
    average_rating=4.5,
    count_of_ratings=10
)

# 2. Перевірка методів

print(f"Початкова оцінка чистоти car1: {car1.clean_mark}")

# Розрахунок ціни
price = wash_station.calculate_washing_price(car1)
print(f"Вартість мийки car1: {price}") # Очікується: 3 * (3 - 1) / 10 * 4.5 = 2.7

# Мийка машини (зміна чистоти)
wash_station.wash_single_car(car1)
print(f"Оцінка чистоти car1 після мийки: {car1.clean_mark}") # Очікується: 3

# Перевірка rate_service
print(f"Початковий середній рейтинг: {wash_station.average_rating}")
wash_station.rate_service(5) # Нова оцінка 5
print(f"Середній рейтинг після оцінки 5: {wash_station.average_rating}") # Очікується зміна





