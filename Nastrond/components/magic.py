import libtcodpy as libtcod

from components.item import *
from item_functions import *
from render_functions import RenderOrder
from entity import Entity



class Magic:
    def __init__(self):
        self.powers = []

    def add_power(self, power):
        self.powers.append(power)
