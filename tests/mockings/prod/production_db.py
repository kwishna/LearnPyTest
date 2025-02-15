class ProductionDB:
    admin = True

    def get_car_price(self, name):
        PRICES = {
            'buggatti': 1000,
            'audi': 500,
            'maruti': 100,
        }
        return PRICES[name]

    def method(self, *args, **kwargs):
        print(args)
        print(kwargs)

def get_cars():
    return ['audi', 'buggatti', 'maruti']