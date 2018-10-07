from equipment_slots import EquipmentSlots


class Equipment:
    def __init__(self, main_hand=None, off_hand=None, head=None, neck=None, main_wrist=None, off_wrist=None, feet=None,
                 belt_pouch=None, belt_skin=None, belt_sheath=None, bandolier=None,):
        self.main_hand = main_hand
        self.off_hand = off_hand
        self.head = head
        self.neck = neck
        self.main_wrist = main_wrist
        self.off_wrist = off_wrist
        self.feet = feet
        self.belt_pouch = belt_pouch
        self.belt_skin = belt_skin
        self.belt_sheath = belt_sheath
        self.bandolier = bandolier

    @property
    def max_hp_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.max_hp_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.max_hp_bonus

        if self.head and self.head.equippable:
            bonus += self.head.equippable.max_hp_bonus

        if self.neck and self.neck.equippable:
            bonus += self.neck.equippable.max_hp_bonus

        if self.main_wrist and self.main_wrist.equippable:
            bonus += self.main_wrist.equippable.max_hp_bonus

        if self.off_wrist and self.off_wrist.equippable:
            bonus += self.off_wrist.equippable.max_hp_bonus

        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.max_hp_bonus

        if self.belt_pouch and self.belt_pouch.equippable:
            bonus += self.belt_pouch.equippable.max_hp_bonus

        if self.belt_skin and self.belt_skin.equippable:
            bonus += self.belt_skin.equippable.max_hp_bonus

        if self.belt_sheath and self.belt_sheath.equippable:
            bonus += self.belt_sheath.equippable.max_hp_bonus

        if self.bandolier and self.bandolier.equippable:
            bonus += self.bandolier.equippable.max_hp_bonus
        return bonus

    @property
    def power_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.power_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.power_bonus

        if self.head and self.head.equippable:
            bonus += self.head.equippable.power_bonus

        if self.neck and self.neck.equippable:
            bonus += self.neck.equippable.power_bonus

        if self.main_wrist and self.main_wrist.equippable:
            bonus += self.main_wrist.equippable.power_bonus

        if self.off_wrist and self.off_wrist.equippable:
            bonus += self.off_wrist.equippable.power_bonus

        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.power_bonus

        if self.belt_pouch and self.belt_pouch.equippable:
            bonus += self.belt_pouch.equippable.power_bonus

        if self.belt_skin and self.belt_skin.equippable:
            bonus += self.belt_skin.equippable.power_bonus

        if self.belt_sheath and self.belt_sheath.equippable:
            bonus += self.belt_sheath.equippable.power_bonus

        if self.bandolier and self.bandolier.equippable:
            bonus += self.bandolier.equippable.power_bonus

        return bonus

    @property
    def defense_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.defense_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.defense_bonus

        if self.head and self.head.equippable:
            bonus += self.head.equippable.defense_bonus

        if self.neck and self.neck.equippable:
            bonus += self.neck.equippable.defense_bonus

        if self.main_wrist and self.main_wrist.equippable:
            bonus += self.main_wrist.equippable.defense_bonus

        if self.off_wrist and self.off_wrist.equippable:
            bonus += self.off_wrist.equippable.defense_bonus

        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.defense_bonus

        if self.belt_pouch and self.belt_pouch.equippable:
            bonus += self.belt_pouch.equippable.defense_bonus

        if self.belt_skin and self.belt_skin.equippable:
            bonus += self.belt_skin.equippable.defense_bonus

        if self.belt_sheath and self.belt_sheath.equippable:
            bonus += self.belt_sheath.equippable.defense_bonus

        if self.bandolier and self.bandolier.equippable:
            bonus += self.bandolier.equippable.defense_bonus

        return bonus

    @property
    def strength_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.strength_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.strength_bonus

        if self.head and self.head.equippable:
            bonus += self.head.equippable.strength_bonus

        if self.neck and self.neck.equippable:
            bonus += self.neck.equippable.strength_bonus

        if self.main_wrist and self.main_wrist.equippable:
            bonus += self.main_wrist.equippable.strength_bonus

        if self.off_wrist and self.off_wrist.equippable:
            bonus += self.off_wrist.equippable.strength_bonus

        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.strength_bonus

        if self.belt_pouch and self.belt_pouch.equippable:
            bonus += self.belt_pouch.equippable.strength_bonus

        if self.belt_skin and self.belt_skin.equippable:
            bonus += self.belt_skin.equippable.strength_bonus

        if self.belt_sheath and self.belt_sheath.equippable:
            bonus += self.belt_sheath.equippable.strength_bonus

        if self.bandolier and self.bandolier.equippable:
            bonus += self.bandolier.equippable.strength_bonus

        return bonus
    
    @property
    def agility_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.agility_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.agility_bonus

        if self.head and self.head.equippable:
            bonus += self.head.equippable.agility_bonus

        if self.neck and self.neck.equippable:
            bonus += self.neck.equippable.agility_bonus

        if self.main_wrist and self.main_wrist.equippable:
            bonus += self.main_wrist.equippable.agility_bonus

        if self.off_wrist and self.off_wrist.equippable:
            bonus += self.off_wrist.equippable.agility_bonus

        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.agility_bonus

        if self.belt_pouch and self.belt_pouch.equippable:
            bonus += self.belt_pouch.equippable.agility_bonus

        if self.belt_skin and self.belt_skin.equippable:
            bonus += self.belt_skin.equippable.agility_bonus

        if self.belt_sheath and self.belt_sheath.equippable:
            bonus += self.belt_sheath.equippable.agility_bonus

        if self.bandolier and self.bandolier.equippable:
            bonus += self.bandolier.equippable.agility_bonus

        return bonus

    @property
    def toughness_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.toughness_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.toughness_bonus

        if self.head and self.head.equippable:
            bonus += self.head.equippable.toughness_bonus

        if self.neck and self.neck.equippable:
            bonus += self.neck.equippable.toughness_bonus

        if self.main_wrist and self.main_wrist.equippable:
            bonus += self.main_wrist.equippable.toughness_bonus

        if self.off_wrist and self.off_wrist.equippable:
            bonus += self.off_wrist.equippable.toughness_bonus

        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.toughness_bonus

        if self.belt_pouch and self.belt_pouch.equippable:
            bonus += self.belt_pouch.equippable.toughness_bonus

        if self.belt_skin and self.belt_skin.equippable:
            bonus += self.belt_skin.equippable.toughness_bonus

        if self.belt_sheath and self.belt_sheath.equippable:
            bonus += self.belt_sheath.equippable.toughness_bonus

        if self.bandolier and self.bandolier.equippable:
            bonus += self.bandolier.equippable.toughness_bonus

        return bonus

    @property
    def intelligence_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.intelligence_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.intelligence_bonus

        if self.head and self.head.equippable:
            bonus += self.head.equippable.intelligence_bonus

        if self.neck and self.neck.equippable:
            bonus += self.neck.equippable.intelligence_bonus

        if self.main_wrist and self.main_wrist.equippable:
            bonus += self.main_wrist.equippable.intelligence_bonus

        if self.off_wrist and self.off_wrist.equippable:
            bonus += self.off_wrist.equippable.intelligence_bonus

        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.intelligence_bonus

        if self.belt_pouch and self.belt_pouch.equippable:
            bonus += self.belt_pouch.equippable.intelligence_bonus

        if self.belt_skin and self.belt_skin.equippable:
            bonus += self.belt_skin.equippable.intelligence_bonus

        if self.belt_sheath and self.belt_sheath.equippable:
            bonus += self.belt_sheath.equippable.intelligence_bonus

        if self.bandolier and self.bandolier.equippable:
            bonus += self.bandolier.equippable.intelligence_bonus

        return bonus

    @property
    def resolve_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.resolve_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.resolve_bonus

        if self.head and self.head.equippable:
            bonus += self.head.equippable.resolve_bonus

        if self.neck and self.neck.equippable:
            bonus += self.neck.equippable.resolve_bonus

        if self.main_wrist and self.main_wrist.equippable:
            bonus += self.main_wrist.equippable.resolve_bonus

        if self.off_wrist and self.off_wrist.equippable:
            bonus += self.off_wrist.equippable.resolve_bonus

        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.resolve_bonus

        if self.belt_pouch and self.belt_pouch.equippable:
            bonus += self.belt_pouch.equippable.resolve_bonus

        if self.belt_skin and self.belt_skin.equippable:
            bonus += self.belt_skin.equippable.resolve_bonus

        if self.belt_sheath and self.belt_sheath.equippable:
            bonus += self.belt_sheath.equippable.resolve_bonus

        if self.bandolier and self.bandolier.equippable:
            bonus += self.bandolier.equippable.resolve_bonus

        return bonus

    @property
    def ego_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.ego_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.ego_bonus

        if self.head and self.head.equippable:
            bonus += self.head.equippable.ego_bonus

        if self.neck and self.neck.equippable:
            bonus += self.neck.equippable.ego_bonus

        if self.main_wrist and self.main_wrist.equippable:
            bonus += self.main_wrist.equippable.ego_bonus

        if self.off_wrist and self.off_wrist.equippable:
            bonus += self.off_wrist.equippable.ego_bonus

        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.ego_bonus

        if self.belt_pouch and self.belt_pouch.equippable:
            bonus += self.belt_pouch.equippable.ego_bonus

        if self.belt_skin and self.belt_skin.equippable:
            bonus += self.belt_skin.equippable.ego_bonus

        if self.belt_sheath and self.belt_sheath.equippable:
            bonus += self.belt_sheath.equippable.ego_bonus

        if self.bandolier and self.bandolier.equippable:
            bonus += self.bandolier.equippable.ego_bonus

        return bonus

    @property
    def knockback_bonus(self):
        bonus = 0

        if self.main_hand and self.main_hand.equippable:
            bonus += self.main_hand.equippable.knockback_bonus

        if self.off_hand and self.off_hand.equippable:
            bonus += self.off_hand.equippable.knockback_bonus

        if self.head and self.head.equippable:
            bonus += self.head.equippable.knockback_bonus

        if self.neck and self.neck.equippable:
            bonus += self.neck.equippable.knockback_bonus

        if self.main_wrist and self.main_wrist.equippable:
            bonus += self.main_wrist.equippable.knockback_bonus

        if self.off_wrist and self.off_wrist.equippable:
            bonus += self.off_wrist.equippable.knockback_bonus

        if self.feet and self.feet.equippable:
            bonus += self.feet.equippable.knockback_bonus

        if self.belt_pouch and self.belt_pouch.equippable:
            bonus += self.belt_pouch.equippable.knockback_bonus

        if self.belt_skin and self.belt_skin.equippable:
            bonus += self.belt_skin.equippable.knockback_bonus

        if self.belt_sheath and self.belt_sheath.equippable:
            bonus += self.belt_sheath.equippable.knockback_bonus

        if self.bandolier and self.bandolier.equippable:
            bonus += self.bandolier.equippable.knockback_bonus

        return bonus

    def toggle_equip(self, equippable_entity):
        results = []

        slot = equippable_entity.equippable.slot

        if slot == EquipmentSlots.MAIN_HAND:
            if self.main_hand == equippable_entity:
                self.main_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.main_hand:
                    results.append({'dequipped': self.main_hand})

                self.main_hand = equippable_entity
                results.append({'equipped': equippable_entity})
        elif slot == EquipmentSlots.OFF_HAND:
            if self.off_hand == equippable_entity:
                self.off_hand = None
                results.append({'dequipped': equippable_entity})
            else:
                if self.off_hand:
                    results.append({'dequipped': self.off_hand})

                self.off_hand = equippable_entity
                results.append({'equipped': equippable_entity})

        return results
