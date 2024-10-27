import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # randomize the angle of the split    
        angle = random.uniform(20, 50)

        new_velocity_1 = self.velocity.rotate(angle) * 1.2
        new_velocity_2 = self.velocity.rotate(-angle) * 1.2


        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = new_velocity_1 * 1.2
        asteroid.velocity = new_velocity_2 * 1.2



