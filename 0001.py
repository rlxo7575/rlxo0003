# Find Capital Words

Capital = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def FindCapital(list,word):
    output = []
    for a,b in enumerate(word):
        for i in list:
            if i == b:
                output.append(a)
    return output

while True:
    choice = input("WORD : ")
    if choice == "stop":
        break
    print(FindCapital(Capital,choice))