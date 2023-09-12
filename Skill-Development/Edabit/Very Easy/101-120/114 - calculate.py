def calculate(num1, num2, operator):
    ans = eval(str(num1) + operator + str(num2))
    print(int(ans))

calculate(24,100, "-") # -76
calculate(-20, -30, "+") # -50
calculate(1500,5, "//") # 300
calculate(38,3, "*") # 114
calculate(49,5, "%") # 4
calculate(7,2, "/") # 3.5