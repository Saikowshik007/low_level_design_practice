from collections import  defaultdict
from threading import Lock, RLock
import time

from parking_lot.ParkingSpot import ParkingSpot


class ParkingLot:
    instance = None
    levels = None
    lock = Lock()
    def __init__(self, levels, spots):
        self.levels = []
        self.lock = RLock()
        for level in range(levels):
            parking_spots =defaultdict(list)
            for i,j in spots.items():
                parking_spots[i] = [ParkingSpot(size=i) for _ in range(j) if (True, time.sleep(0.0001))[0]]
            self.levels.append(parking_spots)

    @staticmethod
    def get_instance(levels, parking_spots):
        with ParkingLot.lock:
            if ParkingLot.instance is None:
                ParkingLot.instance = ParkingLot(levels, parking_spots)
                return ParkingLot.instance
        return ParkingLot.instance


    def add_vehicle(self, vehicle):
        with self.lock:
            spot = self.find_available_spots(vehicle.size)
            if spot is None or vehicle is None:
                return False
            spot.add_vehicle(vehicle)
            vehicle.parking_spot = spot
            return True

    def remove_vehicle(self, vehicle):
        with self.lock:
            if vehicle is None:
                return False
            vehicle.parking_spot.remove_vehicle()
            vehicle.parking_spot = None
            return True
    def find_available_spots(self, size):
        with self.lock:
            available_sizes = self.get_available_sizes(size)
            for size in available_sizes:
                for level in self.levels:
                    for i in level[size]:
                        if not i.is_occupied:
                            return i
        return None

    def get_available_sizes(self, size):
        size_hierarchy = {"small" : ["small", "medium", "large"], "medium" : ["medium", "large"], "large" : ["large"]}
        if size not in size_hierarchy:
            raise ValueError("size should be of small, medium, large")
        return size_hierarchy[size]

    def display_availability(self):
        with self.lock:
            for level_idx, level in enumerate(self.levels):
                for size, spots in level.items():
                    for spot in spots:
                        status = "Available" if not spot.is_occupied else "Occupied"
                        print(f"Level {level_idx}, Spot {spot.id}, Size {size}: {status}")







