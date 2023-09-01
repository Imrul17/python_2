#global variable
x = "awesome"
def func():
    print("python is "+x)

func()


#local and global variable

x = "awesome" #global variable
def func():
    x="fantastic" #local variable
    print("python is really "+x)

func()

print("python is really "+x)


# global variable funtion

x = "awesome" #global variable
def func():
    # x="fantastic" #local variable
    print("python is really "+x)

func()

print("python is really "+x)