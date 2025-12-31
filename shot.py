import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, 5)
        self.direction = direction
        self.speed = 500  # pixels per second

    def update(self, dt):
        movement = pygame.Vector2(0, 1).rotate(self.direction) * self.speed * dt
        self.position += movement   
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)