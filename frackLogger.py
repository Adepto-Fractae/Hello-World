import serial

from twilio.rest import Client
client = Client("AC6931bca0100b52f39cdd1ebe26767a13", "0b9477263d4e8bc24bd01ff0c004ecf3")

counter = 0
detectNum = 1

portName = "COM6"
outputFileName = "output.txt"

outputFile = open(outputFileName, "a")

mySerial = serial.Serial(portName)
print(mySerial.name)

while(1):
    myInput = mySerial.readline()
    myString = str(myInput)[2:-3]
    #myString += "\n"
    #print(myString)
    print("------------------------")
    splitString = myString.split(",")
    print(splitString)
    print("water level: " + splitString[0])

    print("vibration: " + splitString[1])
    print("temperature: " + splitString[2])
    print("gas: " + splitString[3])
    print("voltage: " + splitString[4])
    fileOutput = str(myString + "\n")
    outputFile.write(fileOutput)
    counter += 1
    if( (int( splitString[1]) > 1000) and (int(counter) > 10) ):
        outputString = "earthquake number: " + str(detectNum) + " value: " + str(splitString[1]) + " methane level: " + splitString[4]
        client.messages.create(to="+17608556188", from_="+12563056329", body=outputString)
        counter = 0
        detectNum += 1


