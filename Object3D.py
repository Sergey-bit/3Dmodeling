from math import pi, cos, sin
import pygame


class Object3D(object):
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

        # screen size
        self.height = self.screen.get_height()
        self.width = self.screen.get_width()

        # unit size
        self.block = 60

        # (0, 0) in coordinates
        self.x = self.width // 2
        self.y = self.height // 2

        # rotate angle
        self.angle = 0

        # Cube in coordinates
        self.points = [
            [-1, -1, -1],
            [-1, 1, -1],
            [1, -1, -1],
            [1, 1, -1],
            [-1, -1, 1],
            [-1, 1, 1],
            [1, -1, 1],
            [1, 1, 1]
        ]
        
        # cube colour
        self.colour = (179, 228, 27)

        # shear
        self.unit_shear = 1 / self.block

    def new_angle(self, angle: float):
        self.angle = angle * 180 / pi

    def shear(self, sx: int, sy: int):
        self.x += sx
        self.y -= sy

    def rotateX(self):
        for point in self.points:
            x, y, z = point

            point[0] = x
            point[1] = y * cos(self.angle) + z * sin(self.angle)
            point[2] = z * cos(self.angle) - y * sin(self.angle)

    def rotateY(self):
        for point in self.points:
            x, y, z = point

            point[0] = x * cos(self.angle) - z * sin(self.angle)
            point[1] = y
            point[2] = z * cos(self.angle) + x * sin(self.angle)
    
    def rotateZ(self):
        for point in self.points:
            x, y, z = point

            point[0] = x * cos(self.angle) + y * sin(self.angle)
            point[1] = y * cos(self.angle) - x * sin(self.angle)
            point[2] = z

    def scale(self, scaled: float):
        self.block *= scaled
    
    def to_pos(self, x: int, y: int):
        return self.x + self.block * x, self.y - self.block * y
    
    def __draw_point(self, point):
        pygame.draw.circle(self.screen, self.colour, self.to_pos(*point[:2]), 5)

    def __draw_line(self, s_pos, e_pos):
        pygame.draw.line(self.screen, self.colour, self.to_pos(*s_pos[:2]), self.to_pos(*e_pos[:2]))

    def draw(self):
        [self.__draw_point(point) for point in self.points]

        self.__draw_line(self.points[0], self.points[1])
        self.__draw_line(self.points[0], self.points[2])
        self.__draw_line(self.points[2], self.points[3])
        self.__draw_line(self.points[1], self.points[3])
        self.__draw_line(self.points[0], self.points[4])
        self.__draw_line(self.points[1], self.points[5])
        self.__draw_line(self.points[2], self.points[6])
        self.__draw_line(self.points[3], self.points[7])
        self.__draw_line(self.points[4], self.points[5])
        self.__draw_line(self.points[4], self.points[6])
        self.__draw_line(self.points[5], self.points[7])
        self.__draw_line(self.points[6], self.points[7])
