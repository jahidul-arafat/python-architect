# add a main method
def main():
    variableValTypeSim()


def variableValTypeSim():
    print("Basic Datatype Simulation")
    print("------------------------")

    print("Basic Datatype Simulation")
    # define a new variable named 'x' and print its value and datatype
    x = 5
    print("x = ", x, " (", type(x), ")")
    # define a new variable named 'y' and print its value and datatype
    y = "Hello World"
    print("y = ", y, " (", type(y), ")")
    # define a new variable named 'z' and print its value and datatype
    z = True
    print("z = ", z, " (", type(z), ")")
    # define a new variable named 'w' and print its value and datatype
    w = None
    print("w = ", w, " (", type(w), ")")

    # define a new variable named 'i' of type 'float' and print its value and datatype
    i = 3.14
    print("i = ", i, " (", type(i), ")")
    print("")

    print("B. Imaginary Data Types")
    # define a new imaginary variable
    j = 1j
    print("j = ", j, " (", type(j), ")")

    # define a new variable named 'k' of type 'complex' and print its value and datatype
    k = 1 + 2j
    print("k = ", k, " (", type(k), ")")

    # given one float and one complex number, add these two variables
    # and print their values and datatypes
    print("")
    print("imaginary+float number")
    l = i + k
    print("l = ", l, " (", type(l), ")")

    # complex number multiplication
    # define two new complex numbers i.e. com1 and com2 and multiply them together
    # and print their values and datatypes®
    print("")
    print("complex number multiplication")
    com1 = 1j
    com2 = 1j
    com3 = com1 * com2
    print("com1 = ", com1, " (", type(com1), ")")
    print("com2 = ", com2, " (", type(com2), ")")
    print("com3 = ", com3, " (", type(com3), ")")
    print("")

    # basic string operations
    print("Basic String Operations")
    # define a new variable named'str1' and print its value and datatype
    str1 = "Hello"
    print("str1 = ", str1, " (", type(str1), ")")

    # define another string variable with different value
    str2 = "World........"
    print("str2 = ", str2, " (", type(str2), ")")

    # define a new variable named'str3' and print its value and datatype
    str3 = str1 + " " + str2
    print("str3 = ", str3, " (", type(str3), ")")




if __name__ == "__main__":
    main()
