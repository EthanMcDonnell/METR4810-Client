
# Retrieved from: https://github.com/ChristianD37/YoutubeTutorials/tree/master/PS4%20Controller
import asyncio
import pygame
import json, os

################################# LOAD self.UP A BASIC WINDOW #################################


###########################################################################################



class Controller:

    def __init__(self):
        pass

class Game:
    
    def __init__(self):
        pygame.init()
        DISPLAY_W, DISPLAY_H = 960, 570
        self.canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
        self.window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
        self.running = True
        self.player = pygame.Rect(DISPLAY_W/2, DISPLAY_H/2, 60,60)
        
        self.clock = pygame.time.Clock()
        self.color = 0
        ###########################################################################################
        self.joysticks = []
        for i in range(pygame.joystick.get_count()):
            self.joysticks.append(pygame.joystick.Joystick(i))
        for joystick in self.joysticks:
            joystick.init()
        print(self.joysticks)

        with open(os.path.join("ps4_keys.json"), 'r+') as file:
            self.button_keys = json.load(file)
        # 0: Left analog horizonal, 1: Left Analog Vertical, 2: Right Analog Horizontal
        # 3: Right Analog Vertical 4: Left Trigger, 5: Right Trigger
        self.analog_keys = {0:0, 1:0, 2:0, 3:0, 4:-1, 5: -1 }
        self.encodable_analog_values = "Null"
        self.LEFT, self.RIGHT, self.UP, self.DOWN = False, False, False, False

    def run_game(self):
        ################################# CHECK PLAYER INPUT #################################
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                ############### UPDATE SPRITE IF SPACE IS PRESSED #################################
                pass

            # HANDLES BUTTON PRESSES
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == self.button_keys['left_arrow']:
                    self.LEFT = True
                if event.button == self.button_keys['right_arrow']:
                    self.RIGHT = True
                if event.button == self.button_keys['down_arrow']:
                    self.DOWN = True
                if event.button == self.button_keys['up_arrow']:
                    self.UP = True
            # HANDLES BUTTON RELEASES
            if event.type == pygame.JOYBUTTONUP:
                if event.button == self.button_keys['left_arrow']:
                    self.LEFT = False
                if event.button == self.button_keys['right_arrow']:
                    self.RIGHT = False
                if event.button == self.button_keys['down_arrow']:
                    self.DOWN = False
                if event.button == self.button_keys['up_arrow']:
                    self.UP = False

            #HANDLES ANALOG INPUTS
            if event.type == pygame.JOYAXISMOTION:

                self.analog_keys[event.axis] = event.value
                self.encodable_analog_values = str(list(self.analog_keys.values()))[1:-1].replace(" ","")
                print(self.analog_keys)
                # Horizontal Analog
                if abs(self.analog_keys[0]) > .4:
                    if self.analog_keys[0] < -.7:
                        self.LEFT = True
                    else:
                        self.LEFT = False
                    if self.analog_keys[0] > .7:
                        self.RIGHT = True
                    else:
                        self.RIGHT = False
                # Vertical Analog
                if abs(self.analog_keys[1]) > .4:
                    if self.analog_keys[1] < -.7:
                        self.UP = True
                    else:
                        self.UP = False
                    if self.analog_keys[1] > .7:
                        self.DOWN = True
                    else:
                        self.DOWN = False
                    # Triggers
                if self.analog_keys[4] > 0:  # Left trigger
                    self.color += 2
                if self.analog_keys[5] > 0:  # Right Trigger
                    self.color -= 2

        # Handle Player movement
        if self.LEFT:
            self.player.x -=5 #*(-1 * self.analog_keys[0])
        if self.RIGHT:
            self.player.x += 5 #* self.analog_keys[0]
        if self.UP:
            self.player.y -= 5
        if self.DOWN:
            self.player.y += 5

        if self.color < 0:
            self.color = 0
        elif self.color > 255:
            self.color = 255

        ################################# UPDATE WINDOW AND DISPLAY #################################
        self.canvas.fill((255,255,255))
        pygame.draw.rect(self.canvas, (0,0 + self.color,255), self.player)
        self.window.blit(self.canvas, (0,0))
        self.clock.tick(60)
        pygame.display.update()