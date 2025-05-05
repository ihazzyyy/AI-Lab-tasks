from collections import deque
from ml_model import predict_fare
from ride_system import request_ride

class Node:
    def __init__(self, ride):
        self.ride = ride
        self.next = None

class RideHistory:
    def __init__(self):
        self.head = None

    def add_ride(self, ride):
        new_node = Node(ride)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next 
            temp.next = new_node

    def display(self):
        print('\nCompleted Ride History:')
        current = self.head
        count = 1
        while current is not None:
            ride = current.ride
            print(f"{count}. from {ride['from']} to {ride['to']} | Fare: ${ride['fare']:.2f}")
            current = current.next
            count += 1 
        if count == 1:
            print('No completed rides yet')

ride_queue = deque()
completed_ride = RideHistory()
ride_data = []

def book_ride():
    source = input('Enter source (A, B, C): ').upper()
    destination = input('Enter destination (A, B, C): ').upper()

    distance = request_ride(source, destination)
    fare = predict_fare(distance)

    ride = {
        'from': source,
        'to': destination,
        'fare': round(fare, 2)
    }

    ride_queue.append(ride)
    ride_data.append((source, destination, fare))
    print(f'Ride added to queue. Estimated fare: ${fare:.2f}\n')

def serve_ride():
    if not ride_queue:
        print('No rides to serve.\n')
        return
    ride = ride_queue.popleft() 
    completed_ride.add_ride(ride)
    print(f"🚕 Ride from {ride['from']} to {ride['to']} completed. Fare: ${ride['fare']:.2f}\n")

def main():
    while True:
        print("\n🚗 Ride Sharing Menu")
        print("1. Book a Ride")
        print("2. Serve Next Ride")
        print("3. View Completed Rides (Linked List)")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            book_ride()
        elif choice == '2':
            serve_ride()
        elif choice == '3':
            completed_ride.display()
        elif choice == '5':
            print("👋 Exiting. Thank you!")
            break
        else:
            print("❌ Invalid choice.\n")

if __name__ == "__main__":
    main()