import libtcodpy as libtcod

from game_messages import Message


class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []


    def add_item(self, item):
        results = []

        if len(self.items) >= self.capacity:
            results.append({
                'item_added': None,
                'message': Message('You cannot carry any more, your inventory is full', libtcod.yellow)
            })
        else:
            results.append({
                'item_added': item,
                'message': Message('You pick up the {0}!'.format(item.name), libtcod.blue)
            })

            self.items.append(item)

        return results

    def use(self, item_entity, power=False, **kwargs):
        results = []

        item_component = item_entity.item
        cost = item_component.cost

        if item_component.use_function is None:
            equippable_component = item_entity.equippable

            if equippable_component:
                results.append({'equip': item_entity})
            else:
                results.append({'message': Message('The {0} cannot be used'.format(item_entity.name), libtcod.yellow)})
        else:
            if item_component.targeting and not (kwargs.get('target_x') or kwargs.get('target_y')):
                results.append({'targeting': item_entity})
            else:
                kwargs = {**item_component.function_kwargs, **kwargs}
                item_use_results = item_component.use_function(self.owner, power=power, cost=cost, **kwargs)

                if not power:
                    for item_use_result in item_use_results:
                        if item_use_result.get('consumed'):
                            self.remove_item(item_entity)

                results.extend(item_use_results)

        return results

    def view_fluff(self, item):
        results = []
        results.append({'item_fluff': True})
        results.append({'message': Message('{0}'.format(item.fluff), libtcod.light_blue)})
        return results

    def remove_item(self, item):
        self.items.remove(item)

    def drop_item(self, item):
        results = []

        if self.owner.equipment.main_hand == item or self.owner.equipment.off_hand == item \
                or self.owner.equipment.head == item or self.owner.equipment.neck == item \
                or self.owner.equipment.main_wrist == item or self.owner.equipment.off_hand == item \
                or self.owner.equipment.feet == item or self.owner.equipment.torso == item \
                or self.owner.equipment.back == item or self.owner.equipment.legs == item:
            self.owner.equipment.toggle_equip(item)

        item.x = self.owner.x
        item.y = self.owner.y

        self.remove_item(item)
        results.append({'item_dropped': item, 'message': Message('You dropped the {0}'.format(item.name),
                                                                 libtcod.yellow)})

        return results
