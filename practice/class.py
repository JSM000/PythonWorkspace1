class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("flyable 생성자")

class FlyableUnit(Unit):
    def __init__(self):
        super().__init__()
