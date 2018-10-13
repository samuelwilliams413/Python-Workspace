import libtcodpy as libtcod

from math import exp
from game_messages import Message

class Fighter:
    def __init__(self, hp, defense, power, action_points=1, xp=0, vim=0, knockback=0, strength=0, agility=0, toughness=0, intelligence=0,
                 resolve=0, ego=0, field_of_vision=1, speed=0):
        self.base_max_hp = hp
        self.hp = hp
        self.base_max_vim = vim
        self.vim = vim // 2
        self.base_defense = defense
        self.base_power = power
        self.action_points = action_points
        self.base_knockback = knockback
        self.xp = xp
        self.base_strength = strength
        self.base_speed = speed
        self.base_agility = agility
        self.base_toughness = toughness
        self.base_intelligence = intelligence
        self.base_resolve = resolve
        self.base_ego = ego
        self.base_field_of_vision = field_of_vision
        self.overload = 0

    @property
    def max_vim(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_vim_bonus
        else:
            bonus = 0

        return self.base_max_vim + self.intelligence*self.owner.level.current_level + bonus

    @property
    def AP(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.action_points_bonus
        else:
            bonus = 0

        return self.action_points + bonus

    @property
    def strength(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.strength_bonus
        else:
            bonus = 0

        return self.base_strength + bonus

    @property
    def field_of_vision(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.field_of_vision_bonus
        else:
            bonus = 0

        return self.base_field_of_vision + bonus

    @property
    def agility(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.agility_bonus
        else:
            bonus = 0

        return self.base_agility + bonus

    @property
    def toughness(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.toughness_bonus
        else:
            bonus = 0

        return self.base_toughness + bonus

    @property
    def intelligence(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.intelligence_bonus
        else:
            bonus = 0

        return self.base_intelligence + bonus

    @property
    def resolve(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.resolve_bonus
        else:
            bonus = 0

        return self.base_resolve + bonus

    @property
    def ego(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.ego_bonus
        else:
            bonus = 0

        return self.base_ego + bonus

    @property
    def max_hp(self):
        if self.hp > (self.real_max_hp - self.overload):
            self.hp = self.real_max_hp - self.overload
        return self.real_max_hp - self.overload

    @property
    def real_max_hp(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_hp_bonus
        else:
            bonus = 0

        return self.base_max_hp + self.toughness*self.owner.level.current_level + bonus

    @property
    def power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.power_bonus
        else:
            bonus = 0

        return self.base_power + self.strength + bonus

    @property
    def defense(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.defense_bonus
        else:
            bonus = 0

        return self.base_defense + bonus

    @property
    def knockback(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.knockback_bonus
        else:
            bonus = 0

        return self.base_knockback + bonus

    @property
    def speed(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.speed_bonus
        else:
            bonus = 0

        return self.base_speed + bonus

    def take_damage(self, amount):
        results = []

        self.hp -= amount

        if self.hp <= 0:
            results.append({'dead': self.owner, 'xp': self.xp})

        return results

    def heal(self, amount):
        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def use_vim(self, amount):
        results = []
        self.vim += amount

        if self.vim > self.max_vim:
            overload = self.vim - self.max_vim
            self.overload += overload
            self.vim = self.max_vim
            results.append({'message': Message('{0} gained {1} corruption.'.format(
                    self.owner.name.capitalize(), overload), libtcod.red)})
        return results

    def heal_vim(self, amount):
        self.vim -= amount

        if self.vim < 0:
            self.vim = 0

    def regen_vim(self, turn):
        turn = (turn + 1) % 2
        if turn % 2 == 0:
            regen = (exp(self.resolve) ** -0.052)
            self.vim = int(self.vim * regen - 1);
            if self.vim < 0:
                self.vim = 0
        return turn


    def resolve_attack(self, target):
        results = []

        defense = target.fighter.defense - self.agility
        if defense < 0:
            defense = 0

        defense = (exp(defense) ** -0.1)

        damage = int(self.power * defense)

        if damage > 0:
            results.append({'message': Message('{0} attacks {1} for {2} hit points.'.format(
                self.owner.name.capitalize(), target.name, str(damage)), libtcod.white)})
            results.extend(target.fighter.take_damage(damage))
        else:
            results.append({'message': Message('{0} attacks {1} but does no damage.'.format(
                self.owner.name.capitalize(), target.name), libtcod.white)})

        return results


    def knockback_qty(self, target):
        knockback = 0
        if self.knockback > 0:
            knockback = self.knockback + self.strength - target.fighter.strength
        return knockback


    def canSee(self, target):
        if self.field_of_vision >= self.owner.distance_to(target):
            return True
        return False


    def resolve_knockback(self, target, game_map, entities):
        results = []
        actual_distance = 0
        knockback_results = self.knockback_qty(target)
        if (knockback_results > 0):
            while (knockback_results > 0):
                dx, dy = self.owner.move_direction(target, target.x, target.y, game_map, entities)
                knockback_results = knockback_results - 1
                actual_distance = actual_distance + 1
                target.move(dx, dy)
                if (dx == 0 and dy == 0):
                    knockback_results = 0;
        if actual_distance > 0:
            results.append({'message': Message('{0} knocks back {1} {2} paces.'.format(
                self.owner.name.capitalize(), target.name, str(actual_distance)), libtcod.white)})
        elif self.knockback > 0:
            results.append({'message': Message('{0} tries to knock back {1}, {1} stands strong!'.format(
                self.owner.name.capitalize(), target.name), libtcod.white)})
        return results