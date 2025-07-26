import pygame

def present(midi_file):
    pygame.init()
    pygame.mixer.music.load(midi_file)
    pygame.display.set_mode((800, 600))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.wait(1000)

    pygame.quit()
