from parking_lot.SIze import Size
from parking_lot.Vehicle import Vehicle
import uuid

class MotorCycle(Vehicle):
    def __init__(self):
        self.size = Size.SMALL
        self.id = uuid.uuid1()