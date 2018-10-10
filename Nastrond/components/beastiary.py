

from components.fighter import Fighter
from entity import Entity
from render_functions import RenderOrder
from components.ai import *

#orc green - libtcod.desaturated_green
#bat violet - libtcod.desaturated_violet
#wraith violet - libtcod.desaturated_blue


def beast_cultist(x=0, y=0):
    fighter_component = Fighter(hp=20, defense=0, power=4, xp=35, knockback=0, strength=0, field_of_vision=2)
    ai_component = BasicMonster()

    monster = Entity(x, y, 'm', libtcod.dark_crimson,'Mook', fluff='Mook: A generic mook', blocks=True,
                     render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
    return monster

def beast_oni(x=0, y=0):
    fighter_component = Fighter(hp=30, defense=2, power=3, xp=150, strength=5, knockback=2)
    ai_component = BasicMonster()

    monster = Entity(x, y, 'B', libtcod.violet,'Big \'Un', fluff='Big \'Un: A large high HP, high damage unit, knock back (2+5)', blocks=True, fighter=fighter_component,
                     render_order=RenderOrder.ACTOR, ai=ai_component)
    return monster

def beast_imp(x=0, y=0):
    fighter_component = Fighter(hp=1, defense=0, power=3, xp=15, knockback=0, action_points=1, field_of_vision=0, speed=2)
    ai_component = BasicMonster()

    monster = Entity(x, y, 'q', libtcod.dark_crimson,'Quick', fluff='Quick: Fast unit that hunts in packs', blocks=True,
                     render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
    return monster

def beast_wraith(x=0, y=0):
    fighter_component = Fighter(hp=5, defense=0, power=10, xp=100, knockback=0, action_points=2, field_of_vision=25)
    ai_component = BasicMonster()

    monster = Entity(x, y, 's', libtcod.desaturated_violet, 'Stalker', fluff='Stalker: slow powerful hunter that sees the in the dark', blocks=True,
                     render_order=RenderOrder.ACTOR, fighter=fighter_component, ai=ai_component)
    return monster