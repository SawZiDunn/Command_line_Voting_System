# Mini Voting Program
#### Video Demo:  <https://youtu.be/6k-v9e8s9C8?si=foCvGJ4vv_9Rig7t>
#### Description:
This is a command-line program in which you can vote different professional football players from
different countries. You need to register before logging in.
And if you're an admin, you can modify the data in csv file by adding and removing players, and
resetting all the votes to zero.

You can use the given username and password in order to log in as an admin to control the data in the CSV file.
ADMIN_USER_NAME = "Admin07"
ADMIN_PASSWORD = "Admin07"

The program contains 12 functions in total including main():
The program automatically sort the players in descending order by looking at the number of votes.
players.csv contains all the data related to the players, and users.csv contains data about the registered users.
test_players.csv is used just for the sake of test_project.py, and not related to the main program.

main() just calls for register() and log_in().
admin_option() and user_option() calls for other functions according to the user's input.
add_player(), remove_player(), and reset_data() are three main functions for the admin actions.
Meanwhile, vote() is the key function for the user action.


## Installation
Use pip to install the package tabulate
```
$ pip install tabulate
```

## Usage
Use python to run the program
```
$ python project.py
```

Use pytest to test the program
```
$ pytest test_project.py
```

## Contribution
You are welcome to suggest any change or alternative or improvements that I could have done differently.




