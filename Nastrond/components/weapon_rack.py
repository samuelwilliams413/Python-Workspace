import libtcodpy as libtcod

from equipment_slots import EquipmentSlots

from components.equippable import Equippable

from entity import Entity

# metallic
#brass=Color(191,151,96)
#copper=Color(197,136,124)
#gold=Color(229,191,0)
#silver=Color(203,203,203)

def item_dagger(x=0, y=0):
    equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=2, knockback_bonus=0)
    item = Entity(x, y, 'l', libtcod.brass, 'Dagger', fluff="Dagger: Your trust dagger", equippable=equippable_component)
    return item


def item_sword(x=0, y=0):
    equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=3)
    item = Entity(x, y, 'L', libtcod.brass, 'Sword', equippable=equippable_component)
    return item


def item_mace(x=0, y=0):
    equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=1, knockback_bonus=2)
    item = Entity(x, y, 'P', libtcod.brass, 'Mace', equippable=equippable_component)
    return item


def item_shield(x=0, y=0):
    equippable_component = Equippable(EquipmentSlots.OFF_HAND, defense_bonus=1)
    item = Entity(x, y, '[', libtcod.dark_orange, 'Shield', equippable=equippable_component)
    return item


def item_helmet(x=0, y=0):
    equippable_component = Equippable(EquipmentSlots.HEAD, defense_bonus=1, max_hp_bonus=1)
    item = Entity(x, y, '[', libtcod.dark_orange, 'Helmet', equippable=equippable_component)
    return item


def item_torch(x=0, y=0):
    equippable_component = Equippable(EquipmentSlots.OFF_HAND, field_of_vision_bonus=7)
    item = Entity(x, y, 'T', libtcod.dark_orange, 'Torch', equippable=equippable_component)
    return item


def item_headlamp(x=0, y=0):
    equippable_component = Equippable(EquipmentSlots.HEAD, field_of_vision_bonus=4)
    item = Entity(x, y, 'O', libtcod.dark_orange, 'Headlamp', equippable=equippable_component)
    return item


def item_oldcloak(x=0, y=0):
    equippable_component = Equippable(EquipmentSlots.BACK)
    item = Entity(x, y, 'O', libtcod.dark_orange, 'Tattered Cloak', equippable=equippable_component)
    return item


def item_oldpants(x=0, y=0):
    equippable_component = Equippable(EquipmentSlots.LEGS)
    item = Entity(x, y, 'O', libtcod.dark_orange, 'Torn Pants', equippable=equippable_component)
    return item


def item_oldtunic(x=0, y=0):
    equippable_component = Equippable(EquipmentSlots.TORSO, defense_bonus=1)
    item = Entity(x, y, 'O', libtcod.dark_orange, 'Old Tunic', equippable=equippable_component)
    return item


def item_oldboots(x=0, y=0):
    equippable_component = Equippable(EquipmentSlots.FEET)
    item = Entity(x, y, 'O', libtcod.dark_orange, 'Battered Boots', equippable=equippable_component)
    return item
