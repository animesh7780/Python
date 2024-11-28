from random import randint
class Train:
    def __init__(slf, trainNumber):
        slf.trainNumber = trainNumber
        
    def book(self, source, destination,):
        print(f"Ticket Booked {self.trainNumber} from {source} to {destination}")
    
    def getStatus(self):
        
        print(f"Ticket Booked in {self.trainNumber} is running")
    
    def getFare(self):
        print(f"Ticket fare is Rs {randint(100, 2000)}")
        
t =  Train(12132)
t.book("Delhi", "Mumbai")
t.getStatus()
t.getFare() 