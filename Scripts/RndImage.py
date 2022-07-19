import os
from random import randint

def GetRndImage():
    path = './Sources/Images/'
    files = os.listdir(path)
    return path + files[randint(0, len(files) - 1)]