class myClass():
    def method1(self):
        print("This is Method 1")
    def method2(self,Mystring):
        print('This is Method 2'," ",Mystring)

class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("This is Another class Method 1")
    def method2(self,Mystring):
        print('This is Another class Method 2'," ",Mystring)

def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")
    c2 = anotherClass()
    c2.method1()
    c2.method2('This is from another class')

if __name__ == "__main__":
    main()