# pyhton task 1st

def reverse(s):
    reverse_str=""
    for i in range(len(s)-1,-1,-1):
        reverse_str +=s[i]
    return reverse_str
    
string = str(input("enter a string :"))
reverse_str = reverse(string)
print("output:",reverse_str)
