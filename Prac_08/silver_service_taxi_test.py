
from Prac_08.silver_service_taxi import SilverServiceTaxi


new_ride = SilverServiceTaxi("Hummer", 100, 2)
new_ride.start_fare()
new_ride.drive(18)
new_ride.get_fare()
print(new_ride.__str__())
print(new_ride.get_fare())
