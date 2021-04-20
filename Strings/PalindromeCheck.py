word = input()
a = 0
b = len(word) - 1
while a < b :
    if word[a] != word[b]:
        print('Not A Palindrome')
        exit(0)
    a+=1
    b-=1
print('Palindrome!')




# Input
# wow
# abccba