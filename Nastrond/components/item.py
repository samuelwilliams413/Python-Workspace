class Item:
    def __init__(self, use_function=None, targeting=False, targeting_message=None, power=False, cost=0, **kwargs):
        self.use_function = use_function
        self.targeting = targeting
        self.targeting_message = targeting_message
        self.power = power
        self.cost = cost
        self.function_kwargs = kwargs
