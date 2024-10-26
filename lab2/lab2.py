import datetime

class Hotel:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.bookings = []

    def add_booking(self, customer, room, in_date, out_date):
        if self.is_room_available(room, in_date, out_date):
            new_booking = Booking(customer, room, in_date, out_date)
            self.bookings.append(new_booking)
            print(f"Booking successfully created for {customer.name}.")
            print('Booking details:\n', new_booking.get_booking_details())
        else:
            print(f"Booking failed: Room {room.number} is not available for the selected dates.")

    def remove_booking(self, customer, room, in_date, out_date):
        booking_to_remove = self.find_booking(customer, room, in_date, out_date)
        if booking_to_remove:
            self.bookings.remove(booking_to_remove)
            print(f"Booking for {customer.name} from {in_date} to {out_date} has been removed.")
        else:
            print(f"No booking found for {customer.name} in room {room.number} from {in_date} to {out_date}.")

    def is_room_available(self, room, in_date, out_date):
        for booking in self.bookings:
            if booking.room == room:
                if in_date < booking.out_date and out_date > booking.in_date:
                    return False
        return True

    def find_booking(self, customer, room, in_date, out_date):
        for booking in self.bookings:
            if booking.customer == customer and booking.room == room and booking.in_date == in_date and booking.out_date == out_date:
                return booking
        return None

    @staticmethod
    def calculate_total_price(in_date, out_date, room):
        return (out_date - in_date).days * room.price_per_night

class Booking:
    def __init__(self, customer, room, in_date, out_date):
        self.customer = customer
        self.room = room
        self.in_date = in_date
        self.out_date = out_date
        self.total_price = Hotel.calculate_total_price(in_date, out_date, room)

    def get_booking_details(self):
        details = f"Customer: {self.customer.name} {self.customer.surname}\nDate: {self.in_date} - {self.out_date}\nTotal price: {self.total_price}"
        return details


class Room:
    def __init__(self, number, price_per_night, beds_number):
        self.number = number
        self._price_per_night = price_per_night
        self.beds_number = beds_number

    @property
    def price_per_night(self):
        return self._price_per_night

    @price_per_night.setter
    def price_per_night(self, value):
        if value > 0:
            self._price_per_night = value
        else:
            raise ValueError("Price per night must be positive.")

    def get_room_details(self):
        details = f"Room {self.number}\nPrice: {self.price_per_night} per night\nNumber of beds: {self.beds_number}"
        return details

class DeluxeRoom(Room):
    def __init__(self, number, price_per_night, beds_number, features):
        super().__init__(number, price_per_night, beds_number)
        self.features = features

    def get_room_details(self):
        details = super().get_room_details()
        details += f"\nFeatures: {', '.join(self.features)}"
        return details

class ClassicRoom(Room):
    def __init__(self, number, price_per_night, beds_number):
        super().__init__(number, price_per_night, beds_number)

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_person_details(self):
        return f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}"

class Employee():
    def __init__(self, salary, experience):
        self._salary = salary
        self.experience = experience

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    def get_employee_details(self):
        return f"\nSalary: {self._salary}\nExperience: {self.experience} years"

class Receptionist(Person, Employee):
    def __init__(self, name, surname, age, salary, experience):
        Person.__init__(self, name, surname, age)
        Employee.__init__(self, salary, experience)

    def create_booking(self, hotel, customer, room, in_date, out_date):
        hotel.add_booking(customer, room, in_date, out_date)

    def cancel_booking(self, hotel, customer, room, in_date, out_date):
        hotel.remove_booking(customer, room, in_date, out_date)

    def get_details(self):
        return super().get_person_details() + super().get_employee_details()

class Housekeeper(Person, Employee):
    def __init__(self, name, surname, age, salary, experience):
        Person.__init__(self, name, surname, age)
        Employee.__init__(self, salary, experience)

    def clean_room(self, room):
        print(f"Housekeeper {self.name} {self.surname} is cleaning room {room.number}.")
        print(f"Room {room.number} has been cleaned and is ready for the next guest.")

    def get_details(self):
        return super().get_person_details() + super().get_employee_details()

class Customer(Person):
    def __init__(self, name, surname, age, email, phone):
        super().__init__(name, surname, age)
        self.email = email
        self.phone = phone

    def get_customer_details(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nPhone number: {self.phone}\nEmail: {self.email}\n"


if __name__ == "__main__":
    hotel = Hotel("Grand Hotel", "123 Main St")

    customer1 = Customer("John", "Doe", 30, "john@example.com", "123456789")
    customer2 = Customer("Jane", "Doe", 28, "jane@example.com", "987654321")

    print(customer1.get_customer_details())

    deluxe_room = DeluxeRoom(101, 2500, 2, ["Sea View", "Jacuzzi"])
    classic_room = ClassicRoom(102, 1800, 2)

    print(deluxe_room.get_room_details())
    print(classic_room.get_room_details())

    receptionist = Receptionist("Alice", "Smith", 25, 30000, 3)
    housekeeper = Housekeeper("Bob", "Brown", 40, 12500, 10)

    print(receptionist.get_details())
    print(housekeeper.get_details())

    print("---- Booking Process ----")
    receptionist.create_booking(hotel, customer1, deluxe_room, datetime.date(2024, 5, 16), datetime.date(2024, 5, 18))
    receptionist.create_booking(hotel, customer2, classic_room, datetime.date(2024, 5, 17), datetime.date(2024, 5, 20))

    classic_room.price_per_night = 1900
    print("\nUpdated Classic Room Price:")
    print(classic_room.get_room_details())

    receptionist.create_booking(hotel, customer2, classic_room, datetime.date(2024, 6, 17), datetime.date(2024, 6, 20))

    print("\n---- Room Cleaning Process ----")
    housekeeper.clean_room(deluxe_room)
    housekeeper.clean_room(classic_room)

    print("\n---- Cancel Booking Process ----")
    receptionist.cancel_booking(hotel, customer1, deluxe_room, datetime.date(2024, 5, 16), datetime.date(2024, 5, 18))

    print("\n---- Room Details ----")
    print(deluxe_room.get_room_details())
    print(classic_room.get_room_details())

    print("\n---- Customer Details ----")
    print(customer1.get_customer_details())
    print(customer2.get_customer_details())