from sys import exit
from random import randint
from textwrap import dedent

#Scene
class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

#Engine
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #be sure to print out the last scene
        current_scene.enter()



##Death
class Death(Scene):

    quips = [
        "You died. You kinda suck at this, bro.",
        "such a luser!",
        "I have a samll puppy that's better at this."
    ]

    def enter(self):
        print(Death.quips[randint(0,len(self.quip)-1)])
        exit(1)

#Central_corridor
class CentralCorridor(Scene):

    def enter(self):
        print("""
        The gothons of Planet Percal #25 have invaded your ship and destroyed
        your entire crew. You are the alst surviving member and your last
        mission is to get the neutron destruct bomb from the Weapons Armory
        put it in the bridge, and blow the ship up after getting into an
        escape pod.
        \n
        "You're running dow the central corridor to the Weapons Aromy When
        a Gothon jumps out, red scaly skin dark grimy teeth, and evil clown costume
        flowing around his hate filled body. He's blocking the door to the
        Aromy and about to pull a weapon to blast you.
        """)

        action = input("> ")

        if action == "shoot!":
            print("""
            Quick on the draw you yank out your blaster and fire it at the Gothon.
            His clown costume is flowing and moving around his body, which throws
            off your aim. Your laser hits his costume but misses him entirely.
            This completely ruins his brand new costume his mother bought him,
            which makes him fly into an insane rage and blast you repeatedly in
            the face until you are dead. Then he eats you.
            """)
            return 'death'

        elif action == "dodge!":
            print("""
            Like a world class boxer you doge, weave, slip and right
            as the Gothon's blaster cranks a laser past your head.
            In the middle of your artful dodge your foot slip and you bang
            your head on the metal wall and pass out.
            You Wake up shortly after only to die as the Gothon stamps on
            your head and eats you.
            """)
            return 'death'

        elif action == "tell a joke":
            print("Lucky for you they made you learn Gothon insults in the academy.")
            print("You tell the one Gothon joke you know:")
            print("Libhe zbgure cf fb sng, jura fur fvgf nebhaq, fur fvgf nebhaq ur!")
            print("The Gothon stops, tries not to laugh, then busts out laughing and can' move.")
            print("While he's laughing you run up and shoot him square in the head")
            print("putting him down, then jump through the Weapon Armory door.")
            return 'laser_weapon_armory'
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


#Laser_Weapon_Amory
class Laser_Weapon_Amory(Scene):

    def enter(self):
        print(
        """
        You do a dive roll into Weapon Armory, crouch and scan the room
        for more gothons that might be hiding. It's dead quiet, too quiet.
        You stand up and run to the far side of the room and find the
        neutron bomb in its container. There's a keypad lock on the box
        and you need the code to get the bomb out.
        If you get the code wrong 10 times then the lock closes forever
        and you can't get the bomb. The code is 3 digit.
        """
        )
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[kyepad]>")
        guesses = 0

        while guess != code and guesses < 10 :
            print("BZZZZEDDD!")
            if guess > code :
                print("your guess is larger than code")
            elif guess < code :
                print("your guess is smaller than code")
            guesses += 1
            guess = input("[keypad>]")

        if guess == code :
            print("""
            The container clicks open and the seal breaks,
            You grab the neutron bomb and run as fast as you can to
            the bridge where you must place it in the right spot.
            """)
            return 'the_bridge'
        else :
            print("""
            The lock buzzes one last time and then you hear a sickening
            """)
            return 'death'

#The Bridege
class TheBridge(Scene):

    def enter(self):
        print("""
        You burst onto the Bridge with the neutron bamp
        under your arm and surprise 7 Gothons who are trying to
        take control of the ship.
        Each of them has an even uglier clown costume than the last.
        They pulled their weapons out yet, as they see the active bomb
        under your arm and don't want to set if off.
        """)
        action = input("> ")

        if action == "Throw the bomb" :
            print("""
            In a panic, you throw the bomb at the group of Gothons.
            One of them catch the bomb and another shoot you.
            """)
            return 'death'
        elif action == "slowly place the bomb" :
            print(
            """
            You opint your blaster at the bomb under your arm and the Gothons
            put their hands up and star to sweat.
            You inch backward to the door and open it and the place the bomb
            one the floor, pointing yoour blaster at it.
            And you jump back through the door, punch the close button
            """)
            return 'escape_pod'
#EscapePod
class EscapePod(Scene):

    def enter(self):
        print(""""
        You rush through the ship desperately trying to make it
        to the escape pod before the whole ship explodes.
        You get to the chamber with the escape pod, some pods are damaged.
        There's 5 pods, which one do you take?
        Hint pod 1,2,3 are making noise and spark.
        """)

        guess = input("[pod #]> ")

        if int(guess) <= 3 :
            print("""
            You jump into the pod {guess} and soon, the pod is exploding.
            Your are an hero but can't survive.
            """)
            return 'death'
        else :
            print("""
            You jump into the pod {guess} and hit the eject button.
            You won!
            """)
        return 'finished'

#Finished
class Finished(Scene):

    def enter(self) :
        print("Good job.")

#Map
class Map(object):

    scenes = {
    'central_corridor' : CentralCorridor(),
    'laser_weapon_armory' : Laser_Weapon_Amory(),
    'the_bridge' : TheBridge(),
    'escape_pod' : EscapePod(),
    'finished' : Finished()
    }
    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

### @export "final_run"

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
