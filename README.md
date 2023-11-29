# Mini Voting Program
#### Video Demo:  <https://youtu.be/t2ii7lmt2rA>
#### Description

This is a command-line program in which you can vote different professional football players from
different countries. You need to register before logging in.
And if you're an admin, you can modify the data in csv file by adding and removing players, and
resetting all the votes to zero.

ADMIN_USER_NAME = "Admin07"
ADMIN_PASSWORD = "Admin07"

The program contains 12 functions in total including main():
The program automatically sort the players in descending order by looking at the number of votes.
players.csv contains all the data related to the players, and users.csv contains data about the registered users.
test_players.csv is used just for the sake of test_project.py, and not related to the main program.

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


    