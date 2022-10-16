from random import *
from aitextgen import aitextgen
from keytotext import pipeline



ai = aitextgen(model='facebook/opt-1.3b')
nlp = pipeline("mrm8488/t5-base-finetuned-common_gen")