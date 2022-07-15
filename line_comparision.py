import math


# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#
#     def line_length(self):
#         z = (self.x1 * self.x1 - self.x2 * self.x2) + (self.y1 * self.y1 - self.y2 * self.y2)
#         if z < 0:
#             value = z * (-1)
#         else:
#             value = z
#             print("Length Of Line 1 Is :{}".format())
#
#         return math.sqrt(value)
#
#     def comparision(self,line2):
#         linelength1 = self.line_length()
#         linelength2 = line2.line_length()
#         var = ''
#         if linelength1 == linelength2:
#             var = "Equal"
#         elif linelength1 > linelength2:
#             var = "Greater Than"
#         elif linelength1 < linelength2:
#             var = "Less Than"
#         print("Line 1 {} is  {} To Line 2 {}".format(linelength1, var, linelength2))
#
#         #sq_len = (pow(self.x2, 2) - pow(self.x1, 2)) + \
#                  #(pow(self.y2, 2) - pow(self.y1, 2))
#         #return round(math.sqrt(sq_len))
#
#
# if __name__ == "__main__":
#     x1 = int(input("Enter The Co-Ordinates x For Point 1: "))
#     y1 = int(input("Enter The Co-Ordinates y For Point 1: "))
#     x2 = int(input("Enter The Co-Ordinates x For Point 2: "))
#     y2 = int(input("Enter The Co-Ordinates y For Point 2: "))
#     line = Line(x1,y1,x2,y2)
#
#
#     x3 = int(input("Enter The Co-Ordinates x For Point 3: "))
#     y3 = int(input("Enter The Co-Ordinates y For Point 3: "))
#     x4 = int(input("Enter The Co-Ordinates x For Point 4: "))
#     y4 = int(input("Enter The Co-Ordinates y For Point 4: "))
#     line2 = Line(x3,y3,x4,y4)
#
#     line.comparision(line2)
#     line2.comparision(line)
#
#


class Line_Comparision:

    def line_length(self, x1, y1, x2, y2):
        return line_length(x1, y1, x2, y2)

    def two_line_comparision(self, x1, y1, x2, y2, x3, y3, x4, y4):
        return two_line_comparision(x1, y1, x2, y2, x3, y3, x4, y4)

    def two_line_input(self, x1, y1, x2, y2, x3, y3, x4, y4):
        return two_line_input(x1, y1, x2, y2, x3, y3, x4, y4)


def line_length(x1, y1, x2, y2):
    x1 = x1
    y1 = y1
    x2 = x2
    y2 = y2

    z = (x1 * x1 - x2 * x2) + (y1 * y1 - y2 * y2)
    if z < 0:
        value = z * (-1)
    else:
        value = z

    length = math.sqrt(value)
    print("length of line is {}".format(length))


def two_line_comparision(x1, y1, x2, y2, x3, y3, x4, y4):
    x1 = x1
    y1 = y1
    x2 = x2
    y2 = y2
    x3 = x3
    y3 = y3
    x4 = x4
    y4 = y4

    z1 = ((x1 * x1 - x2 * x2) + (y1 * y1 - y2 * y2))
    z2 = ((x3 * x3 - x4 * x4) + (y3 * y3 - y4 * y4))
    if z1 < 0:
        value1 = z1 * (-1)
    else:
        value1 = z1

    length1 = math.sqrt(value1)

    if z2 < 0:
        value2 = z2 * (-1)
    else:
        value2 = z2

    length2 = math.sqrt(value2)

    print("Length Of Line1 is: {} units".format(length1))
    print("Length Of Line2 is: {} units".format(length2))

    if length1 == length2:
        print("Line 1 Of Length {} units is equal to line 2 of length {} units".format(length1, length2))
    else:
        print("Line 1 of length {} units is not equal to line 2 of length {} units".format(length1, length2))


def two_line_input(x1, y1, x2, y2, x3, y3, x4, y4):
    z1 = ((x1 * x1 - x2 * x2) + (y1 * y1 - y2 * y2))
    z2 = ((x3 * x3 - x4 * x4) + (y3 * y3 - y4 * y4))

    if z1 < 0:
        value1 = z1 * (-1)
    else:
        value1 = z1

    length1 = math.sqrt(value1)
    if z2 < 0:
        value2 = z2 * (-1)
    else:
        value2 = z2

    length2 = math.sqrt(value2)

    print("Length of Line1 is : {} units".format(length1))
    print("Length of Line2 is : {} units".format(length2))

    if length1 < length2:
        print("Line 1 of Length {} units is Less than Line 2 of Length {} units ".format(length1, length2))
    elif length1 > length2:
        print("Line 1 of Length {} units is Greater than Line 2 of Length {} units".format(length1, length2))
    else:
        print("Line 1 of Length {} units is Equal to Line 2 of Length {} units".format(length1, length2))


def errorHandler():
    return "Invalid Choice"


def main():
    print(
        """
        Choose Any Operation That You Want To Perform:
        ----------------------------------------------
        1.Check The Length Of Line\n
        2.Check The Two Lines Are Equal Or Not\n
        3.Check Between Two Lines Which One Is Greater,Lesser Or Equal
        """
    )

    choice = int(input("Choose Any Option: "))

    operation = {
        1: line_length,
        2: two_line_comparision,
        3: two_line_input
    }
    if choice == 1:

        x1 = int(input("Enter The Co-Ordinates x For Point 1: "))
        y1 = int(input("Enter The Co-Ordinates y For Point 1: "))
        x2 = int(input("Enter The Co-Ordinates x For Point 2: "))
        y2 = int(input("Enter The Co-Ordinates y For Point 2: "))

        length = Line_Comparision()
        length.line_length(x1, y1, x2, y2)

    elif choice == 2:

        x1 = int(input("Enter The Co-Ordinates x For Point 1: "))
        y1 = int(input("Enter The Co-Ordinates y For Point 1: "))
        x2 = int(input("Enter The Co-Ordinates x For Point 2: "))
        y2 = int(input("Enter The Co-Ordinates y For Point 2: "))
        x3 = int(input("Enter The Co-Ordinates x For Point 3: "))
        y3 = int(input("Enter The Co-Ordinates y For Point 3: "))
        x4 = int(input("Enter The Co-Ordinates x For Point 4: "))
        y4 = int(input("Enter The Co-Ordinates y For Point 4: "))

        length1 = Line_Comparision()
        length1.two_line_comparision(x1, y1, x2, y2, x3, y3, x4, y4)

    elif choice == 3:

        x1 = int(input("Enter The Co-Ordinates x For Point 1: "))
        y1 = int(input("Enter The Co-Ordinates y For Point 1: "))
        x2 = int(input("Enter The Co-Ordinates x For Point 2: "))
        y2 = int(input("Enter The Co-Ordinates y For Point 2: "))
        x3 = int(input("Enter The Co-Ordinates x For Point 3: "))
        y3 = int(input("Enter The Co-Ordinates y For Point 3: "))
        x4 = int(input("Enter The Co-Ordinates x For Point 4: "))
        y4 = int(input("Enter The Co-Ordinates y For Point 4: "))

        length2 = Line_Comparision()
        length2.two_line_input(x1, y1, x2, y2, x3, y3, x4, y4)

    else:
        print(errorHandler())

    output = operation.get(choice)


if __name__ == "__main__":
    main()
