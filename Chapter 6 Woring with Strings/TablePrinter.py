def getColWidths(table):
    colWidths = [0] * len(table)
    for x in range(len(table)):
        for y in range(len(table[0])):
            if len(tableData[x][y]) > colWidths[x]:
                colWidths[x] = len(tableData[x][y])
    return colWidths

def printTable(tableData):
    colWidths = getColWidths(tableData)
    for y in range(len(tableData[0])):
        curStr = ''
        for x in range(len(tableData)):
            curStr += tableData[x][y].rjust(colWidths[x]) + ' '
        curStr.rstrip()
        print(curStr)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)