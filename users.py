



class Admin:
    def __init__(self):
        self.id = 'Genos'

class Reg:
    max_users = 0
    def __init__(self, ID, r = []):
        Reg.max_users += 1
        self.id = ID
        self.room = r

    def GetInTheFuckingRobotShinji(self, r):
        self.room = r

    def IsShinjiInTheRobot(self):
        if self.room:
            return self.room
        return []

    def EjectEntryPlug(self):
        self.room = []



