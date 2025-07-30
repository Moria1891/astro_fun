from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random
class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        # print(f"Asteroid created at ({x}, {y}) with radius {radius}")
        
    def draw(self, screen):
        pygame.draw.circle(screen,(255, 255, 255),self.position,self.radius ,2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        """
        Splits the asteroid into smaller asteroids if its radius is greater than ASTEROID_MIN_RADIUS.

        Returns:
            list: A list of new Asteroid instances if split occurs, otherwise an empty list.
        """
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return []
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroids = []
            angle = random.uniform(20, 50)
            offset = pygame.Vector2(new_radius, 0).rotate(angle)
            new_position = self.position + offset

            new_asteroids_1 = (new_position.x, new_position.y, new_radius)
            new_asteroids_2 = (new_position.x, new_position.y, new_radius)

            asteroid1 = Asteroid(*new_asteroids_1)
            asteroid2 = Asteroid(*new_asteroids_2) 



            asteroid1.velocity = self.velocity.rotate(angle) * 1.2
            asteroid2.velocity = self.velocity.rotate(-angle) * 1.2

            new_asteroids.append(asteroid1)
            new_asteroids.append(asteroid2)
    


            return new_asteroids