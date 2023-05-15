import re

def regexCheck(regexStr : str, passwd : str):
    regexMo = re.compile(regexStr)
    if regexMo.search(passwd) != None:
        return  True
    else:
        return False

def lenDetect(string : str):
    if len(string) < 8:
        return False
    else:
        return True

def numberDetect(passwd : str):
    return regexCheck(r'\d', passwd)

def upperDetect(passwd : str):
    return regexCheck(r'[A-Z]', passwd)

def lowerDetect(passwd : str):
    return regexCheck(r'[a-z]', passwd)
    
def StrongPasswordDetection(passwd : str):
    return \
        lenDetect(passwd) \
        and numberDetect(passwd) \
        and upperDetect(passwd) \
        and lowerDetect(passwd)
    
