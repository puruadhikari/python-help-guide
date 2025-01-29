#basic_calculator("12+34-5")

def basic_calculator(expression):
    if not expression or len(expression) ==0:
        return 0
    i =0
    result = 0
    sign = 1
    while i < len(expression):
        if expression[i].isdigit():
            num = expression[i]
            while i+1 < len(expression) and expression[i+1].isdigit() :
                i+= 1
                num += expression[i]
            num = int(num)
            result += num*sign
        elif expression[i] =="+":
            sign = 1
        elif expression[i] == "-":
            sign = -1
        i += 1
    return result

print(basic_calculator("12+34-5"))