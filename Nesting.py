#Take input of a word

string - input("Please enter your own word : ")
char = input("Please enter your own Character :)
i = 0
court = 0
#loop will find the occurence of character
while(i < len(string)): # string operation

    if(string[i] == char): #condiition 1
        count = count + 1
    i = i + 1

    #Display the result 
    print("The total Number of Times ",char, "has Occured = ",
    court)
