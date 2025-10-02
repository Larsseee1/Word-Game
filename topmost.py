import sys
import wordfreq
import urllib.request

def main():
    lines_list = []
    if sys.argv[2].startswith('http'):
        response = urllib.request.urlopen(sys.argv[2])
        url_lines_list = response.read().decode("utf8").splitlines()
        for lines in url_lines_list:
            lines_list.append(lines)
             
        
            
    else:
        with open(sys.argv[2], encoding='utf-8') as input_file:
                sys.argv[2] = input_file.readlines()
        for lines in sys.argv[2]:
                print(lines)
                print(lines.strip())
                lines_list.append(lines)
    
    with open(sys.argv[1], encoding='utf-8') as input_file_2:
        sys.argv[1] = input_file_2.readlines()
    lines_list_stop = []
    
    for lines in sys.argv[1]:
        lines_list_stop.append(lines.strip('\n'))
    #print(lines_list)


    token = wordfreq.tokenize(lines_list)
    
    count = wordfreq.countWords(token, lines_list_stop)
    
    most = wordfreq.printTopMost(count, int(sys.argv[3]))
    print(most)
    #print(sys.argv[2][0])
main()


