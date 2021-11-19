import pygame

pygame.mixer.init()

FLASH = pygame.mixer.Sound('sound/flash.ogg')
RED = pygame.mixer.Sound('sound/laser.wav')
GREEN = pygame.mixer.Sound('sound/shoot1.wav')
EXPLOSION = pygame.mixer.Sound('sound/explosion5.mp3')
EAT = pygame.mixer.Sound('sound/eat.ogg')
CHICK = pygame.mixer.Sound('sound/chick.wav')
POWERUP = pygame.mixer.Sound('sound/powerup.mp3')
CLICK = pygame.mixer.Sound('sound/click.wav')
CLUCK = pygame.mixer.Sound('sound/cluck.wav')
SELECTOR = pygame.mixer.Sound('sound/selector.wav')
MUSIC = pygame.mixer.Sound('sound/Chicken Invaders 4 (Ultimate Omelette) OST - Chapter 3_ Chapter 11 (HQ).ogg')
BOSS_MUSIC = pygame.mixer.Sound('sound/Chicken Invaders 4 (Ultimate Omelette) OST - Boss Theme (HQ).ogg')
TITLE_MUSIC = pygame.mixer.Sound('sound/Chicken Invaders 4 (Ultimate Omelette) OST - Title Theme (HQ).ogg')


RED.set_volume(0.4)
GREEN.set_volume(0.3)
EAT.set_volume(0.2)
MUSIC.set_volume(0.4)
BOSS_MUSIC.set_volume(0.5)
TITLE_MUSIC.set_volume(0.5)

class SFx:
    def __init__(self):
        self.ms = {'flash':FLASH,
            'red':RED,
            'green':GREEN,
            'explosion':EXPLOSION,
            'eat':EAT,
            'chick':CHICK,
            'cluck':CLUCK,
            'powerup':POWERUP,
            'click':CLICK,
            'selector':SELECTOR,
            'music':MUSIC,
            'boss_music':BOSS_MUSIC,
            'title_music':TITLE_MUSIC}

    def getSFx(self,s):
        return self.ms[s]
