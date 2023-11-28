from tabulate import tabulate
import sys
import csv

ADMIN_USER_NAME = "Admin07"
ADMIN_PASSWORD = "Admin07"


def main():
    try:
        option = eval(input("\nPress 1 to Register\nPress 2 to Log In\nPress 3 to Exit"))
        if option == 1:
            register()
        elif option == 2:
            log_in()
        elif option == 3:
            sys.exit()
        else:
            raise SyntaxError
    except (SyntaxError, ValueError, NameError):
        print("Invalid Option!")
        main()


def register():
    users: list = read_data("users.csv")

    username = input("Username: ")
    password = input("Password: ")
    confirmation = input("Confirm Password: ")
    if password != confirmation:
        print("Password does not match!")
        main()
    # list comprehension
    elif username.lower() in [user["username"].lower() for user in users]:
        print("Username already exits!")
        main()

    try:
        with open("users.csv", "a", newline="\n") as file:
            writer = csv.DictWriter(file, fieldnames=["username", "password"])
            writer.writerow({"username": username, "password": password})
            print("Registration Complete!")
            main()

    except FileNotFoundError:
        sys.exit("File is not found!")


def log_in():
    users: list = read_data("users.csv")
    players: list = read_data("players.csv")

    username = input("Username: ")
    password = input("Password: ")

    if username == ADMIN_USER_NAME and password == ADMIN_PASSWORD:
        admin_option(players)

    for user in users:
        if user["username"] == username and user["password"] == password:
            user_option(players)
    print("You are not registered!")
    main()


def admin_option(players):
    while True:
        try:
            option = eval(
                input("\nPress 1 to view player list\nPress 2 to add players\nPress 3 to remove players\nPress 4 to "
                      "Reset All Data\nPress 5 to Exit"))

            if option == 1:
                view_players(players)
            elif option == 2:
                add_player(players)
            elif option == 3:
                remove_player(players)
            elif option == 4:
                if input("Are you sure you want to reset all the data? (Y/N)").lower().startswith("y"):
                    reset_data(players)
            elif option == 5:
                if input("Do you want to save your data?(y/n): ").lower().startswith("y"):
                    save_data("players.csv", players)

                sys.exit("Thanks for using our Voting System!\n")
            else:
                raise NameError
        except (ValueError, NameError, SyntaxError):
            print("Invalid Option!\nPlease try again!\n")


def add_player(players):
    last_name = input("Player Last Name: ")
    first_name = input("Player First Name: ")
    country = input("Country:")
    players.append({"Last Name": last_name, "First Name": first_name, "Country": country, "Vote": "0"})
    print(f"\nYou have successfully added {last_name} {first_name} to the Player List!\n")
    view_players(players)


def remove_player(players):
    try:
        option = eval(input("Who do you want to remove? (Choose by No."))
        del players[option - 1]

        print("============================")
        print("You have removed a player from the list!\n")
        return
    except (ValueError, NameError, SyntaxError, IndentationError):
        print("Invalid Choice!\nPlease try again!")


def user_option(players):
    while True:
        try:
            option = eval(input("\nPress 1 to view players\nPress 2 to Vote\nPress 3 to exit\n"))

            if option == 1:
                # if we change the array inside a function, that will also change the original array
                # since we are passing the reference of the original array.

                # even if we make new_list = original_list,
                # changes to new_list will still affect the original_list
                view_players(players)

            elif option == 2:
                vote(players)
            elif option == 3:
                if input("Do you want to save your data?(y/n): ").lower().startswith("y"):
                    save_data("players.csv", players)

                sys.exit("Thanks for using our Voting System!\n")

            else:
                raise ValueError

        except (ValueError, NameError, SyntaxError):
            print("Invalid Option!\nPlease try again!\n")
            user_option(players)


def read_data(file_name):
    try:
        with open(file_name) as file:
            reader = csv.DictReader(file)
            dic_array: list = [row for row in reader]

            # for row in reader:
            #     dic_array.append({"Last Name": row["Last Name"], "First Name": row["First Name"],
            #                       "Country": row["Country"], "Vote": int(row["Vote"])})

            return dic_array
    except FileNotFoundError:
        sys.exit("File is not found!")


def view_players(players):
    players.sort(key=lambda player: int(player["Vote"]), reverse=True)
    players = players.copy()

    for i in range(len(players)):
        new_dic = {"No": i + 1}
        new_dic.update(players[i])  # update() methods changes the original, does not return a new one
        players[i] = new_dic

    print(tabulate(players, headers="keys", tablefmt="rounded_outline"))
    print()


def vote(dic_array):
    while True:
        choice = eval(input("Who do you want to vote?\n(Choose by No...)\n"))
        votes = eval(input("How many votes?\n"))

        for i in range(len(dic_array)):
            if choice == i + 1:

                dic_array[i]["Vote"] = int(dic_array[i]["Vote"]) + votes
                print("============================\n")
                print(f"You have successfully voted {dic_array[i]['Last Name']} {dic_array[i]['First Name']}.\n")
                print("============================")
                view_players(dic_array)
                return dic_array
        print("Invalid Choice!\nPlease try again!")


def save_data(file_name, dic_array):
    try:
        with open(file_name, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=list(dic_array[0]))
            writer.writeheader()
            writer.writerows(dic_array)

            # for dic in dic_array:
            #     # dict comprehension
            #     # making sure that we're not saving "No" key's values in the csv file
            #     writer.writerow({key: value for key, value in dic.items() if key != "No"})
    except FileNotFoundError:
        sys.exit("File is not found!")


def reset_data(dic_array):

    for dic in dic_array:
        dic["Vote"] = 0
    print("============================\n")
    print("All votes have been reset to Zero.\n")
    print("============================")
    dic_array.sort(key=lambda player: player["First Name"])
    return


if __name__ == "__main__":
    main()
