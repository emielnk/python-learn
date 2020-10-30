import Object.Animal
import Object.Food

def main() :
    times = input("Input how much time do u want to print Hello World: ")
    helloWorldForNTimes(times)

def helloWorld():
    print("Hello World")

def helloWorldForNTimes(times) :
    for i in range(times) :
        print("Hello World")

main()