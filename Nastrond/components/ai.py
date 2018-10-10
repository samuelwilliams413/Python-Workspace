import libtcodpy as libtcod

from random import randint

from game_messages import Message
from entity import get_blocking_entities_at_location
from components.effects import *


class BasicMonster:
    def take_turn(self, target, fov_map, game_map, entities):
        results = []

        monster = self.owner


        monster.hasSeen = monster.fighter.canSee(target)

        if libtcod.map_is_in_fov(fov_map, monster.x, monster.y) or monster.hasSeen:

            monster.hasSeen = True

            for x in range(0, monster.fighter.speed):
                if monster.distance_to(target) >= 2:
                    monster.move_astar(target, entities, game_map)

            for x in range(0, monster.fighter.AP):

                if monster.distance_to(target) >= 2:
                    monster.move_astar(target, entities, game_map)

                elif target.fighter.hp > 0:
                    knockback_results = monster.fighter.resolve_knockback(target, game_map, entities)
                    results.extend(knockback_results)
                    attack_results = monster.fighter.resolve_attack(target)
                    results.extend(attack_results)



        return results

class FastMonster:
    def take_turn(self, target, fov_map, game_map, entities):
        results = []

        monster = self.owner

        for x in range(0, monster.fighter.speed):
            if monster.distance_to(target) >= 2:
                monster.move_astar(target, entities, game_map)

        results = self.take_turn(target, fov_map, game_map, entities)

        return results


class ConfusedMonster:
    def __init__(self, previous_ai, number_of_turns=10):
        self.previous_ai = previous_ai
        self.number_of_turns = number_of_turns

    def take_turn(self, target, fov_map, game_map, entities):
        results = []

        if self.number_of_turns > 0:
            random_x = self.owner.x + randint(0, 2) - 1
            random_y = self.owner.y + randint(0, 2) - 1

            if random_x != self.owner.x and random_y != self.owner.y:
                self.owner.move_towards(random_x, random_y, game_map, entities)

            self.number_of_turns -= 1
        else:
            self.owner.ai = self.previous_ai
            results.append({'message': Message('The {0} is no longer confused!'.format(self.owner.name), libtcod.red)})

        return results
