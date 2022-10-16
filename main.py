import msvcrt as m
import generate
import store
from ainlp import ai
from ainlp import nlp

def get_diagnose(val):
    return generate.generateTextDiagnostic(val)

def get_wrong_words(text,past_list):
    return store.readType(text,past_list)

def prompt(input):
    diagnose = get_diagnose(input)

    for word in diagnose:
        print(word)

    # #send this diagnosis to ronit
    
    wrong_diagnosis = get_wrong_words(diagnose[0],[])
    # # send this list to ronit

    batch = generate.getRelatedWord(input)
    for word in wrong_diagnosis:
        batch.append(word)

    # print("related words")
    # print(related_words)
    # print("wrong_diagnosis")
    # print(wrong_diagnosis)
    # print("batch")
    # print(batch)

    #next button mechnics here

    past_wrong = wrong_diagnosis
    while True:
        text = generate.generatedTextGivenKeywords(batch)
        avgpos = round((len(text) / 4) * 3)
        print(text[avgpos])

        wrong_words = get_wrong_words(text[avgpos],past_wrong)

        for word in wrong_words:
            batch.append(word)

        # print("batch")
        # print(batch)

        print("You want to keep going? y/n")
        response = m.getch().decode('ASCII')
        print(response)
        if(response == 'n'):
            break

        past_wrong = wrong_words


    print("Good job!")
    return 0

# if(__name__ == "__main__"):
# prompt("Football")