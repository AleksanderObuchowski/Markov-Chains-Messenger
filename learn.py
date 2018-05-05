import sys
import os
import json
import codecs
import argparse
import subprocess
def readArguments():
    numArguments = len(sys.argv)-1
    dictionaryFile = "dictionary.json"
    inputFile = ""
    if numArguments>= 1:
        dictionaryFile = sys.argv[1]
    if numArguments>=2:
        inputFile = sys.argv[2]
    return dictionaryFile,inputFile

def getmessages(name, inputFile):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname,"messages.htm")

    command = "fbcap messages "+filename + " > " +inputFile+ " -t "+name.split(" ")[0]+" -f text"
    print(command)
    subprocess.call(command,shell =True)
    print("saved conversation in "+ inputFile)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help ="Name",type=str)
    parser.add_argument("surname", help="Surname", type=str)
    parser.add_argument('-d','--dictionary',help = "Name of the output dictionary",type = str)
    args = parser.parse_args()
    name = args.name
    surname =args.surname
    inputFile= name+".txt"
    dictionaryFile= name+"_"+surname+".json"
    getmessages(name,inputFile)


    dictionary= loadDictionary(dictionaryFile)
    if inputFile == "":
        #interactive mode
        while True:
            userInput = input(">> ")
            if userInput == "":
                break
            dictionary = learn(dictionary,userInput)
            updateFile(dictionaryFile,dictionary)
    else:
        #read from file
        print("reading from "+ inputFile)


        fp= codecs.open(inputFile,"r", "UTF-8")
        lines= fp.readlines()
        print("number of messages: "+str(len(lines)))

        for i in range(2,len(lines)):
            print("learning from message "+ str(i) + " out of "+ str(len(lines)))
            line = lines[i].split(' ')

            try:

                if line[1]== name and line[2]==surname+":":
                    message = line[3:]
                    message = ' '.join(message)
                    dictionary = learn(dictionary,message)
                    updateFile(dictionaryFile,dictionary)

            except:
                pass
        print("learning succesfull, data stored in "+ dictionaryFile)
def loadDictionary(filename):
    if not os.path.exists(filename):
        file = open(filename,"w")
        json.dump({},file)
        file.close()
    file =open(filename,"r")
    dictionary = json.load(file)
    file.close()
    return dictionary


def learn(dict,input):
    tokens = input.split(" ")

    for i in range (0,len(tokens)-1):
        currentWord = tokens[i]
        nextWord = tokens[i+1]
        if currentWord not in dict:
            dict[currentWord] = {nextWord:1}
        else:
            allNextWords = dict[currentWord]
            if nextWord not in allNextWords:
                dict[currentWord][nextWord] = 1
            else:
                dict[currentWord][nextWord]= dict[currentWord][nextWord] +1
    return dict

def updateFile(filename,dictionary):
    file = open(filename, "w")
    json.dump(dictionary,file)
    file.close




main()
