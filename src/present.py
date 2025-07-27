import pygame
import random
import math
from collections import deque

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
LINE_THICKNESS = 8
LINE_SPEED = 5
FILLED_PIXEL_THRESHOLD = 200
SPAWN_INTERVAL = 1000


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Line:
    def __init__(self, start_pos, speed, direction_change_interval_ms, line_thickness, color):
        self.current_pos = pygame.Vector2(start_pos)
        self.speed = speed
        self.direction = pygame.Vector2(random.uniform(-1, 1),
                random.uniform(-1, 1)).normalize()
        self.path_points = [self.current_pos.copy()]
        self.last_point = self.current_pos.copy()
        self.direction_change_interval_ms = direction_change_interval_ms
        self.last_change_tick = pygame.time.get_ticks()
        self.line_thickness = line_thickness
        self.color = color

    def update(self, current_ticks):
        if current_ticks - self.last_change_tick > self.direction_change_interval_ms:
            self.direction.rotate_ip(random.uniform(-45, 45))
            self.direction.normalize_ip()
            self.last_change_tick = current_ticks

        new_pos = self.current_pos + self.direction * self.speed

        if not (0 <= new_pos.x <= SCREEN_WIDTH):
            self.direction.x *= -1
            new_pos.x = max(0, min(SCREEN_WIDTH, new_pos.x))
        if not (0 <= new_pos.y <= SCREEN_HEIGHT):
            self.direction.y *= -1
            new_pos.y = max(0, min(SCREEN_HEIGHT, new_pos.y))

        self.last_point = self.current_pos.copy()
        self.current_pos = new_pos
        self.path_points.append(self.current_pos.copy())

    def draw(self, surface):
        if len(self.path_points) > 1:
            pygame.draw.line(surface,
                    self.color,
                    self.last_point,
                    self.current_pos,
                    self.line_thickness)


def get_random_color():
    '''Generate a color in RGB format.'''
    return tuple(random.randrange(0, 200) for i in range(3))

def is_valid_point(x, y):
    '''check if x-y coordinate is within bounds of the screen.'''
    return 0 <= x < SCREEN_WIDTH and 0 <= y < SCREEN_HEIGHT


def present(midi_file, tempo):
    pygame.init()
    pygame.mixer.init()
    
    screen_dimensions = (SCREEN_WIDTH, SCREEN_HEIGHT)

    screen = pygame.display.set_mode(screen_dimensions)


    # used for flood fill detection
    line_surface = pygame.Surface(screen_dimensions, pygame.SRCALPHA)
    line_surface.fill((0, 0, 0, 0)) # starts transparent

    active_lines = []

    last_spawn_time = pygame.time.get_ticks()

    tempo_convert = 1000 / (tempo / 60)

    active_lines.append(Line(
        (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
        LINE_SPEED,
        tempo_convert,
        LINE_THICKNESS,
        get_random_color()
    ))

    running = True
    midi_playing = False
    
    clock = pygame.time.Clock()


    pygame.mixer.music.load(midi_file)
    pygame.mixer.music.play()
    midi_playing = True


    while running:
        current_ticks = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT and event.code == 'MIDI_ENDEVENT':
                running = False

        if midi_playing and not pygame.mixer.music.get_busy():
            running = False


        if current_ticks - last_spawn_time >= tempo_convert:
            start_x = random.randint(0, SCREEN_WIDTH)
            start_y = random.randint(0, SCREEN_HEIGHT)
            next_color = get_random_color()
            active_lines.append(Line(
                (start_x, start_y),
                LINE_SPEED,
                random.randint(100, 300),
                LINE_THICKNESS,
                next_color
            ))
            last_spawn_time = current_ticks

        screen.fill(WHITE)

        for line in active_lines:
            line.update(current_ticks)
            line.draw(line_surface)
        
        screen.blit(line_surface, (0,0))

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
