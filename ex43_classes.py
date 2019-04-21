#Scene
class Scene(object):

    def enter(self):
        pass

#Engine
class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass


##Death
class Death(Scene):

    def enter(self):
        pass

#Central_corridor
class Central_corridor(Scene):

    def enter(self):
        pass

#Laser_Weapon_Amory
class Laser_Weapon_Amory(Scene):

    def enter(self):
        pass

#The Bridege
class TheBridge(Scene):

    def enter(self):
        pass

#EscapePod
class EscapePod(Scene):

    def enter(self):
        pass

#Map
class Map(object):

    def __init__(self,start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

## Test code
a_map = Map('central_corridor')
print(a_map)
a_game = Engine(a_map)
print(a_game)
a_game.play()
