import config as gc


def events_handler(current_events, pygame, bloodhunt):
    for e in current_events:
        check_quit_game(e, current_events, pygame, bloodhunt)
        check_mouse_clicks(e, current_events, pygame, bloodhunt)


def check_quit_game(e, current_events, pygame, bloodhunt):
    if e.type == pygame.QUIT:
        bloodhunt.running = False

    if e.type == pygame.KEYDOWN:
         if e.key == pygame.K_ESCAPE:
            bloodhunt.running = False


def check_mouse_clicks(e, current_events, pygame, bloodhunt):
    if e.type == pygame.MOUSEBUTTONDOWN:
        index = find_tile_where_mouse_click(pygame)
        add_tile_for_compare_with_another_tile(index, bloodhunt)


def find_tile_where_mouse_click(pygame):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return (find_index(mouse_x, mouse_y))


def find_index(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return index


def add_tile_for_compare_with_another_tile(index, bloodhunt):
    if index not in bloodhunt.current_images:
        bloodhunt.current_images.append(index)

    if len(bloodhunt.current_images) > 2:
        bloodhunt.current_images = bloodhunt.current_images[1:]

