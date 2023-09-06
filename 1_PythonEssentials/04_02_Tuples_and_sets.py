# add a main method
def tupeSetOps():
    # create a tuple of strings
    strTup = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
    print(strTup)
    print(strTup.count('a'))
    print(strTup.index('a'))
    print(strTup.index('j'))
    print(strTup[0])

    returnedVal = returnTup()
    print(returnedVal)
    print(type(returnedVal))
    a,b,c= returnTup()
    print(a)
    print(b)
    print(c)

# define a function returning a tuple
def returnTup():
    return 1,2,3



def main():
    print("Hello World")
    tupeSetOps()


if __name__ == "__main__":
    main()
