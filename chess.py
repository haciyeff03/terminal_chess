
def is_valid_position(position): 
   # Check if the given position is valid on the chessboard.
    return len(position) == 2 and 'A' <= position[0] <= 'H' and '1' <= position[1] <= '8'

def is_valid_move(start, wanted):
  
   # Check if the queen move from the start position to the wanted position is valid.
   
    # Check if both start and wanted positions are valid
    if not is_valid_position(start) or not is_valid_position(wanted):
        return False
    
    # Check if the move is horizontal, vertical, or diagonal
    delta_x = abs(ord(start[0]) - ord(wanted[0]))
    delta_y = abs(int(start[1]) - int(wanted[1]))

    return delta_x == delta_y or start[0] == wanted[0] or start[1] == wanted[1]


def main():
    # Step 1: Get start position input from the user
    start_position = input("Enter the start position of the queen (e.g., B2): ")

    # Step 2: Get wanted position input from the user
    wanted_position = input("Enter the wanted position for the queen (e.g., C3): ")

    # Step 3: Check if the move is possible and print the result
    if is_valid_move(start_position.upper(), wanted_position.upper()):
        print("Yes")
    else:
        print("Not")


if __name__ == "__main__":
    main()
