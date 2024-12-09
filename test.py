

myString = "This is going to be a really long string. I am hoping to break up the string by each word so that it splits each line at a space instead of in the middle of a word. "
myString += "I am not sure this is long enough so I am going to repeat myself. "
myString += "This is going to be a really long string. I am hoping to break up the string by each word so that it splits each line at a space instead of in the middle of a word."


#print(myString)

#print(os.get_terminal_size().columns)
import os
import textwrap
wrapped_text = textwrap.fill(myString, os.get_terminal_size().columns)
print(wrapped_text)


#for lcv in range(len(myString)%os.get_terminal_size().columns):
#    curIndex = os.get_terminal_size().columns*(lcv+1)
#    print(f"{curIndex = }\t\t{len(myString) = }")
#    while(curIndex < len(myString) and myString[curIndex] != " "):
#        curIndex -= 1
#        print(f"\t\t{curIndex = }\t\t{len(myString) = }")
#        if(myString[curIndex] == " "):
#            myString = myString[0:curIndex] + "\n" + myString[curIndex:]
#            break





print(myString)