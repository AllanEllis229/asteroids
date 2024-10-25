import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other_circle):
        distance = self.position.distance_to(other_circle.position)
        r1 = self.radius
        r2 = other_circle.radius

        if distance <= r1 + r2:
            return True
        return False

