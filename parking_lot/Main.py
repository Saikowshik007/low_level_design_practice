from parking_lot.ParkingLot import ParkingLot
from parking_lot.Vehicle import Vehicle


def main():
    spots = {"small": 10, "medium" : 5, "large" : 5}
    parking_lot = ParkingLot.get_instance(levels= 3, parking_spots=spots)
    v = Vehicle(size="small")
    parking_lot.add_vehicle(v)
    print(parking_lot.display_availability())

if __name__ == "__main__":
    main()