#Simple Calculator
def login (username, password):    

    farmers = {
        "Charles": "CHARLIE254",
        "Roesemary": "rose@254",
        "Guest": "guest34"
    }
    if username in farmers and password == farmers[username]:
        return f"Welcome, {username} to the farm yield calculator\n"
    else:
        return f"Calculator access forbidden,\nPlease try again later!"
    
username = input ("What\'s your username:")
password = input ("Input your password:")

print (login(username, password))


def calculator (num1, num2, operator):

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return float(round((num1 * num2), 2))
    elif operator == "/":
        if num2 != 0:
            return float(round((num1 / num2), 3))
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
    
num1 = input ("Key in your 1st parameter:")
num2 = input ("Key in your 2nd parameter:")
operator = input ("Key in the operator:")

#result = calculator (174.655, 65.46, "*")

result = calculator (num1, num2, operator)
print (f"Result: {result}")
