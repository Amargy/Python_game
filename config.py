#!/usr/bin/env python3
import os


IMAGE_SIZE = 128
SCREEN_SIZE = 512
NUM_TILES_SIDE = 4
NUM_TILES_TOTAL = 16
MARGIN = 4
BEAST_PNG_DIR = 'beasts_png'
BEAST_PNG_FILES = [x for x in os.listdir(BEAST_PNG_DIR) if x[-3:].lower() == 'png']

assert len(BEAST_PNG_FILES) == 8