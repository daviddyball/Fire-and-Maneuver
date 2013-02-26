from pygamehelper import *
from pygame import *
from pygame.locals import *
from pygame.sprite import rect
from vec2d import *
from math import e, pi, cos, sin, sqrt, floor
from random import uniform

class Node(object):
    def __init__(self,x,y,size):
        self.rect = (x,y,size,size)
        self.g = None
        self.h = None
        self.f = None

def find_path(start,end,world):
    path = []
    start_node = Node(start.x,start.y,20)
    while

class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))
        self.click_pos = vec2d(self.w/2, self.h/2)
        self.dest_pos = vec2d(self.w/2, self.h/2)
        self.box_side = 20
        print "Horiz Squares: %f" % (self.w / self.box_side)
        print "Verti Squares: %f" % (self.h / self.box_side)
        
    def update(self):
        pass
        
    def keyUp(self, key):
        pass
        
    def mouseUp(self, button, pos):
        if button == 1:
            self.click_pos = vec2d(pos)
            print "New Position: %f,%f" % (self.click_pos.x, self.click_pos.y)
        if button == 3:
            self.dest_pos = vec2d(pos)
            print "New Destination: %f,%f" % (self.dest_pos.x, self.dest_pos.y)
        
    def mouseMotion(self, buttons, pos, rel):
        pass

    def collide(self, pos):
        for obstacle in self.obstacles:
            if sprite.rect(obstace.get_box(box_side).colliderect(sprite.rect(pos.get_box(box_side)))):
                return true
        
    def draw(self):
        self.screen.fill((255,255,255))

        # Draw Position
        pos_square_x = floor(self.click_pos.x / self.box_side)
        pos_square_y = floor(self.click_pos.y / self.box_side)
        pygame.draw.rect(self.screen,(255,0,0),
                         (pos_square_x*self.box_side,
                          pos_square_y*self.box_side,
                          self.box_side,
                          self.box_side))

        # Draw Destination
        if self.dest_pos != self.click_pos:
            dest_square_x = floor(self.dest_pos.x / self.box_side )
            dest_square_y = floor(self.dest_pos.y / self.box_side )
            pygame.draw.rect(self.screen,(0,255,0),
                             (dest_square_x * self.box_side,
                             dest_square_y * self.box_side,
                             self.box_side,
                             self.box_side))
            # Draw Path
            for node in find_path(self.click_pos, self.dest_pos,self):
                node_square_x = floor(node.x / self.box_side)
                node_square_y = floor(node.y / self.box_side)
                pygame.draw.rect(self.screen, (0,255,255)
                                (node_square_x * self.box_side,
                                 node_square_y * self.box_side,
                                 self.box_side,
                                 self.box_side))

        # Draw Horizontal Grid
        for i in range(self.w/self.box_side):
            pygame.draw.line(self.screen,(0,0,0),(i*self.box_side,0),(i*self.box_side,self.h),3)
        for i in range(self.h/self.box_side):
            pygame.draw.line(self.screen,(0,0,0),(0,self.box_side*i),(self.w,self.box_side*i),3)

s = Starter()
s.mainLoop(40)
