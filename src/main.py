"Program to take a youtube channel URL and return the RSS feed link for the channel."

import sys
import conv as cv

def print_help():
    "Prints help menu"
    print(open("help.txt", "r").read())

def main():
    "Displays the menu if neccecary or carrys out the specified flag"
    
    links = sys.argv
    length = len(links)
    
    #If the flag exists get it
    if length > 1:
        flag = links[1]

    #If no flag is passed, then ask them for a URL to convert
    if length == 1:
        link = input("Enter channel url: ")
        print(cv.convert(link))
    
    #If help flag passed, print help
    elif flag == "-h":
        print_help()

    #If flag is -u, and a URL is given, process URL(s) and convert them
    elif flag == "-u" and length > 2:
        links.pop(0)
        links.pop(0)

        cv.mass_convert(links, length - 2) # -2 as we popped 2 from list above

    #If flag is for a file, get URL(s) from the file
    elif flag == "-f" and length == 3:
        try:
            #Read the links from the file passed and calculate length
            links = open(links[2], "r").readlines()
            length = len(links)

            #Remove \n from links list
            for i in range(length):
                links[i] = links[i][:-1]
            
            #Convert the links
            cv.mass_convert(links, length)

        #If file not found then print so
        except FileNotFoundError:
            print("File not found")
    
    #Notifies the user if command not found
    else:
        print("Command unknown, printing help...")
        print_help()


main()
