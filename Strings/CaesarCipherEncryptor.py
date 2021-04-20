inputString = list(input())
key = int(input())
outputString=''
for letter in inputString:
    value = ord(letter) + key
    if value > 122:
        value = value % 122
        outputString+=chr(96+value)
    else:
        outputString+=chr(value)
print(outputString)
# Input
# xyz (Small letters Only)
