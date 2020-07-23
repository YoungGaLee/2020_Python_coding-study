#문제 : 범위에 맞게 출력문 출력 + 3년후 범위에서 다시 출력 

class Person:
    def __init__(self,initialAge):
        self.nai = initialAge
        self.after = initialAge + 3
        # Add some more code to run some checks on initialAge
    def amIOld(self):
        if self.nai < 0:
            print("Age is not valid, setting age to 0.")
        
        if 13 > self.nai : 
            print("You are young.")

        if 13 <= self.nai < 18 :
            print("You are a teenager.")

        if 18 <= self.nai :
            print("You are old.")


        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        self.nai = self.after
        if self.nai < 0 : 
            self.nai = 0
        # Increment the age of the person in here

t = int(input())
