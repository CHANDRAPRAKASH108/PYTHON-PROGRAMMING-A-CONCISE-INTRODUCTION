def problem2_7():
    """ computes area of triangle using Heron's formula. """
    a=input("Enter length of side one: ")
    a=float(a)
    b=input("Enter length of side one: ")
    b=float(b)
    c=input("Enter length of side one: ")
    c=float(c)
    s=0.5*(a+b+c)
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print("Area of a triangle with sides",a, b, c,"is",area)
    