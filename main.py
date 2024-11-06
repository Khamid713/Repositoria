class Player:
    def __init__(self, power, speed, accuracy, stamina):
        self.power = power
        self.speed = speed
        self.accuracy = accuracy
        self.stamina = stamina

class Goalkeeper(Player):
    def __init__(self, power, speed, accuracy, stamina):
        super().__init__(self, power, speed, accuracy, stamina)

    def save(self):
        print('Поймал мяч!')


class Defender(Player):
    def __init__(self, power, speed, accuracy, stamina):
        super().__init__(self, power, speed, accuracy, stamina)

    def block(self):
        print('Остановил нападающего!')


class Midfielder(Player):
    def __init__(self, power, speed, accuracy, stamina):
        super().__init__(self, power, speed, accuracy, stamina)

    def passing(self):
        print('Сделал пасс!')


class Striker(Player):
    def __init__(self, power, speed, accuracy, stamina):
        super().__init__(self, power, speed, accuracy, stamina)

    def goal(self):
        print('Забил гол!')