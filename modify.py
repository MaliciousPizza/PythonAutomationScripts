import fileinput, os , sys

#Filesearch equals command line argument to indicate file we are transforming
fileSearch = sys.argv[1]#input("File to search for: ")
#Textsearch = command line argument to indicate the text we are searching for
textSearch = sys.argv[2] #input("Text to search for: ")
#Textreplace = command line argument to indicate the text we are replacing textSearch with
textReplace = sys.argv[3]#input("Replacement text: ")

#Open and read filespec (smbd.txt)
filespec = open(fileSearch, "r")
#Create second reference to filespec in memory and write to it
filespec2 = open(fileSearch,"r+")
#For each line in filespec
for line in filespec:
    #Determine if the line has the text we are searching for
    if textSearch in line:
        #If the text we are searching for exists ask the user if they want to replace the string
        print(line,"to",line.replace(textSearch, textReplace))
        yn = input("Would you like to alter this line? ")
        if yn == "y":
            #If the user says yes to replace the string
            #Write to the file to replace the text
            filespec2.write(line.replace(textSearch, textReplace))
        #If the user does not want to replace the string continue
        else:
            print("Okay lets continue")
    #If the text is not in the file print text not found
    else:
        print("Text not found")
#Close filespec and second instance of filespec
filespec.close()
filespec2.close()