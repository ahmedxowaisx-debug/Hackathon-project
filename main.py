# Smart Bus Ticket Booking System - Basic Version

buses = [
    {"id": 1, "from": "Karachi", "to": "Lahore", "fare": 3000, "seats": 10},
    {"id": 2, "from": "Karachi", "to": "Hyderabad", "fare": 800, "seats": 10},
    {"id": 3, "from": "Lahore", "to": "Islamabad", "fare": 1500, "seats": 10}
]
bookings = []

def show_buses():
    print("\nAvailable Buses")
    for bus in buses:
        print("ID:", bus["id"], "|", bus["from"], "to", bus["to"],
              "| Fare: Rs.", bus["fare"], "| Seats:", bus["seats"])

def book_ticket():
    show_buses()
    bus_id = int(input("Enter Bus ID: "))
    selected_bus = None

    for bus in buses:
        if bus["id"] == bus_id:
            selected_bus = bus

    if selected_bus is None:
        print("Bus not found.")
        return
    if selected_bus["seats"] == 0:
        print("No seats available.")
        return

    name = input("Enter passenger name: ")
    age = int(input("Enter passenger age: "))
    selected_bus["seats"] = selected_bus["seats"] - 1

    booking = {"name": name, "age": age,
               "bus_id": bus_id, "fare": selected_bus["fare"]}
    bookings.append(booking)
    print("Ticket booked successfully!")
    print("Passenger:", name, "| Age:", age, "| Fare: Rs.", selected_bus["fare"])

def show_bookings():
    print("\nBookings")
    if len(bookings) == 0:
        print("No bookings yet.")
    else:
        for booking in bookings:
            print("Name:", booking["name"], "| Age:", booking["age"],
                  "| Bus ID:", booking["bus_id"], "| Fare: Rs.", booking["fare"])

def main():
    while True:
        print("\n--- SMART BUS BOOKING ---")
        print("1. Show buses")
        print("2. Book ticket")
        print("3. Show bookings")
        print("0. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            show_buses()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            show_bookings()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

main()
