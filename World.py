from Objects import *

class World(object):
    def __init__(self, w, h):
        self.w, self.h = w,h
        self.all_objects = []
        self.drawable_objects = []
        self.static_objects = []
        self.actors = []

    def add_object(self, obj):
        # Add to all_objects
        self.all_objects.append(obj)
        
        # Is Drawable?
        if issubclass(obj.__class__, DrawableObject):
            self.drawable_objects.append(obj)
        
        # Is Static?
        if issubclass(obj.__class__, StaticObject):
            self.static_objects.append(obj)

        # Is Actor w/update()
        if issubclass(obj.__class__, Actor):
            self.actors.append(obj)

    def remove_object(self, obj):
        self.all_objects.remove(obj)
        if obj in self.drawable_objects:
            self.drawable_objects.remove(obj)
        if obj in self.static_objects:
            self.static_objects.remove(obj)
        if obj in self.actor:
            self.actors.remove(obj)
