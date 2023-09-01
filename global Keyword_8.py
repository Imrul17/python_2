#global keyword
def func():
    global x # it is local variable but it is global keyward
    x = " imrul kayes "

func()
print("My name is"+x)

x = " hasan"
def func():
    global x # it is local variable but it is global keyward
    x = " imrul kayes "

func()
print("My name is"+x)

x = " hasan"
def func():
    global x # it is local variable but it is global keyward
    x = " imrul kayes "
print("My name is"+x)
func()
print("My name is"+x)
