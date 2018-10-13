class Item:
    def __init__(self, use_function=None, targeting=False, targeting_message=None, power=False, cost=0, game_map=None, **kwargs):
        self.use_function = use_function
        self.targeting = targeting
        self.targeting_message = targeting_message
        self.power = power
        self.cost = cost
        self.game_map = game_map
        self.function_kwargs = kwargs
