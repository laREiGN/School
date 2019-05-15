class LightBulb():
    
    lightState = False
    def __init__(self, state):
        self.lightState = state
    def turn_on(self):
        self.lightState = True
        self.status()
    def turn_off(self):
        self.lightState = False
        self.status()
    def toggle(self):
        if self.lightState == True:
            self.lightState = False
            self.status()
        else:
            self.lightState = True
            self.status()
    def status(self):
        if self.lightState == True:
            print('light = True')
        else:
            print('light = False')


light = LightBulb(False)

test_case = int(input('How many times do you want to toggle?'))
for i in range(test_case):
    light.toggle()


