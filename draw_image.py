from time import sleep
import config as gc


def draw_content_in_window(bloodhunt, screen):
    screen.fill((255, 255, 255))
    for tile in bloodhunt.tiles:
        image_i = tile.image if tile.index in bloodhunt.current_images else tile.box

        if not tile.skip:
            screen.blit(image_i, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))


def catch_two_images_and_compare_them(bloodhunt, screen, display):
    if len(bloodhunt.current_images) == 2:
        idx1, idx2 = bloodhunt.current_images
        if bloodhunt.tiles[idx1].name == bloodhunt.tiles[idx2].name:
            bloodhunt.tiles[idx1].skip = True
            bloodhunt.tiles[idx2].skip = True
            sleep(0.4)
            screen.blit(bloodhunt.matched, (0, 0))
            display.flip()
            sleep(0.4)
            bloodhunt.current_images = []