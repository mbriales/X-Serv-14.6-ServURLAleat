#!/usr/bin/python

from webapp import webApp   # Imports webApp class from webapp.py
import random               # For create random objects
import sys                  # For exit

# Creates a random number between 1 and 10000
URLaleatoria = str(random.randint(1, 10000))


# Defines my own class based in webapp.webAppp class
class myApp(webApp):
    # Defines new process answer
    def process(self, request):
        return ("200 OK",
                "<html><body>" +
                "<p>Hola" +
                ". Dame otra " +
                # Prints random URL
                "<a href='URL-aleatoria'>" + URLaleatoria + "</a>"
                "</p>" +
                "</body></html>")


# Executes the application
if __name__ == "__main__":
    try:
        myApp("localhost", 1234)
    except:
        print "Exit"
        sys.exit()
