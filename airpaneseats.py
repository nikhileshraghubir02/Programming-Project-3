First_Class_Seats = [1, 2, 3, 4, 5]
Emergency_Seats = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
First_Class_Fee = 50
seats_taken = {i: False for i in range(1, 21)}
def display_seats_in_plane():
    print("\nSeats (The symbol T means taken):")
    for i in range(1, 21):
        label = "T" if seats_taken[i] else str(i)
        if i in First_Class_Seats:
            label = f"[First:{label}]"
        elif i in Emergency_Seats:
            label = f"[Emergency:{label}]"
        else:
            label = f"[Regular:{label}]"
        print(label, end="  ")
        if i % 5 == 0:
            print()
    print()
def parse_seats(text):
    result = []
    parts = text.split(",")
    for part in parts:
        part = part.strip()
        if "-" in part:
            a, b = part.split("-")
            a, b = int(a), int(b)
            for s in range(a, b + 1):
                result.append(s)
        else:
            result.append(int(part))
    return result
def purchase_of_seat(seat_list):
    total_fee = 0
    for s in seat_list:
        if s < 1 or s > 20:
            print(f"This seat {s} is invalid.")
            continue
        if seats_taken[s]:
            print(f"This seat {s} is already taken.")
            continue
        if s in Emergency_Seats:
            ans = input("This is an emergency seat. Do you accept full responsibility in an emergency? (y/n): ")
            if ans.lower() != "y":
                print(f"The seat {s} was not purchased (safety was not accepted).")
                continue
        if s in First_Class_Seats:
            total_fee += First_Class_Fee
        seats_taken[s] = True
        print(f"Seat {s} has been purchased.")
    print(f"Total fees: ${total_fee}\n")
def main():
    print("Welcome to our seat selection system! Please choose a seat.")
    while True:
        display_seats_in_plane()
        choice = input("Enter seat numbers (e.g. 1,3 or 6-8) or Q to quit: ")
        if choice.lower() == "q":
            print("Have a good day!")
            break
        try:
            seat_list = parse_seats(choice)
        except (ValueError, IndexError):
            print("That was an invalid entry.\n")
            continue
        purchase_of_seat(seat_list)
if __name__ == "__main__":
    main()