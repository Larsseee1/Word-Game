import sys

def tokenize(my_list):
    real_text = ''
    text = ''.join(my_list)
    for i in range(len(text)):
        if i > 0 and text[i].isalpha() and text[i-1].isdigit():
            real_text += ' ' + text[i]
        elif not text[i].isalpha() and not text[i].isdigit():
            real_text += ' ' + text[i] + ' '
        else:
            real_text += text[i]
    return real_text.lower().split()
def countWords(words, stopWords):
    my_dict={}
    ammount = 0
    
    
    for i in words:
        ammount = 0
        if i not in stopWords:
            for count in words:
                if i == count:
                    ammount +=1
            my_dict[i] = ammount           
        else:
            continue       
    return my_dict
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
