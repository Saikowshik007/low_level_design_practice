from parking_lot.SIze import Size
from parking_lot.Vehicle import Vehicle
import uuid

class Truck(Vehicle):
    def __init__(self):
        self.size = Size.LARGE
        self.id = uuid.uuid1()