def local():
    global a # have to declare first
    a = 1
    b = 2

a = "one"
b = "two"
local()
print(a)
print(b)