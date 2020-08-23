#!/usr/bin/env python3
import os
import random
import config as gc
from pygame import image, transform


beasts_count = dict((a, 0) for a in gc.BEAST_PNG_FILES)


class Main_BloodHunt_class:
    def __init__(self):
        self.matched = image.load('other_png/success.png')
        self.tiles = [Beast(i) for i in range(0, gc.NUM_TILES_TOTAL)]
        self.current_images = []
        self.running = True


def available_beasts():
        return [a for a, c in beasts_count.items() if c < 2]


class Beast:
    def __init__(self, index):
        self.index = index
        self.row = index // gc.NUM_TILES_SIDE
        self.col = index % gc.NUM_TILES_SIDE
        self.name = random.choice(available_beasts())
        beasts_count[self.name] += 1

        self.image_path = os.path.join(gc.BEAST_PNG_DIR, self.name)
        self.image = image.load(self.image_path)
        self.image = transform.scale(self.image,
        (gc.IMAGE_SIZE - 2*gc.MARGIN, gc.IMAGE_SIZE - 2*gc.MARGIN))
        self.box = self.image.copy()
        self.box.fill((200, 200, 200))
        self.skip = False
        