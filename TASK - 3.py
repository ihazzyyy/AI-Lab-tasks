class reflex:
    def __init__(self,temp):
        self.desired_temp = temp

    def percieve(self):
        return float(input('Enter the current temprature: '))

    def act(self, temp):
        if temp >= self.desired_temp:
            print(f'Temprature: {temp} turn off the heater: ')

        else:
            print(f'Temprature: {temp} turn on the heater: ')

rooms = {
    'living room ': 16 ,
    'bedroom': 20,
    'drawing room': 18,
    'bathroom': 22,
}

for  room, temp in rooms.items():
    print(room, temp)

desired_temp = float(input('Enter the desired temprature: '))
reflex = reflex(desired_temp)

current_temp = reflex.percieve()
reflex.act(current_temp)
      

