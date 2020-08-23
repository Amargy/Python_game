#!/usr/bin/env python3


                        ### BLOODHUNT ###


import pygame
import config as gc

from blood_events import events_handler
from class_collection import Main_BloodHunt_class
from class_collection import Beast
from pygame import display, event, image
from time import sleep
from draw_image import draw_content_in_window
from draw_image import catch_two_images_and_compare_them


pygame.init()
display.set_caption("BloodHunt")
screen = display.set_mode((512, 512))
bloodhunt = Main_BloodHunt_class()


if __name__ == '__main__':
    while bloodhunt.running:
        current_events = event.get()
        events_handler(current_events, pygame, bloodhunt)
        draw_content_in_window(bloodhunt, screen)
        catch_two_images_and_compare_them(bloodhunt, screen, display)
        display.flip()