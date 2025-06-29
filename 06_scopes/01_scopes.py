username = "Milan"

def name():
    # global username
    # print(username)
    username2="Milan2"
    username="Hello"
    print(username)

name()
print(username)
# print(username2)


x=11
def fun1():
    x=12
    def fun2():
        # global x
        print(x)
    fun2()
fun1()



y=11
def fun3():
    y=12
    def fun4():
        # global y
        print(y)
    return fun4

myresult = fun3()                         # here in fun3 we return instance of fun4 but thing that need to be noted is that here with fun4 all the refrences of variable that are assciated with fun4 will also be return with that so myResult() will print 12. this is bag theory
# print(myresult)
myresult()





def function(num):
    def actual(a):
        return a ** num
    return actual

f = function(2)         
g = function(3)
# if you see and understand then now "f" have refrence of "actual" function and refrence of num(here num = 2) so now if we  call "f" and pass "a" it always return square of a.
# like wise in "g", "g" have refrence of "actual" function and refrence of num(here num = 3) so now if we  call "g" and pass "a" it always return qube of a.

print(f(3))
print(g(3))
