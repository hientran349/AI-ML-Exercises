import gdown
import string

filePath = 'ex3_data.txt'  # Replace with your desired file name and extension
# fileUrl = 'https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko'
# gdown.download(fileUrl, filePath, quiet=False)


def removePunctuation(input_string):
    # Create a string of punctuation and newline characters
    punctuation = string.punctuation

    # Use list comprehension to filter out punctuation and newline characters
    return ''.join(char   for char in input_string   
                            if char not in punctuation and char != '\n')



def wordCountDict(filePath):
    # Read all data from the file
    aFile = open(filePath, "r")
    
    data = aFile.read()
    # dataLines = aFile.readlines()
    aFile.close()


    # # Preprocessing data by lines
    # for index, line in enumerate(dataLines):
    #     line = line.lower()
    #     line = removePunctuation(line)
    #     line = line.replace('\n', '').replace('\r', '') # Remove newline character
    #     dataLines[index] = line #WRITE BACK

    # # Split the words in all lines and join them
    # wordList = [word   for line in dataLines  for word in line.split(" ")]


    # Preprocessing whole data
    data = data.lower()
    # data = removePunctuation(data)
    data = data.replace('\n', '').replace('\r', '')
    wordList = data.split(" ")

    # Count the words
    result_dict = {}
    for word in wordList: # go through all words in the word list

        # Add/Update the item in the dictionary
        #  result_dict.get(word, 0): get current value (default is 0 if not found)
        result_dict[word] =  result_dict.get(word, 0) + 1

    print(result_dict)
    return result_dict


wordCountDict(filePath)