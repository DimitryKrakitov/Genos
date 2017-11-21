class room:
    def __init__(self, fenixAPI_r_info):
        #parse fenixAPI_r_info from the fenixedu API
        self.limit = 0 #Full student capacity - from fenixAPI_r_info
        self.id = 'x' #Room ID - from fenixAPI_r_info
        self.current_ocupation = 0
        self.users = []

    def insertEntryPlug(self, user):
        if self.current_ocupation < self.limit:
            user.GetInTheFuckingRobotShinji(self)
            self.current_ocupation += 1
            self.users.append(user)
