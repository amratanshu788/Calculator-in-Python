while input("Do you want open calculator? , Type 'y' or 'n': ").lower() == "y":
    n = int(input("Enter first number: "))
    m = int(input("Enter second number: "))
    function = input(
        "What do you want to perform: '+' , '-' , '*' ,'/' , '%', '//': ")
    if function == '+':
        ans1 = n + m
        print("Addition of", n, "and", m, "is", ans1)
    if function == '-':
        ans2 = n-m
        print("Subtraction of", n, "and", m, "is", ans2)
    if function == '*':
        ans3 = n*m
        print("Multiplication of", n, "and", m, "is", ans3)
    if function == '/':
        ans4 = n/m
        print("Division of", n, "and", m, "is", ans4)
    if function == '%':
        ans5 = n % m
        print("Modulus of", n, "and", m, "is", ans5)
    if function == '//':
        ans6 = n//m
        print("Floor Division of", n, "and", m, "is", ans6)
else:
    print("Thanks for showing up!!")
