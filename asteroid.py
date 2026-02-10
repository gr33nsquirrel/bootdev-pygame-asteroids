import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event

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

    def split(self):
         pygame.sprite.Sprite.kill(self)
         if self.radius <= ASTEROID_MIN_RADIUS:
              return
         else:
              log_event("asteroid_split")
              random_angle = random.uniform(20, 50)
              nav1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
              nav2 = pygame.math.Vector2.rotate(-self.velocity, random_angle)
              new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
              new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
              new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
              new_asteroid_1.velocity = nav1 * 1.2
              new_asteroid_2.velocity = nav2 * 1.2



    
    