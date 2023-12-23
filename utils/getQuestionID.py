from utils.getCompiler import *

def getQuestionID(pathToCode):
    n = len(pathToCode)
    mx = 0
    for i in range(n):
        if pathToCode[i] == '/':
            mx = i
            
    questionID = pathToCode[mx + 1:]
    n = len(questionID)
    for i in range(n):
        if questionID[i] == '.':
            compiler = getCompiler(questionID, i)
            questionID = questionID[:i]
            break
    return questionID, compiler