
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS
import pygame
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # Additional initialization for Asteroid can go here

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        # Update asteroid position based on its velocity
        self.position += self.velocity * dt
    
    def split(self):
        # Logic to split the asteroid into smaller asteroids
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        #log_event("asteroid_split")
        new_angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = self.velocity.rotate(new_angle)
        asteroid2.velocity = self.velocity.rotate(-new_angle)
