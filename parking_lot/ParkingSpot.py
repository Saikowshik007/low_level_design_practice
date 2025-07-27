import uuid
from threading import Lock
class ParkingSpot:
    size = None
    is_occupied= False
    vehicle = None
    id = None
    lock = None
    def __init__(self, size):
        self.size = size
        self.id = uuid.uuid1()
        self.lock=Lock()

    def add_vehicle(self, vehicle):
        with self.lock:
            self.is_occupied = True
            self.vehicle = vehicle
    def remove_vehicle(self):
        with self.lock:
            self.vehicle = None
            self.is_occupied= False
