def CommonCode(spam):
    str = '' 
    for item in spam[:-1]:
      str += (item + ', ')
    str += 'and ' + spam[-1]
    return str