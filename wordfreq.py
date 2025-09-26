
my_list = ['clean water is drinkable water']

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

    #print('modified:', real_text)
    
    return real_text.lower().split()


tokens = tokenize(my_list)
#print(tokens)

with open('eng_stopwords.txt') as input_file:
    stopWords = input_file.readlines()


def countWords(words, stopWords):
    my_dict={}
    ammount = 0
    words = tokens
    
    for i in words:
        ammount = 0
        if i + '\n' not in stopWords:
            for count in words:
                if i == count:
                    ammount +=1
            my_dict[i] = ammount           
        else:
            continue                 
    return my_dict
print(countWords(tokens, stopWords))
def printTopmost(my_dict, n):
    sorted_dict = dict(sorted(my_dict.items(),key=lambda item: item[1], reverse=True))
    
   
    for i in range(n):
        for k, v in sorted_dict.items():
            print(k, v)
my_dict = countWords(tokens, stopWords)
n=2
printTopmost(my_dict, n)