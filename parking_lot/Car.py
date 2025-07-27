from parking_lot.Size import Size
from parking_lot.Vehicle import Vehicle
import uuid

class Car(Vehicle):
    def __init__(self):
        self.size = Size.MEDIUM
        self.id = uuid.uuid1()