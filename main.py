import math as m

pi = 3.14

print("Welcome to PyCal. The calculator made with pure python.")
print("")
print("")
op = str(input(">(Simple operations, Perimeter and area, Speed, Weight, Digital Storage, Temperature) "))


def simple():
    # Normal operations like addition and subtraction
    operation = ["Pi", "Addition", "Subtraction", "Multiplication", "Division", "Square of numbers"]
    print(operation)
    operation_choice = str(input("Enter a mathematical operation: "))
    if operation_choice == "Pi":
        print(m.pi)

    elif operation_choice == "Addition":
        add_num1 = float(input("Enter a number: "))
        add_num2 = float(input("Enter 2nd number "))
        add_result = add_num1 + add_num2
        print("Sum is", add_result)

    elif operation_choice == "Subtraction":
        sub_num1 = float(input("Enter a number: "))
        sub_num2 = float(input("Enter 2nd number: "))
        difference = sub_num1 - sub_num2
        print("Difference is", int(difference))

    elif operation_choice == "Multiplication":
        mul_num1 = float(input("Enter a number: "))
        mul_num2 = float(input("Enter 2nd number: "))
        product = mul_num1 * mul_num2
        print("Product is", product)

    elif operation_choice == "Division":
        div_num1 = float(input("Enter a number: "))
        div_num2 = float(input("Enter 2nd number: "))
        quotient = div_num1 / div_num2
        print("Quotient is", float(quotient))

    elif operation_choice == "Square of numbers":
        sqr = float(input("Enter number to find square: "))
        first = m.pow(sqr, 2)
        print(first)


def PerimeterArea():
    # Calculate perimeter and Area of different shapes
    types = ["Circumference of a circle", "Diameter of a circle", "Radius of a circle", "Perimeter of square",
             "Perimeter of rectangle",
             "Area of square", "Area of circle", "Area of rectangle", "Area of triangle"]
    print(types)
    choice = str(input("Enter the name as they are: "))

    if choice == "Circumference of a circle":
        r = float(input("Enter radius: "))
        c = 2 * (pi * r)
        print("Circumference is", c)

    elif choice == "Diameter of a circle":
        rad = float(input("Enter radius: "))
        d = 2 * rad
        print("Diameter is", d)

    elif choice == "Radius of a circle":
        a = float(input("Enter area of circle: "))
        radius = m.sqrt(a / pi)
        print(float("Radius is", radius))

    elif choice == "Perimeter of square":
        sq1 = float(input("Enter side 1: "))
        sq_perimeter = sq1 * 4
        print("Perimeter is", sq_perimeter)

    elif choice == "Perimeter of rectangle":
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        rectPerimeter = 2 * (l + b)
        print("Perimeter is", rectPerimeter)

    elif choice == "Area of square":
        side = float(input("Enter side: "))
        sq_area = side * side
        print("Area of square is", sq_area)

    elif choice == "Area of circle":
        areaRadius = float(input("Enter radius: "))
        CircleArea = pi * (m.pow(areaRadius, 2))
        print(CircleArea)

    elif choice == "Area of rectangle":
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        rectArea = l * b
        print(rectArea)

    elif choice == "Area of triangle":
        a = float(input("Enter side 1 of triangle: "))
        b = float(input("Enter side 2 of triangle: "))
        c = float(input("Enter side 3 of triangle: "))
        s = (a + b + c) / 2
        TriArea = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print(TriArea)


def Speed():
    # Calculate different speed measurements
    calculations = ["kmph to mph", "mph to kmph", "meter per second to mph", "mph to meter per second",
                    "kmph to meter per second",
                    "meter per second to kmph"]
    print(calculations)
    convert = str(input("Enter any one of the above: "))

    if convert == "kmph to mph":
        kmph = float(input("Enter Kilometers per hour: "))
        mph = kmph / 1.609
        print(mph)

    elif convert == "mph to kmph":
        m = float(input("Enter miles per hour: "))
        k = m * 1.609
        print(k)

    elif convert == "meter per second to mph":
        meter = float(input("Enter meter per second: "))
        mph = meter * 2.237
        print(mph)

    elif convert == "mph to meter per second":
        mile = float(input("Enter miles per hour: "))
        meter = mile / 2.237
        print(meter)

    elif convert == "kmph to meter per second":
        k = float(input("Enter kilometers per hour: "))
        Meter = k * 3.6
        print(Meter)

    elif convert == "meter per second to kmph":
        mETER = float(input("Enter meter per second: "))
        kmph = mETER / 3.6
        print(kmph)


def Weight():
    # Calculate weight
    weightCal = ["Kilos to pounds", "Pounds to kilos", "Kilos to ton",
                 "Ton to kilos"]
    print(weightCal)
    weightChoice = str(input("> "))

    if weightChoice == "Kilos to pounds":
        kg = float(input("Enter Kilograms: "))
        lbs = kg * 2.205
        print(lbs)

    elif weightChoice == "Pounds to kilos":
        lbs = float(input("Enter pounds: "))
        kgs = lbs / 2.205
        print(kgs)

    elif weightChoice == "Kilos to ton":
        kilo = float(input("Enter Kilogram: "))
        ton = kilo / 1000
        print(ton)

    elif weightChoice == "Ton to kilos":
        tonne = float(input("Enter Ton: "))
        kilos = tonne * 1000
        print(kilos)


def DigitalStorage():
    # Calculate digital storage
    digi = ["MB to GB", "GB to MB", "TB to GB", "GB to TB"]
    print(digi)

    DigitalChoice = str(input("> "))

    if DigitalChoice == "MB to GB":
        mb = float(input("Enter MegaByte: "))
        gb = mb / 1000
        print(gb)

    elif DigitalChoice == "GB to MB":
        giga = float(input("Enter GigaByte: "))
        mega = giga * 1000
        print(mega)

    elif DigitalChoice == "TB to GB":
        tb = float(input("Enter TeraByte: "))
        gig = tb * 1000
        print(gig)

    elif DigitalChoice == "GB to TB":
        gb = float(input("Enter GigaByte: "))
        tera = gb / 1000
        print(tera)


if op == "Simple operations":
    simple()

elif op == "Perimeter and Area":
    PerimeterArea()

elif op == "Speed":
    Speed()

elif op == "Weight":
    Weight()

elif op == "Digital Storage":
    DigitalStorage()
