#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

def movethemfiles(transportString,targetLocation):
    # Lab 12 - Customization Request 03 and 04
    # iterate across the files within directory


        # movethemfiles(sftp,inputLocation,inputDevice,inputUsername,inputPassword)

    for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
        if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
#            transportString.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location
            transportString.put("/home/student/filestocopy/"+x, targetLocation+x) # move file to target location
    return

def main():

    ## where to connect to
    #    t = paramiko.Transport("10.10.2.3", 22) ## IP and port

    notDoneFlag = "y" 

    while notDoneFlag == "y":
        ## Grab the Location where files should be placed
        inputLocation = input("Please enter the location to place files (target directory): ")
        inputDevice = input("Please enter the Machine Name: ")
        inputUsername = input("Please enter the Username of the device: ")
        inputPassword = input("Please enter the Password of the device: ")

        ## Make an sftp connection object
        sftp = paramiko.SFTPClient.from_transport(t)

        ## iterate across the files within directory
        movethemfiles(sftp,inputLocation,inputDevice,inputUsername,inputPassword)

        ## close the connection
        sftp.close() # close the connection 

        ## Prompt user to continue
        notDoneFlag = input("Would you like to continue (y/n): ")  

if __name__ == "__main__":
    main()

