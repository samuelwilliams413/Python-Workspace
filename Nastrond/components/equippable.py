class Equippable:
    def __init__(self, slot, power_bonus=0, defense_bonus=0, max_hp_bonus=0, strength_bonus=0, agility_bonus=0,
                 toughness_bonus=0, intelligence_bonus=0, resolve_bonus=0, ego_bonus=0, knockback_bonus=0,
                 field_of_vision_bonus=0, vim_bonus=0, max_vim_bonus=0, action_points_bonus=0, speed_bonus=0):
        self.slot = slot
        self.power_bonus = power_bonus
        self.defense_bonus = defense_bonus
        self.max_hp_bonus = max_hp_bonus
        self.strength_bonus = strength_bonus
        self.agility_bonus = agility_bonus
        self.toughness_bonus = toughness_bonus
        self.intelligence_bonus = intelligence_bonus
        self.resolve_bonus = resolve_bonus
        self.ego_bonus = ego_bonus
        self.knockback_bonus = knockback_bonus
        self.field_of_vision_bonus = field_of_vision_bonus
        self.vim_bonus = vim_bonus
        self.max_vim_bonus = max_vim_bonus
        self.action_points_bonus = action_points_bonus
        self.speed_bonus = speed_bonus
