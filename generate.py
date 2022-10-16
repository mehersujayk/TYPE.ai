from random import *
from aitextgen import aitextgen
from keytotext import pipeline
import spacy
import requests
from ainlp import ai
from ainlp import nlp

def getRelatedWord(topic):
  # dictionary=PyDictionary(topic)
  # meaning = dictionary.getMeanings()
  import requests

  req = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{topic}")

  output = req.json()[0]['meanings'][0]['definitions'][0]['definition']
  meaning = output
  nlp_model = spacy.load("en_core_web_sm")
  doc1 = nlp_model(topic)
  doc2 = nlp_model(str(meaning))
  returnList = []
  for word in str(meaning).split():
    if(doc1.similarity(nlp_model(word)) > 0.5 and word not in returnList):
      returnList.append(word)

  returnList.append(topic)
  #   print(returnList)
  return returnList


def generateTextDiagnostic(keyword):
  inputPrompt = getRelatedWord(keyword)
  generatedPrompt = generatedTextGivenKeywords(inputPrompt)
  x =  ai.generate(n = 1, 
                   prompt = generatedPrompt[len(generatedPrompt)-1],
                   max_length = 150,
                   temperature = 0.4, 
                   do_sample = True,
                   return_as_list = True,
                   seed = randint(1, 1000),
                   repetition_penalty=1.3)
  return x 
  
def generatedTextGivenKeywords(keywords):
  params = {"do_sample":True, "num_beams":6, "no_repeat_ngram_size":1, "early_stopping":True}
  sentences = []
  for x in range(len(keywords)):
     nlpList = []
     for num in range(x+1):
       nlpList.append(keywords[num])
     sentence = nlp(nlpList, **params)
     sentences.append(sentence)
  return sentences


# output = generateTextDiagnostic('Dog')

# for word in output:
#   print(word)


