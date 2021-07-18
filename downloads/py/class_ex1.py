# global variable i
i = 2
class myobj:
    # local variable i
    i = 1
    print(i)
    def method1(self):
        # can only access global variable variable i
        # can access local variable i through self.i 
        return i, self.i
def main():
    myinst = myobj()
    print(myinst.method1()) 

print(__name__)

if __name__ == "__main__":
    main()