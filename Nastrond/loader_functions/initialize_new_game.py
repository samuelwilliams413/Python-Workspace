import libtcodpy as libtcod

from components.equipment import Equipment

from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from components.weapon_rack import *
from components.magic import *

from entity import Entity




from game_messages import MessageLog

from game_states import GameStates

from map_objects.game_map import GameMap

from render_functions import RenderOrder


def get_constants():
    window_title = 'Nastrond'

    screen_width = 80
    screen_height = 50

    bar_width = 20
    panel_height = 7
    panel_y = screen_height - panel_height

    message_x = bar_width + 2
    message_width = screen_width - bar_width - 2
    message_height = panel_height - 1

    map_width = 80
    map_height = 43

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = 10

    max_monsters_per_room = 3
    max_items_per_room = 2

    colors = {
        'dark_wall': libtcod.Color(59, 59, 59),
        'dark_ground': libtcod.Color(80, 80, 80),
        'light_wall': libtcod.Color(130, 110, 50),
        'light_ground': libtcod.Color(200, 180, 50)
    }

    constants = {
        'window_title': window_title,
        'screen_width': screen_width,
        'screen_height': screen_height,
        'bar_width': bar_width,
        'panel_height': panel_height,
        'panel_y': panel_y,
        'message_x': message_x,
        'message_width': message_width,
        'message_height': message_height,
        'map_width': map_width,
        'map_height': map_height,
        'room_max_size': room_max_size,
        'room_min_size': room_min_size,
        'max_rooms': max_rooms,
        'fov_algorithm': fov_algorithm,
        'fov_light_walls': fov_light_walls,
        'fov_radius': fov_radius,
        'max_monsters_per_room': max_monsters_per_room,
        'max_items_per_room': max_items_per_room,
        'colors': colors
    }

    return constants


def get_game_variables(constants):
    fighter_component = Fighter(hp=100, defense=6, power=2, knockback=0, strength=1, agility=1, toughness=1,
                                intelligence=1, resolve=1, ego=1, vim=10, action_points=1)

    inventory_component = Inventory(20)
    level_component = Level()
    equipment_component = Equipment()

    magic_component = Magic()
    power_item_component = Item(use_function=heal, amount=20, power=True, cost=5)
    p = Entity(0, 0, '!', libtcod.violet, 'Healing Potion', render_order=RenderOrder.ITEM,
               item=power_item_component)
    magic_component.add_power(p)

    power_item_component = Item(use_function=cast_bow, targeting=True, power=True, cost=2, targeting_message=Message(
        'Left-click a target tile for the bow, or right-click to cancel.', libtcod.light_cyan),
                          damage=0, radius=0)
    p = Entity(0, 0, '#', libtcod.red, 'Fireball Scroll', render_order=RenderOrder.ITEM,
                  item=power_item_component)
    magic_component.add_power(p)

    power_item_component = Item(use_function=cast_teleport, targeting=True, power=True, cost=10, targeting_message=Message(
        'Left-click a tile to teleport, or right-click to cancel.', libtcod.light_cyan))
    p = Entity(0, 0, '#', libtcod.green, 'Teleport Scroll', render_order=RenderOrder.ITEM,
                  item=power_item_component)
    magic_component.add_power(p)


    player = Entity(0, 0, '@', libtcod.white, 'Player', fluff='Player: This is you', blocks=True, render_order=RenderOrder.ACTOR,
                    fighter=fighter_component, inventory=inventory_component, level=level_component,
                    equipment=equipment_component, magic=magic_component)
    player.fighter.heal(100);
    player.fighter.heal_vim(100);
    entities = [player]

    dagger = item_dagger()
    player.inventory.add_item(dagger)
    player.equipment.toggle_equip(dagger)

    headlamp = item_headlamp()
    player.inventory.add_item(headlamp)
    player.equipment.toggle_equip(headlamp)

    game_map = GameMap(constants['map_width'], constants['map_height'])
    game_map.make_map(constants['max_rooms'], constants['room_min_size'], constants['room_max_size'],
                      constants['map_width'], constants['map_height'], player, entities)

    message_log = MessageLog(constants['message_x'], constants['message_width'], constants['message_height'])

    game_state = GameStates.PLAYERS_TURN

    return player, entities, game_map, message_log, game_state
