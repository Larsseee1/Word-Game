import sys

def tokenize(my_list):
   
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
    #real_text = ''
    #text = ''.join(my_list)
    #for i in range(len(text)):
    #    if text[i].isalpha() and text[i-1].isdigit():
    #        real_text += ' ' + text[i]
    #    elif not text[i].isalpha() and not text[i].isdigit():
    #        real_text += ' ' + text[i] + ' '
    #    else:
    #        real_text += text[i]
    #return real_text.lower().split()
def countWords(words, stopWords):
    my_dict={}
    for i in words:
        if i not in stopWords:
            my_dict.setdefault(i, 0)
            my_dict[i] += 1
    return my_dict
            
    
    #for i in words:
    #    ammount = 0
    #    if i not in stopWords:
    #        for count in words and not my_dict[i]:
    #            if i == count:
    #                ammount +=1
    #        my_dict[i] = ammount           
    #    else:
    #        continue       
    #return my_dict
def printTopMost(my_dict, n):
    
    sorted_dict = dict(sorted(my_dict.items(),key=lambda item: item[1], reverse=True))
    filtered_dict = list(sorted_dict.items())[:n]
   
    for k, v in filtered_dict:
        print(str(k).ljust(19), str(v).rjust(5))
def main():
    n = 2
    my_list = ''
    
    tokenize(my_list)
    
    #with open('eng_stopwords.txt') as input_file:
        #StopWords_text = "".join(input_file.readlines())
        #stopWords = StopWords_text.split('\n')
    stopWords = []
    countWords(tokenize(my_list), stopWords)

    my_dict = countWords(tokenize(my_list), stopWords)

    printTopMost(my_dict, n)
main()
