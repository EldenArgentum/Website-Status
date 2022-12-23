import requests
from datetime import datetime

print("Hello! This program will check the status of a program and will log the status in a text file.")

usedProgram = str(input("Have you used this program before? (y/n)\t"))

while True:
    if usedProgram.lower() == "y":
        fileName = str(input("What is the name of the file you previously logged to?\t"))
        fileName = fileName + ".txt"
        f = open(fileName, 'a')
        break
    elif usedProgram.lower() == "n":
        fileName = str(input("What do you want to name the file that contains all of your logs?\t"))
        fileName = fileName + ".txt"
        f = open(fileName, 'w')
        break
    else:
        print("You can't bamboozle me! Yes or no? (Enter y for yes, n for no)")


url = str(input("Enter the URL you want to check the status of:\t"))


response = requests.get(url)


if response.status_code == 200:
    statusCode = "successful"
elif response.status_code == 404:
    statusCode = "not found; try to enter another url."
else:
    statusCode = "unsuccessful"

now = datetime.now()


f.write(f"At {now} you requested to check the status of {url}. The status was {statusCode}.\n\n")


print(f"Your request to {url} is {statusCode.upper()}.")

f.close()