lines = ([' Hej jag gillar korv.'])
def tokenize(lines):
    text = ' '.join(lines).lower()
    return text.split()
print(tokenize(lines))

    

