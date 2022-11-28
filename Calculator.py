
while('true') :
        def add(i1, i2):
            return i1 + i2
        def sub(i1, i2):
            return i1 - i2
        def multi(i1, i2):
            return i1 * i2
        def div(i1, i2):
            return i1 / i2


        calculator = input("1-Add, 2-subtract, 3- multiply, 4- divide: ")
        print (calculator)
        input1 = float(input("Add input 1: "))
        input2 = float(input("Add input 2: "))

        if calculator =="4" and input2 == "0":
            print('can not divide by zero')


        output = 0
        if calculator == "1":
            output = add(input1, input2)
        elif calculator == "2":
            output = sub(input1, input2)
        elif calculator == "3":
            output = multi(input1, input2)
        elif calculator == "4":
            output = div(input1, input2)
        else:
            print('function is not defined')

        print (output)

        exit = input("if you want to exit y/n: ")
        if exit == 'y':
             break
