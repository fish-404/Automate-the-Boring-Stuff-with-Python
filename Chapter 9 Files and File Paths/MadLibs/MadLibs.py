from replace import replaceAwithB

templateFile = open('template.txt', 'r') 
templateContent = templateFile.read()
templateFile.close()

print("Enter an adjective:")
templateContent = replaceAwithB(templateContent, "ADJECTIVE", input())
print("Enter a noun:")
templateContent = replaceAwithB(templateContent, "NOUN", input())
print("Enter a verb:")
templateContent = replaceAwithB(templateContent, "VERB", input())
print("Enter a noun:")
templateContent = replaceAwithB(templateContent, "NOUN", input())

print(templateContent)

resultFile = open('result.txt', 'w')
resultFile.write(templateContent)
resultFile.close()


