class Car:
    def __init__(self , name , color , manufactor ):

        self.name = name
        self.color = color
        self.manufactor = manufactor


    def start(self):
        print("Starting the engine ")
    
    def turn(self , turn):
        print(f"Turned {turn}")

    