import sys

def tokenize(my_list):
   #Funktion för att dela upp text i ord
    words = []
    for line in my_list:
        start = 0
        while start < len(line):
            while start < len(line) and line[start].isspace():
                start += 1
            if start >= len(line):
                break
            if line[start].isdigit():
                end = start
                while end < len(line) and line[end].isdigit():
                    end += 1
                words.append(line[start:end])
                start = end
            elif line[start].isalpha():
                end = start
                while end < len(line) and line[end].isalpha():
                    end += 1
                words.append(line[start:end].lower())
                start = end
            else:
                words.append(line[start])
                start += 1
    return words
    
def countWords(words, stopWords): #Räknar ord och exkluderar stoppord
    my_dict={}
    for i in words:
        if i not in stopWords:
            my_dict.setdefault(i, 0)
            my_dict[i] += 1
    return my_dict
            
def printTopMost(my_dict, n): #Skriver ut de n vanligaste orden
    sorted_dict = dict(sorted(my_dict.items(),key=lambda item: item[1], reverse=True))
    filtered_dict = list(sorted_dict.items())[:n]
    for k, v in filtered_dict:
        print(str(k).ljust(19), str(v).rjust(5))

def main():
    n = 2
    my_list = ''
    tokenize(my_list)
    stopWords = []
    countWords(tokenize(my_list), stopWords)
    my_dict = countWords(tokenize(my_list), stopWords)

    printTopMost(my_dict, n)
main()
