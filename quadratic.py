def roots(a, b, c):
    disc = (b * b) - (4 * a * c)

    if disc > 0:
        root1 = ((-b + (disc**0.5)) / (2 * a))
        root2 = ((-b - (disc**0.5)) / (2 * a))
        print("Two real roots are: ", (root1, root2))

    elif disc == 0:
        root1 = root2 = -b / (2 * a)
        print("Two equal and real roots are:", (root1, root2))

    elif disc < 0:
        root1 = ((-b + (disc**0.5)) / (2 * a))
        root2 = ((-b - (disc**0.5)) / (2 * a))
        print("Two distinct complex roots are:", (root1, root2))


a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))
c = int(input('Enter the value of c: '))

roots(a, b, c)
