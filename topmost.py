import sys
import wordfreq

def main():
    lines_list = []
    with open(sys.argv[2], encoding='utf-8') as input_file:
        sys.argv[2] = input_file.readlines()
    for lines in sys.argv[2]:
        lines_list.append(lines)
    
    with open(sys.argv[1], encoding='utf-8') as input_file_2:
        sys.argv[1] = input_file_2.readlines()
    lines_list_stop = []
    for lines in sys.argv[1]:
        lines_list_stop.append(lines.strip('\n'))
    print(lines_list)
    token = wordfreq.tokenize(lines_list)
    count = wordfreq.countWords(token, lines_list_stop)
    most = wordfreq.printTopMost(count, int(sys.argv[3]))
    print(most)
main()


