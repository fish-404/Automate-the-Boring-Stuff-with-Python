import re

def RegexStrip(sentence : str, letters = None):
    regexStr = r"[^\s].*[^\s]"
    if letters != None:
        regexStr = r"[^" + re.escape(letters) + r"].*[^" + re.escape(letters) + r"]"    
        print(regexStr)

    mo = re.compile(regexStr)
    matchObj = mo.search(sentence)
    if matchObj != None:
        return matchObj.group()
    else:
        return sentence