x=100#global variable
print("bfore function",x)#global function
def display():
    global x
    x=200
    y=300#local variable
    print(x)
    print(y)#local function
display()
print("after funtion",x)