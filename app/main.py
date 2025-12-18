class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: int) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int,
                 average_rating: int, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car) -> float:
        cost = (car.comfort_class *
                (self.clean_power - car.clean_mark)
                / self.distance_from_city_center
                * self.average_rating)
        return round(cost, 1)

    def wash_single_car(self, car) -> float:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def several_cars(self, cars) -> float:
        total_inner = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                wash_cost = self.calculate_washing_price(car)
                total_inner += wash_cost
                self.wash_single_car(car)
        return round(total_inner, 1)

    def rate_service(self, new_raiting):
        new_average_rating = (self.average_rating
                              * self.count_of_ratings) + new_raiting
        denominater = self.count_of_ratings + 1
        self.average_rating = (new_average_rating / denominater, 1)
        self.count_of_ratings += 1




