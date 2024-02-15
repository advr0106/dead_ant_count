from dead_ant_counter import dead_ant_count

while True:
    ants = input("Enter the ants string (q to exit): ")
    if ants == "q":
        break
    print(dead_ant_count(ants))