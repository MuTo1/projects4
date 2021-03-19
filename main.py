class Calculate:

    def sum(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y

    print("აირჩიეთ ოპერაცია.")
    print("1.მიმატება")
    print("2.გამოკლება")
    print("3.გამრავლება")
    print("4.გაყოფა")

    while True:
        choice = input("შეიყვანეთ თქვენი არჩევანი(1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):

            num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
            num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

            if choice == '1':
                print(num1, "+", num2, "=", sum(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", sub(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
            break
        else:
            print("გთხოვთ აირჩიოთ 1-დან 4-მდე ციფრი")