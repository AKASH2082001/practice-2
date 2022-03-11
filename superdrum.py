class Instrument:
    def sound(self):
        print("All instruments give sound")

class Drums(Instrument):
    def sound(self):
        super().sound()
        print("drums can make more noise")

ab = Drums()
ab.sound()