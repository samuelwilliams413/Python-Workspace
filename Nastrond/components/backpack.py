import libtcodpy as libtcod

from equipment_slots import EquipmentSlots

from components.equippable import Equippable
from components.item import Item

from item_functions import *
from entity import Entity
from rarity import Rarity
from render_functions import RenderOrder

def item_pot_heal(x=0, y=0):
    item_component = Item(use_function=heal, amount=40)
    item = Entity(x, y, '!', libtcod.violet, 'Healing Potion', render_order=RenderOrder.ITEM,
                  item=item_component)
    return item


def item_scroll_lightning(x=0, y=0):
    item_component = Item(use_function=cast_lightning, damage=40, maximum_range=5)
    item = Entity(x, y, '#', libtcod.yellow, 'Lightning Scroll', render_order=RenderOrder.ITEM,
                  item=item_component)
    return item


def item_scroll_fireball(x=0, y=0):
    item_component = Item(use_function=cast_fireball, targeting=True, targeting_message=Message(
        'Left-click a target tile for the fireball, or right-click to cancel.', libtcod.light_cyan),
                          damage=25, radius=3)
    item = Entity(x, y, '#', libtcod.red, 'Fireball Scroll', render_order=RenderOrder.ITEM,
                  item=item_component)
    return item

def item_scroll_confusion(x=0, y=0):
    item_component = Item(use_function=cast_confuse, targeting=True, targeting_message=Message(
        'Left-click an enemy to confuse it, or right-click to cancel.', libtcod.light_cyan))
    item = Entity(x, y, '#', libtcod.light_pink, 'Confusion Scroll', render_order=RenderOrder.ITEM,
                  item=item_component)
    return item

def item_scroll_teleport(x=0, y=0):
    item_component = Item(use_function=cast_teleport, targeting=True, targeting_message=Message(
        'Left-click a tile to teleport, or right-click to cancel.', libtcod.light_cyan))
    item = Entity(x, y, '#', libtcod.light_green, 'Teleportation Scroll', render_order=RenderOrder.ITEM,
                  item=item_component)
    return item