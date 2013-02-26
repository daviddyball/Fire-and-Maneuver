from pygame import Rect

class GameObject(object):
    def __init__(self)
        self.rect = Rect(0,0,0,0)

class DrawableObject(GameObject):
    def draw(self, world):
        pass

class StaticObject(DrawableObject):
    pass

class AnimatedObject(DrawableObject):
    def update(self):
        pass

class Actor(AnimatedObject):
    def update(self):
        
