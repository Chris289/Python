import urllib

def read_text():
    quotes = open("C:\Users\Christopher\Documents\Python\Movie Quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.purgomalum.com/service/containsprofanity?text="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Pronfanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")
    
read_text()
