def division(a, b):
    if b == 0:
        print("Couldn't division 0")
        return 0
    else:
        return a/b

if __name__=="__main__":
    a = int(input("a: "))
    b = int(input("b: "))
    print(division(a,b))
    