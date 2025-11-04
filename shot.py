from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, SHOT_RADIUS)
        self.direction = direction.normalize()
        self.speed = PLAYER_SHOOT_SPEED

    def update(self, dt):
        self.position += self.direction * self.speed * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)

    