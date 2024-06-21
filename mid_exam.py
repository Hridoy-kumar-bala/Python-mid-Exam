
class Hall:
    def __init__(self):
        self.__show_list = []
        self.seats = {}

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_list.append(show)
        
        self.seats[id] = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]

        ]
    
    def book_seats(self, id, seat_list):
        if id in self.seats:
            seat_matrix = self.seats[id]
            
            for seat in seat_list:
                row, col = seat
                if 0 <= row < len(seat_matrix) and 0 <= col < len(seat_matrix[0]):
                    if seat_matrix[row][col] == 0:
                        seat_matrix[row][col] = 1
                        print(f'your seat row:{row} and cal : {col} is booked')
                    else:
                        print(f"Your seat row: {row} and col: {col} is already booked.")
                else:
                    print(f'seat at row {row} and cal: {col} is invalid')
        else:
            print(f'this id is not found.')
    def view_show_list(self):
        if self.__show_list:
            for show in self.__show_list:
                print(f"ID: {show[0]}, Movie Name: {show[1]}, Time: {show[2]}")
        else:
            print("No shows available.")
    def view_available_seats(self, id):
        if id in self.seats:
            seat_matrix = self.seats[id]
            for row in range(len(seat_matrix)):
                for col in range(len(seat_matrix[row])):
                    if seat_matrix[row][col] == 1:
                        seat_status = '1'
                    else:
                        seat_status = '0'
                    print(f"Seat [{row}, {col}]: {seat_status}\n")
            # print(f'seat position: {seat_matrix}\n')
            # for row in range(len(seat_matrix)):
                # for col in range(len(seat_matrix[row])):
            print(f" {seat_matrix}\n")
        else:
            print(f"Show with id {id} not found.")

hall = Hall()
hall.entry_show(1,'Puspa','10 am')
hall.entry_show(2,'Bahuboli','3 pm')
# print(hall.show_list)
seat_list = [(0, 1), (1, 2), (2, 3)]
hall.book_seats(1, seat_list)
# print(hall.seats)
while True:
    print("\n1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. Book ticket in a show")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        hall.view_show_list()
    elif choice == 2:
        show_id = int(input("Enter show ID: "))
        hall.view_available_seats(show_id)
    elif choice == 3:
        show_id = int(input("Enter show ID: "))
        user_input = input("Enter seats to book (e.g., 0,1 1,2 2,3): ")
        seat_list = [tuple(map(int, seat.split(','))) for seat in user_input.split()]
        hall.book_seats(show_id, seat_list)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")
