import re
def main() :
    generateGanjilGenap()

def generateGanjilGenap() :
    string1 = raw_input("Input your Plate Number: ")
    start = False
    lastDigit = 0
    number = int(getDigitsOnly(string1))
    if(number %2 == 0) :
        print("Genap")
    else :
        print("Ganjil")

def getDigitsOnly(string1) :
    digits = ''
    for i in range(len(string1)) :
        if(string1[i].isdigit()) :
            print(string1[i])
            char = string1[i]
            digits = digits + char
    return digits

main()