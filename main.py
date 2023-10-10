

def getNumberOfWord(str):
  return len(str.split(" "))

def getLetterCount(str):
  letterCount = {}
  for letter in str:
    letter = letter.lower()
    if not letter.isalpha() : continue
    if letter in letterCount :
      letterCount[letter] += 1
    else:
      letterCount[letter] = 1
  return letterCount


def reportDetails(letterCount):
  list = [[letter , count] for letter, count in letterCount.items()]
  sum = 0;
  
  for i in list: 
    sum += i[1]
  print(f"There are {sum} words in book")
  list.sort(key=lambda x : x[1], reverse=True)
  for letter in list:
    print(f"The '{letter[0]}' was found {letter[1]} times")
  pass

with open("book.txt", "r", encoding="utf-8") as file:
  fileContent = file.read()
  length = getNumberOfWord(fileContent)
  letterCount = getLetterCount(fileContent)
  reportDetails(letterCount)
  
file.close()

