import time
from difflib import SequenceMatcher
import msvcrt as m


def similarityRatio(a, b):
    return SequenceMatcher(None, a, b).ratio()



def similarSort(wrong_words,curr,thres):
    best = None
    for w in wrong_words:
        ratio = similarityRatio(curr,w)
        # print(curr + ", " + w)
        # print(ratio)
        if ratio >= thres:
            best = w
            thres = ratio
    if best != None:
        if len(best) > len(curr):
            wrong_words.remove(best)
            best = curr
        else:
            wrong_words.remove(best)
        wrong_words.insert(0,best)
    else:
        wrong_words.insert(0,curr)
    return wrong_words



def readType(text,wrong_words):
    word_list = text.split()
    printString = ""
    past = None

    # start = time.time()
    index = 0
    currWord = ""
    for letter in text:
        w = word_list[index]
        finished_word = False;
    
        while True:
            if letter == "\n":
                break;

            keyInput = m.getch().decode('ASCII')
            # print(keyInput + ", " + letter)

            if keyInput != letter and w not in wrong_words:
                if w[-1] in {'.','?','!',':',';',','}:
                    new_w = w[:-1]
                    similarSort(wrong_words,new_w,0.7)
                else:
                    similarSort(wrong_words,w,0.7)
            if keyInput == letter:
                print(letter)
                if letter in {' ','.','?','!',':',';',','}:
                    if past in {' ','.','?','!',':',';',','}:
                        index = index - 1
                    finished_word = True
                past = letter
                break;
        if finished_word == True:
            # print(index)
            index = index + 1
        
            
    # end = time.time()

    # elapsedTime = end - start
    # num_words = len(word_list)
    # wpm = round((num_words/elapsedTime) * 60)
    
    return wrong_words
        

# x = readType("psychology is the study of how people react to events.",[])
# print(x)