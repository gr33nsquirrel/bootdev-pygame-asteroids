import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

# asteroid class
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # draw asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, LINE_WIDTH)

    # update asteroid
    def update(self, dt):
            self.position += self.velocity * dt
    
    