while 1:
    def add(x,y):
        return x + y
    def subtract(x,y):
        return x - y
    def multiply(x,y):
        return x * y
    def divide(x,y):
        return x / y

    print()
    print("Select operation")
    print("0. Exit")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Enter choice(0/1/2/3/4): "))

    if choice == 0:
        break

    if choice > 4 or choice < 0:
        print("틀린 입력을 하였습니다")
        continue

    num1 = float(input("첫번째 숫자를 입력하시오: "))
    num2 = float(input("두번째 숫자를 입력하시오: "))

    if choice == 1:
        print(num1, "+", num2, "=", add(num1,num2))
    elif choice == 2:
        print(num1, "-", num2, "=", subtract(num1,num2))
    elif choice == 3:
        print(num1, "*", num2, "=", multiply(num1,num2))
    else:
        print(num1, "/", num2, "=", divide(num1,num2))
