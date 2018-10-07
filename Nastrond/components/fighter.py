import libtcodpy as libtcod

from game_messages import Message

class Fighter:
    def __init__(self, hp, defense, power, xp=0, knockback=0, strength=0, agility=0, toughness=0, intelligence=0, resolve=0, ego=0):
        self.base_max_hp = hp
        self.hp = hp
        self.base_defense = defense
        self.base_power = power
        self.base_knockback = knockback
        self.xp = xp
        self.base_strength = strength
        self.base_agility = agility
        self.base_toughness = toughness
        self.base_intelligence = intelligence
        self.base_resolve = resolve
        self.base_ego = ego

    @property
    def strength(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.strength_bonus
        else:
            bonus = 0

        return self.base_strength + bonus

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
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.max_hp_bonus
        else:
            bonus = 0

        return self.base_max_hp + bonus

    @property
    def power(self):
        if self.owner and self.owner.equipment:
            bonus = self.owner.equipment.power_bonus
        else:
            bonus = 0

        return self.base_power + bonus

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

    def resolve_attack(self, target):
        results = []

        damage = self.power - target.fighter.defense

        if damage > 0:
            results.append({'message': Message('{0} attacks {1} for {2} hit points.'.format(
                self.owner.name.capitalize(), target.name, str(damage)), libtcod.white)})
            results.extend(target.fighter.take_damage(damage))
        else:
            results.append({'message': Message('{0} attacks {1} but does no damage.'.format(
                self.owner.name.capitalize(), target.name), libtcod.white)})

        return results


    def knockback_qty(self, target):
        knockback = self.knockback - target.fighter.strength
        return knockback


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
        return results