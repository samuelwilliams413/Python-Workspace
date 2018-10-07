import libtcodpy as libtcod

from equipment_slots import EquipmentSlots

from components.equippable import Equippable

from entity import Entity


def item_dagger(x=0, y=0):
    equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=2, knockback_bonus=1)
    item = Entity(x, y, 'l', libtcod.darker_orange, 'Dagger', equippable=equippable_component)
    return item


def item_sword(x=0, y=0):
    equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=3)
    item = Entity(x, y, 'L', libtcod.darker_orange, 'Sword', equippable=equippable_component)
    return item


def item_mace(x=0, y=0):
    equippable_component = Equippable(EquipmentSlots.MAIN_HAND, power_bonus=9, knockback_bonus=10)
    item = Entity(x, y, 'P', libtcod.darker_orange, 'Mace', equippable=equippable_component)
    return item


def item_shield(x=0, y=0):
    equippable_component = Equippable(EquipmentSlots.OFF_HAND, defense_bonus=1)
    item = Entity(x, y, '[', libtcod.darker_orange, 'Shield', equippable=equippable_component)
    return item


def item_helmet(x=0, y=0):
    equippable_component = Equippable(EquipmentSlots.HEAD, defense_bonus=1, max_hp_bonus=1)
    item = Entity(x, y, '[', libtcod.darker_orange, 'Shield', equippable=equippable_component)
    return item