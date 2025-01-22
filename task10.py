# pyhton task 10th

def factorial(num):
    if num>=0:
        if( num == 0 or num ==1):
            return 1
        else:
            return num * factorial(num-1)
    else:
         return "enter valid number"

print("factorial :",factorial(5))
