class Person:
    def __init__(self,initialAge):
        if initialAge<0:
            print("Age is not valid, setting age to 0.")
            initialAge=0
        self.Age=initialAge
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.Age<13:
            print("You are young.")
            return
        if 13<=self.Age<18:
            print("You are a teenager.")
            return
        print("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        self.Age+=1

