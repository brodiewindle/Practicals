from Prac_08.silver_service_taxi import SilverServiceTaxi
from Prac_08.taxi import Taxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    total_fare_price = 0
    taxis = [Taxi("Pruis", 100), SilverServiceTaxi("limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    current_taxi = None
    menu_input = input(">>> ").lower()
    while menu_input != "q":
        if menu_input == "c":
            print("Taxis available: ")
            print_taxis(taxis)
            valid_taxi_number = False
            while not valid_taxi_number:
                try:
                    taxi_choice = int(input("Choose Taxi: "))
                    if taxi_choice > len(taxis) - 1:
                        taxi_choice = int(input("Choose Taxi: "))
                    else:
                        valid_taxi_number = True
                except ValueError:
                    print("Invalid Number")
            print("Bill to date: ${:.2f}".format(total_fare_price))
            current_taxi = taxis[taxi_choice]
        elif menu_input == "d":
            if current_taxi is not None:
                current_taxi.start_fare()
                drive_distance = float(input("Drive how far? "))
                current_taxi.drive(drive_distance)
                trip_price = current_taxi.get_fare()
                print("Your {} trip cost you {}".format(current_taxi.name, current_taxi.get_fare()))
                total_fare_price += trip_price
        else:
            print("Invalid Option")
        print("Bill to date: ${:.2f}".format(total_fare_price))
        print(MENU)
        menu_input = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_fare_price))
    print_taxis("Taxis are now:")
    print_taxis(taxis)


def print_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()