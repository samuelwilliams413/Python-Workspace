import libtcodpy as libtcod
from random import randint

from components.ai import *
from components.equipment import EquipmentSlots
from components.equippable import Equippable
from components.fighter import Fighter
from components.item import Item
from components.stairs import Stairs
from components.weapon_rack import *
from components.beastiary import *
from components.backpack import *

from entity import Entity

from game_messages import Message

from rarity import Rarity

from item_functions import cast_confuse, cast_fireball, cast_lightning, heal

from map_objects.rectangle import Rect
from map_objects.tile import Tile

from random_utils import from_dungeon_level, random_choice_from_dict

from render_functions import RenderOrder


class GameMap:
    def __init__(self, width, height, dungeon_level=1):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

        self.dungeon_level = dungeon_level

    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]

        return tiles

    def make_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height, player, entities):
        rooms = []
        num_rooms = 0

        center_of_last_room_x = None
        center_of_last_room_y = None

        for r in range(max_rooms):
            # random width and height
            w = randint(room_min_size, room_max_size)
            h = randint(room_min_size, room_max_size)
            # random position without going out of the boundaries of the map
            x = randint(0, map_width - w - 1)
            y = randint(0, map_height - h - 1)

            # "Rect" class makes rectangles easier to work with
            new_room = Rect(x, y, w, h)

            # run through the other rooms and see if they intersect with this one
            for other_room in rooms:
                if new_room.intersect(other_room):
                    break
            else:
                # this means there are no intersections, so this room is valid

                # "paint" it to the map's tiles
                self.create_room(new_room)

                # center coordinates of new room, will be useful later
                (new_x, new_y) = new_room.center()

                center_of_last_room_x = new_x
                center_of_last_room_y = new_y

                if num_rooms == 0:
                    # this is the first room, where the player starts at
                    player.x = new_x
                    player.y = new_y
                else:
                    # all rooms after the first:
                    # connect it to the previous room with a tunnel

                    # center coordinates of previous room
                    (prev_x, prev_y) = rooms[num_rooms - 1].center()

                    # flip a coin (random number that is either 0 or 1)
                    if randint(0, 1) == 1:
                        # first move horizontally, then vertically
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                        # first move vertically, then horizontally
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)

                self.place_entities(new_room, entities)

                # finally, append the new room to the list
                rooms.append(new_room)
                num_rooms += 1
        stairs_component = Stairs(self.dungeon_level + 1)
        down_stairs = Entity(center_of_last_room_x, center_of_last_room_y, '>', libtcod.white, 'Stairs',
                             render_order=RenderOrder.STAIRS, stairs=stairs_component)
        entities.append(down_stairs)

    def create_room(self, room):
        # go through the tiles in the rectangle and make them passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].block_sight = False

    def place_entities(self, room, entities):
        max_monsters_per_room = from_dungeon_level([[2, 1], [3, 4], [5, 6]], self.dungeon_level)
        max_items_per_room = from_dungeon_level([[1, 1], [2, 4]], self.dungeon_level)

        # Get a random number of monsters
        number_of_monsters = randint(0, max_monsters_per_room)

        # Get a random number of items
        number_of_items = randint(0, max_items_per_room)

        monster_chances = {
            'imp': int(Rarity.COMMON),
            'wraith': from_dungeon_level([[int(Rarity.UNCOMMON), 0], [int(Rarity.COMMON), 3]], self.dungeon_level),
            'cultist': from_dungeon_level([[int(Rarity.COMMON), 0], [int(Rarity.UNCOMMON), 2], [int(Rarity.SCARCE), 4]], self.dungeon_level),
            'oni': from_dungeon_level([[0, 0], [int(Rarity.SCARCE), 3], [int(Rarity.UNCOMMON), 5], [int(Rarity.COMMON), 7]], self.dungeon_level)
        }

        item_chances = {
            'healing_potion': int(Rarity.ABUNDANT),
            'mace': int(Rarity.UNCOMMON),
            'torch': int(Rarity.COMMON),
            'sword': from_dungeon_level([[int(Rarity.UNCOMMON), 4]], self.dungeon_level),
            'shield': from_dungeon_level([[int(Rarity.UNCOMMON), 8]], self.dungeon_level),
            'lightning_scroll': from_dungeon_level([[int(Rarity.COMMON), 4]], self.dungeon_level),
            'fireball_scroll': from_dungeon_level([[int(Rarity.COMMON), 6]], self.dungeon_level),
            'confusion_scroll': from_dungeon_level([[int(Rarity.COMMON), 2]], self.dungeon_level)
        }

        for i in range(number_of_monsters):
            # Choose a random location in the room
            x = randint(room.x1 + 1, room.x2 - 1)
            y = randint(room.y1 + 1, room.y2 - 1)

            # Check if an entity is already in that location
            if not any([entity for entity in entities if entity.x == x and entity.y == y]):
                monster_choice = random_choice_from_dict(monster_chances)

                monster = beast_cultist(x, y)
                if monster_choice == 'cultist':
                    monster = beast_cultist(x,y)

                elif monster_choice == 'imp':
                    monster = beast_imp(x,y)
                    for i in range(0,randint(1,3)):
                        entities.append(monster)
                        # Choose a random location in the room
                        while(any([entity for entity in entities if entity.x == x and entity.y == y])):
                            x = randint(room.x1 + 1, room.x2 - 1)
                            y = randint(room.y1 + 1, room.y2 - 1)
                        monster = beast_imp(x,y)

                elif monster_choice == 'wraith':
                    monster = beast_wraith(x,y)

                elif monster_choice == 'oni':
                    monster = beast_oni(x,y)


                entities.append(monster)

        for i in range(number_of_items):
            x = randint(room.x1 + 1, room.x2 - 1)
            y = randint(room.y1 + 1, room.y2 - 1)

            if not any([entity for entity in entities if entity.x == x and entity.y == y]):
                item_choice = random_choice_from_dict(item_chances)

                if item_choice == 'healing_potion':
                    item_component = Item(use_function=heal, amount=40)
                    item = Entity(x, y, '!', libtcod.violet, 'Healing Potion', render_order=RenderOrder.ITEM,
                                  item=item_component)
                elif item_choice == 'mace':
                    item = item_mace(x, y)
                elif item_choice == 'sword':
                    item = item_sword(x, y)
                elif item_choice == 'torch':
                    item = item_torch(x, y)
                elif item_choice == 'shield':
                    item = item_shield(x, y)
                elif item_choice == 'fireball_scroll':
                    item = item_scroll_fireball(x,y)
                elif item_choice == 'confusion_scroll':
                    item = item_scroll_confusion(x,y)
                else:
                    item = item_scroll_lightning(x,y)

                entities.append(item)

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False

    def next_floor(self, player, message_log, constants):
        self.dungeon_level += 1
        entities = [player]

        self.tiles = self.initialize_tiles()
        self.make_map(constants['max_rooms'], constants['room_min_size'], constants['room_max_size'],
                      constants['map_width'], constants['map_height'], player, entities)

        player.fighter.heal(player.fighter.max_hp // 2)
        player.fighter.heal_vim(player.fighter.vim // 2)

        message_log.add_message(Message('You take a moment to rest, and recover your strength.', libtcod.light_violet))

        return entities