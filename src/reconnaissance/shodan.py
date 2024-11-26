import shodan 
import sys 
import log
import os

SHODAN_API_KEY = "EZlTmNmBMAoCJ14ArLMs4u03huW7vj6j"

def read(filename):
    try: 
        with open(filename,'r') as file: 
            domains = f.readlines()
            return domains
    except FileNotFoundError:
        print(f"couldn't find {filename} on the directory")
    except Exception as e : 
        print(f"{e}")

def getHostInfo(): 

def getOpenPorts():

def searchVulnerability(): 

def getDomainInfo(): 

def getDevicesInfo(): 

def getGeoLocation(): 

def getAccountStatus(): 



def main():


if __name__ == "__main__":
    main()
