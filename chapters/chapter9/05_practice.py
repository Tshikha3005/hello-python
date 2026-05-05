from random import randint
class Train:
  def __init__(self, trainNo):
    self.trainNo = trainNo
  def book(self, fro, to):
    print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
  def getStatus(self):
    print(f"Train no: {self.trainNo} is running on time")
  def getFare(self, fro, to):
    print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to} the fair is {randint(222,5555)}")
    
rajdhani = Train(22345)
rajdhani.book("Delhi","Mumbai")
rajdhani.getStatus()
rajdhani.getFare("Delhi","Mumbai")