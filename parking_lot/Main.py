from parking_lot.Car import Car
from parking_lot.ParkingLot import ParkingLot
from parking_lot.Size import Size


def main():
    spots = {Size.SMALL: 10, Size.MEDIUM : 5, Size.LARGE : 5}
    parking_lot = ParkingLot.get_instance(levels= 3, parking_spots=spots)
    v = Car()
    parking_lot.add_vehicle(v)
    print(parking_lot.display_availability())

if __name__ == "__main__":
    main()