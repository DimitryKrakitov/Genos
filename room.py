
class ist_map:
    n_nodes = 0
    nodes = []
    def __init__(self):
        n_nodes = 0

    def construction(self, client):
        # God node (IST):
        god = node()
        ist_map.n_nodes = 1
        #Make all the gets to fenix, and build the tree representing the map
        campus_spaces = client.get_spaces()
        for campus in campus_spaces:
            aux_campus = node(panode=god, id=campus['id'], type=campus['type'], name=campus['name'])
            ist_map.append(aux_campus)
            ist_map.n_nodes = ist_map.n_nodes + 1
            campus_info = client.get_space(campus['id'])
            for building in campus_info['containedSpaces']:
                aux_building = node(panode=aux_campus, id=building['id'], type=building['type'], name=building['name'])
                ist_map.append(aux_building)
                ist_map.n_nodes = ist_map.n_nodes + 1
                building_info = client.get_space(building['id'])# a building can have floors or rooms (wth no floors)
                # In case of not having floors, we put generate a dummy floor = 0 node ????
                for floor_room in building_info['containedSpaces']:
                    if(floor_room['type'] == "FLOOR"):
                        floor_aux = node(panode=aux_building, id=floor_room['id'], type=floor_room['type'], name=floor_room['name'])
                        ist_map.append(floor_aux)
                        ist_map.n_nodes = ist_map.n_nodes + 1
                        floor_info = client.get_space(floor_room['id'])
                        for room in floor_info['containedSpaces']:
                            aux_room = room(panode=floor_aux, id=room['id'], type=room['type'], name=room['name']) ######### ADD THE LIMIT !!!!!
                            ist_map.append(aux_room)
                            ist_map.n_nodes = ist_map.n_nodes + 1
                    else:
                        aux_room = room(panode=aux_building, id=floor_room['id'], type=floor_room['type'], name=floor_room['name'])  ######### ADD THE LIMIT !!!!!
                        ist_map.append(aux_room)
                        ist_map.n_nodes = ist_map.n_nodes + 1


class node:

    def __init__(self,panode = [], id = 1, type = "God", name = "God"): # Default case is god node
        self.name = name
        self.type = type # If this is a floor, campus...
        self.id = id  # ID - from fenixAPI_r_info
        self.parent = panode
        self.children = []

    def append_children(self, children):
        self.children.append(children)

class room:
    def __init__(self, panode, id, name):
        #parse fenixAPI_r_info from the fenixedu API
        self.name = name
        self.limit = 0 #Full student capacity - from fenixAPI_r_info
        self.type = "Room"
        self.parent = panode
        self.id = id #Room ID - from fenixAPI_r_info
        self.current_ocupation = 0
        self.users = []

    def insertEntryPlug(self, user):
        if self.current_ocupation < self.limit:
            user.GetInTheFuckingRobotShinji(self)
            self.current_ocupation += 1
            self.users.append(user)
