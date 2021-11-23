class InfoMessage:
    def __init__(
        self,
        training_type,
        duration,
        distance,
        speed,
        calories
    ):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        text = (
            f'Тип тренировки: {self.training_type}; '
            + f'Длительность: {self.duration} ч.; '
            + f'Дистанция: {self.distance} км; '
            + f'Ср. скорость: {self.speed} км/ч; '
            + f'Потрачено ккал: {self.calories}.'
        )
        return text


class Training:
    LEN_STEP = 0.65
    M_IN_KM = 1000
    MIN_IN_HOUR = 60
    training_type = 'Base training'

    def __init__(
        self,
        action,
        duration,
        weight
    ):
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self):
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self):
        return self.get_distance() / self.duration

    def get_spent_calories(self):
        pass

    def show_training_info(self):
        training_type = self.training_type
        duration = self.duration
        distance = self.get_distance()
        speed = self.get_mean_speed()
        calories = self.get_spent_calories()
        return InfoMessage(training_type, duration, distance, speed, calories)


class Running(Training):
    training_type = 'Running'

    def get_spent_calories(self):
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        spent_calories = (
            (
                coeff_calorie_1
                * self.get_mean_speed()
                - coeff_calorie_2
            ) * self.weight / self.M_IN_KM
            * self.duration * self.MIN_IN_HOUR
        )
        return spent_calories


class SportsWalking(Training):
    training_type = 'SportsWalking'

    def __init__(
        self,
        action,
        duration,
        weight,
        height
    ):
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self):
        coeff_calorie_1 = 0.035
        coeff_calorie_2 = 0.029
        spent_calories = (
            (
                coeff_calorie_1
                * self.weight
                + (
                    self.get_mean_speed()**2
                    // self.height
                )
                * coeff_calorie_2
                * self.weight
            )
            * self.duration
            * self.MIN_IN_HOUR
        )
        return spent_calories


class Swimming(Training):
    training_type = 'Swimming'
    LEN_STEP = 1.38

    def __init__(
        self,
        action,
        duration,
        weight,
        length_pool,
        count_pool
    ):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self):
        mean_speed = (
            self.length_pool * self.count_pool
            / self.M_IN_KM / self.duration
        )
        return mean_speed

    def get_spent_calories(self):
        coeff_calorie_1 = 1.1
        coeff_calorie_2 = 2
        spent_calories = (
            (self.get_mean_speed() + coeff_calorie_1)
            * coeff_calorie_2 * self.weight
        )
        return spent_calories


def read_package(workout_type, data):
    trainings = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    training_object = trainings[workout_type](*data)
    return training_object


def main(training):
    info = training.show_training_info()
    info_message = info.get_message()
    print(info_message)


packages = [
    ('SWM', [720, 1, 80, 25, 40]),
    ('RUN', [15000, 1, 75]),
    ('WLK', [9000, 1, 75, 180]),
]

for workout_type, data in packages:
    training = read_package(workout_type, data)
    main(training)
