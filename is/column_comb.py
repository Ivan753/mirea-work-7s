text = list (
  "ОННАНЦОНДЛЬХФИСНИАТЫКЕЬД"
)

key = list(
  "XX24X3"
)

matrix = []

# generate matrix
lenRow = len(text) // len(key)
unusedInKeyColumns = []

for i in range(len(key)):
  matrix.append(text[lenRow*i:lenRow*i+lenRow])
  if str(i+1) not in key:
    unusedInKeyColumns.append(matrix[i])

# showing matrix func
def printMatrixWithKey(key, matrix):
  print()
  for i in key:
    print(i, end=" ")
  print()

  for i in range(len(matrix[0])):
    print()
    for j in range(len(matrix)):
      print(matrix[j][i], end=" ")
  print()

# display ini matrix
printMatrixWithKey(key, matrix)

# decode
## display with current key
print("X count", key.count("X"))

# get all X-key variants
allVariants = []
def FindAllVariants(count, key):
  if len(count) == 1:
    key.append(count[0])
    allVariants.append(key)
  else:
    for i in range(len(count)):
      newCount = count.copy()
      newKey = key.copy()

      newKey.append(count[i])
      newCount.remove(count[i])

      FindAllVariants(newCount, newKey)

FindAllVariants(unusedInKeyColumns, [])

# display all variants
for variant in allVariants:
  newMatrix = []
  for a in key:
    if a != "X":
      newMatrix.append(matrix[int(a)-1])
    else:
      newMatrix.append(variant.pop())

  printMatrixWithKey(key, newMatrix)

