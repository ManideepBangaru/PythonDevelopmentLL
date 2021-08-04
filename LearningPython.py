# print('Hello World !!!')
# Name = input('Enter your Name : ')
# print("Nice to Meet you,",Name)

def main():
    print('Hello World !!!')
    Name = input('Enter your Name : ')
    print("Nice to Meet you,", Name)

# if __name__=="__main__":
#     main()

# Playing with variables
f = 0
print(f)

f = "abc"
print(f)

# Below code throws an error
# print('This is a string' + 123)
print('This is a string' + str(123))

# Global vs Local variables in functions
def someFunction():
    f = "def"
    print(f)

someFunction()
print(f)

def someFunction():
    global f
    f = "def"
    print(f)

someFunction()
print(f)

del f
# NameError: name 'f' is not defined
# print(f)

# Functions
def func1():
    print("Iam a function")

func1()
print(func1())
print(func1)

def func2(arg1,arg2):
    print(arg1," ",arg2)

def cube(x):
    return x**3
print("#########################")
func1()
print(func1())
print(func1)
func2(10,20)
print(func2(10,20))
print(cube(3))
cube(4)

def power(num,x=1):
    return num**x

print(power(2,3))
print(power(x=4,num=4))

def multi_add(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print(multi_add(1,2))
print(multi_add(1,2,3,4,5,6,7,8,9))

# Conditional structures
def checker(x,y):
    if (x<y):
        print('x is less than y')
    else:
        print('y is less than x')

checker(10,20)

def checker(x,y):
    if (x<y):
        print('x is less than y')
    elif(x==y):
        print('x is equal to y')
    else:
        print('y is less than x')

checker(20,20)

# conditional statement in one line
x = 30; y = 40;
result = "x is less than y" if (x<y) else "y is same or greater than x"
print(result)

x = 0
while (x < 50):
    print(x)
    x+=2

# using break and continue
for i in range(0,100):
    if i == 10:
        break
    else:
        print(i)
for i in range(0,100):
    if i == 10:
        continue
    elif i == 50:
        break
    else:
        print(i)

days = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
for i,d in enumerate(days):
    print(i,"---->",d)