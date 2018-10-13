import libtcodpy as libtcod

from components.ai import ConfusedMonster

from entity import get_blocking_entities_at_location

from game_messages import Message


def heal(*args, **kwargs):
    player = args[0]
    amount = kwargs.get('amount')
    power = kwargs.get('power')
    cost = kwargs.get('cost')

    results = []

    if player.fighter.hp == player.fighter.max_hp:
        results.append({'consumed': False, 'message': Message('You are already at full health', libtcod.yellow)})
    else:
        player.fighter.heal(amount)
        results.append({'power_used': True})
        if power:
            results.append({'consumed': False, 'message': Message('Your wounds start to feel better!', libtcod.green)})

        else:
            results.append({'consumed': True, 'message': Message('Your wounds start to feel better!', libtcod.green)})
        results.extend(player.fighter.use_vim(cost))
        results.extend(player.fighter.take_damage(0))
    return results


def cast_lightning(*args, **kwargs):
    caster = args[0]
    entities = kwargs.get('entities')
    fov_map = kwargs.get('fov_map')
    damage = kwargs.get('damage')
    maximum_range = kwargs.get('maximum_range')

    results = []

    target = None
    closest_distance = maximum_range + 1

    for entity in entities:
        if entity.fighter and entity != caster and libtcod.map_is_in_fov(fov_map, entity.x, entity.y):
            distance = caster.distance_to(entity)

            if distance < closest_distance:
                target = entity
                closest_distance = distance

    if target:
        results.append({'consumed': True, 'target': target, 'message': Message('A lighting bolt strikes the {0} with a loud thunder! The damage is {1}'.format(target.name, damage))})
        results.extend(target.fighter.take_damage(damage))
    else:
        results.append({'consumed': False, 'target': None, 'message': Message('No enemy is close enough to strike.', libtcod.red)})

    return results


def cast_fireball(*args, **kwargs):
    entities = kwargs.get('entities')
    fov_map = kwargs.get('fov_map')
    damage = kwargs.get('damage')
    radius = kwargs.get('radius')
    target_x = kwargs.get('target_x')
    target_y = kwargs.get('target_y')

    results = []

    if not libtcod.map_is_in_fov(fov_map, target_x, target_y):
        results.append({'consumed': False, 'message': Message('You cannot target a tile outside your field of view.', libtcod.yellow)})
        return results


    results.append({'consumed': True, 'message': Message('The fireball explodes, burning everything within {0} tiles!'.format(radius), libtcod.orange)})

    for entity in entities:
        if entity.distance(target_x, target_y) <= radius and entity.fighter:
            results.append({'message': Message('The {0} gets burned for {1} hit points.'.format(entity.name, damage), libtcod.orange)})
            results.extend(entity.fighter.take_damage(damage))

    return results




def cast_bow(*args, **kwargs):

    entities = kwargs.get('entities')
    fov_map = kwargs.get('fov_map')
    damage = kwargs.get('damage')
    radius = kwargs.get('radius')
    target_x = kwargs.get('target_x')
    target_y = kwargs.get('target_y')
    power = kwargs.get('power')
    cost = kwargs.get('cost')

    results = []

    if not libtcod.map_is_in_fov(fov_map, target_x, target_y):
        results.append({'consumed': False, 'message': Message('You cannot target a tile outside your field of view.', libtcod.yellow)})
        return results

    results.append({'consumed': False})
    results.append({'power_used': True})

    player = entities[0]


    if player.fighter.ego > damage:
        damage = player.fighter.ego

    for entity in entities:
        if entity.distance(target_x, target_y) <= radius and entity.fighter:
            results.append({'message': Message('The {0} gets hit by an arrow for {1} hit points.'.format(entity.name, damage), libtcod.orange)})
            results.extend(entity.fighter.take_damage(damage))

    results.extend(player.fighter.use_vim(cost))
    results.extend(player.fighter.take_damage(0))
    return results

def cast_teleport(*args, **kwargs):

    entities = kwargs.get('entities')
    fov_map = kwargs.get('fov_map')
    target_x = kwargs.get('target_x')
    target_y = kwargs.get('target_y')
    game_map = kwargs.get('game_map')
    cost = kwargs.get('cost')

    results = []

    if not libtcod.map_is_in_fov(fov_map, target_x, target_y):
        results.append({'consumed': False, 'message': Message('You cannot target a tile outside your field of view.', libtcod.yellow)})
        return results

    results.append({'consumed': False})
    results.append({'power_used': True})

    player = entities[0]

    if game_map is None:
        results.append({'message': Message('The gamemap is NONE. [cast_teleport] ', libtcod.orange)})
        return results

    if not game_map.is_blocked(target_x, target_y):
        enemy = get_blocking_entities_at_location(entities, target_x, target_y)
        if not enemy:
            player.x = target_x
            player.y = target_y
            results.append({'message': Message(
                'The {0} teleports.'.format(player.name), libtcod.orange)})

    results.extend(player.fighter.use_vim(cost))
    results.extend(player.fighter.take_damage(0))
    return results

def cast_confuse(*args, **kwargs):
    entities = kwargs.get('entities')
    fov_map = kwargs.get('fov_map')
    target_x = kwargs.get('target_x')
    target_y = kwargs.get('target_y')

    results = []

    if not libtcod.map_is_in_fov(fov_map, target_x, target_y):
        results.append({'consumed': False, 'message': Message('You cannot target a tile outside your field of view.', libtcod.yellow)})
        return results

    for entity in entities:
        if entity.x == target_x and entity.y == target_y and entity.ai:
            confused_ai = ConfusedMonster(entity.ai, 10)

            confused_ai.owner = entity
            entity.ai = confused_ai

            results.append({'consumed': True, 'message': Message('The eyes of the {0} look vacant, as he starts to stumble around!'.format(entity.name), libtcod.light_green)})

            break
    else:
        results.append({'consumed': False, 'message': Message('There is no targetable enemy at that location.', libtcod.yellow)})

    return results
