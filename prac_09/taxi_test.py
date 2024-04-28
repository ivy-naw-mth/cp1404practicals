from prac_09.taxi import Taxi

# 1. Create a new taxi object, my_taxi, with name "Prius 1", 100 units of fuel and price of $1.23
my_taxi = Taxi("Prius 1", 100)

# 2. Drive the taxi 40 km
my_taxi.drive(40)

# 3. Print the taxi's details and the current fare
print("Taxi details:")
print(my_taxi)
print(my_taxi.get_fare())

# 4. Restart the meter (start a new fare) and then drive the car 100 km
my_taxi.start_fare()
my_taxi.drive(100)

# 5. Print the details and the current fare
print("Taxi details after restarting the fare:")
print(my_taxi)
print("Current fare:", my_taxi.get_fare())

# Whole Program
# from prac_09.taxi import Taxi
# def main():
#     my_taxi = Taxi("Prius 1", 100)
#     my_taxi.drive(40)
#     print("Taxi details:")
#     print(my_taxi)
#     print(my_taxi.get_fare())
#     my_taxi.start_fare()
#     my_taxi.drive(100)
#     print("Taxi details after restarting the fare:")
#     print(my_taxi)
#     print("Current fare:", my_taxi.get_fare())
# main()



