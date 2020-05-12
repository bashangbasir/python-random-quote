import random

def main():
  while True:
    option = input("Show quote or input quote [1-show 2-input 3-exit]  : ")
    
    if option == "3":
      break 
    else:
      if option == "1":
        print_quote()
      elif option == "2":
        input_quote = input("type qoute to insert: ")
        insert_quote(input_quote)
      else: 
        print("Wrong input")

def print_quote():
  f = open("quotes.txt") # open file 
  quotes = f.readlines() # read the file content by line - return array of content lines
  f.close() # close file

  for i in range(3):
    print(quotes[random.randint(0,len(quotes)-1)],end="") # print random quotes from text file

def insert_quote(quote):
  f = open("quotes.txt","a") #open file with append mode
  f.write("\n") #write newline
  f.write(quote) #write string to the file
  f.close() # close file

if __name__== "__main__":
  main()
  
