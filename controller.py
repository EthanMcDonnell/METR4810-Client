
# Retrieved from: https://github.com/ChristianD37/YoutubeTutorials/tree/master/PS4%20Controller
import pygame
import json, os

class Game:
    
    def __init__(self):
        """
        Initialises the Game, inlcuding joysticks, GUI etc.
        """
        pygame.init()
        DISPLAY_W, DISPLAY_H = 960, 570
        self.canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
        self.window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
        self.running = True
        self.player = pygame.Rect(DISPLAY_W/2, DISPLAY_H/2, 60,60)
        self.analogValuesAssigned = False
        self.clock = pygame.time.Clock()
        self.color = 0
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

    
    def run_game(self):
        """
        Single loop of game
        """
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                pass

            # Analog Inputs
            if event.type == pygame.JOYAXISMOTION:
                self.analog_keys[event.axis] = event.value
                self.analogValuesAssigned = True
                self.encodable_analog_values = str(list(self.analog_keys.values()))[1:-1].replace(" ","")
                    
        # Update windown and display
        self.canvas.fill((255,255,255))
        pygame.draw.rect(self.canvas, (0,0 + self.color,255), self.player)
        self.window.blit(self.canvas, (0,0))
        self.clock.tick(60)
        pygame.display.update()