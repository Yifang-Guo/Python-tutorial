class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def moves(self):
        print('moves along... ')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")

my_car = Vehicle("Ford", "TX7")

print(my_car.make)
print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Cadillac', 'Escalate')
your_car.get_make_model()
your_car.moves()


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id
    
    def moves(self):
        print('flies along...')


class Truck(Vehicle):
    def moves(self):
        print('rumbles along...')

cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
mack = Truck('Mack', 'Pinnacle')

cessna.get_make_model()
cessna.moves()

mack.get_make_model()
mack.moves()

print("\n\n")

for v in (my_car, your_car, cessna, mack):
    v.get_make_model()
    v.moves()