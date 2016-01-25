#!/usr/bin/python

# Script Name	: cspAnalyzer.py
# Author		: Sharmila Paneerselvam
# Version		: 0.1
# Usage         : python cspAnalyzer.py <url>

# Import the modules
import sys
import requests

#function to invoke the requested url
def loadUrl(uriName):    
    if(uriName == ""):
        print('URL is not defined')
        exit(2)
    
    print("Invoking url: "+ uriName+"\n")    
    r = requests.head(uriName)
    if (r.status_code != 200):
        print(r.status_code)
        exit(2) # exit if not success    
    return r
    
#analyze the headers for content security headers
def analyze(request):
    #get the content security header if the req is success
    csp = request.headers.get('Content-Security-Policy')
    if(csp):
        prettyPrintHeaders(csp)
    else:
        print('Content-Security-Policy not defined')        
    
#help function
def printHelp():
    print('usage: python cspAnalyzer.py <url>')
    
def printHeader():
    print('\n*******************************************\n')
    print("cspAnalyzer v0.1 \nby Sharmila Paneerselvam\n") 
    print('cspAnalyzer is a light weight command line utility to check the Content Security Policy in a given URL.\n\nPlease check the following link to know more about http://content-security-policy.com/')
    print('\n*******************************************\n')
    
#pretty print headers
def prettyPrintHeaders(cspHeader):
    cspList = cspHeader.split(";")
    for csp in cspList:
        content = csp.split(' ')
        header = 1
        for c in content:            
            if(header):
                print(c)
            else:
                print('\t'+c)
            header = 0
            
def main():
    printHeader()    
    uriName = ''
    
    #check for necessary args
    if(len(sys.argv) !=2):
        printHelp()
        exit(2)
   
   #assign the user passed url     
    uriName = sys.argv[1]          
    
    #invoke the website
    r = loadUrl(uriName)
    
    #analyze the headers for CSP
    analyze(r)
    exit(0)
    

if __name__ == '__main__':
    main()