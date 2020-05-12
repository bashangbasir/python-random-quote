import random

def primary():
  #print("Keep it logically awesome.")
  
  f = open("quotes.txt") # open file 
  quotes = f.readlines() # read the file content by line - return array of content lines
  f.close() # close file

  print(quotes[random.randint(0,len(quotes)-1)]) # print random quotes from text file

if __name__== "__main__":
  primary()
