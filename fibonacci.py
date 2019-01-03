#fibonacci series

def main() :
    print("Enter the number for Fibonacci series  : ")
    num = int(input())
    first = 0
    second = 1
    print(first, end = ' ')
    while second < num :
        print(second, end = ' ')
        first, second = second, first + second


if __name__ == '__main__' : main()
