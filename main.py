# -*- coding: utf-8 -*-
from janome.tokenizer import Tokenizer
import random
import sys
import re
from Debug import Debugger
tokenizer = Tokenizer()
logger = Debugger("outLog.log")

def prob1():
    sentenses = sys.argv[1];
    logger.println(len(sentenses))
    count = 1
    for token in tokenizer.tokenize(sentenses):
        if(token.part_of_speech.split(",")[1] in ["固有名詞"] and random.randint(0,len(sentenses)//600) == 0):
            logger.println("({})".format(count),end="")
            count+=1
        else:
            logger.println(token.surface,end="")
        #logger.println("["+str(token)+"]",end="")
    logger.println()

def prop2():
    hinsiCounter = {}
    with open("sentenses.txt","r",encoding="utf-8") as f:
        sentenses = f.read()
    logger.println(len(sentenses))
    tokens = tokenizer.tokenize(sentenses)
    meisis = []
    for token in tokenizer.tokenize(sentenses):
        logger.println(token)
        if(token.part_of_speech.split(",")[0] in ["名詞"]):
            meisis.append(token.surface)
        try:
            hinsiCounter[token.part_of_speech.split(",")[0]]+=1
        except KeyError:
            hinsiCounter[token.part_of_speech.split(",")[0]] = 1
    indexis = [i for i in range(len(meisis))]
    ountes = []
    logger.println("置換対象数:{}".format(len(meisis)))
    logger.println("品詞カウンター:{}".format(hinsiCounter))
    for i in range(len(indexis)):
        indexindex = random.randint(0,len(indexis)-1)
        index = indexis.pop(indexindex)
        ountes.append(meisis[index])
    i = 0
    outSentenses = ""
    for token in tokenizer.tokenize(sentenses):
        if(token.part_of_speech.split(",")[0] in ["名詞"]):
            outSentenses += ountes[i]
            i+=1
        else:
            outSentenses += token.surface
    with open("sentensesOut.txt","w",encoding="utf-8") as f:
        f.write(outSentenses)
    logger.println(outSentenses)
prop2()

pattern = r"((助動詞)*(名詞)+(名詞接尾)?(助動詞)*(名詞非自立)?(助動詞)*(助詞)*(記号)*)|((動詞)(助動詞)*(名詞接尾)*(助詞)*(記号)*)|(副詞)(助詞)*|(名詞)(動詞)|(感動詞)(記号)*|((形容詞)(助動詞)*(助詞)*)|((接続詞)(記号)*)"

def prob3():
    with open("sentenses.txt","r",encoding="utf-8") as f:
        sentenses = f.read()
    tangoList = []
    for token in tokenizer.tokenize(sentenses):
        tangoList.append(token.surface)
    end = 0
    start = 0
    outStr = ""
    while(start < len(tangoList)-end):
        logger.println("start:{}, end:{}".format(start,end))
        temp = "".join(tangoList[start:len(tangoList)-end])
        hinsiTemp = ""
        for token in tokenizer.tokenize(temp):
            if(token.part_of_speech.split(",")[1] in ["接尾","非自立"] and token.part_of_speech.split(",")[0] in ["名詞"]):
                hinsiTemp += token.part_of_speech.split(",")[0] + token.part_of_speech.split(",")[1]
            else:
                hinsiTemp += token.part_of_speech.split(",")[0]
        result = re.fullmatch(pattern,hinsiTemp)
        logger.println("文節:{}, 品詞:{}, result:{}".format(temp,hinsiTemp,result))
        if(result == None):
            end += 1
        else:
            start = len(tangoList[0:len(tangoList)-end])
            end = 0
            outStr += temp + "/"
    logger.println(outStr)
prob3()

logger.flush()