from pywebio.input import *
from pywebio.output import *
def operation():
    a = input("Enter the first number：", type=FLOAT)
    b = input("Enter the second number：", type=FLOAT)
    c=0
    operation = radio("Choose any operation", options=['+', '*', '/', '%'])
    operation_name=""
    if operation=="+":
        operation_name="addition"
        c=a+b
    elif operation=="*":
        operation_name="multiplication"
        c=a*b
    elif operation=="/":
        operation_name="division"
        c=a/b
    else:
        operation_name="modulus"
        c=a%b
        
    put_text('The operation you have chosen between ' + str(a) + ' and ' + str(b) + ' is %s and the result will be %.1f .' % (operation_name, c))
if __name__ == '__main__':
    operation()