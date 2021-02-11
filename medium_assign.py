'''
This file contains the functions that you need for completing this assignment. 
1. expression_1() --> 30%
2. expression_2() --> 40%
3. expression_3() --> 30% 
Failure to follow the variable name guides will lead to reduction of 10 points. 
DO NOT EDIT THE FUNCTION NAMES.
'''

def expression_1(x):
    result = x ** 3 - (2 * x + x ** 2) - 100
    return result
    
    '''
    
        Write a code that returns value for the following expression: x^3 - (2x + x^2) - 100 
    
    '''


def expression_2(x, y):
    result = int((x ** 4 / (2 * y)) - 3 * x * y + 6 * y / (7 * x))
    return result

    '''
        Write code that returns only the integer value of the following expression: (x^4 / 2y) - (3xy) + (6y / 7x)
    '''



def expression_3(x, y):
    result = (x ** 3 + y ** 2) / (x ** 2 - y ** 3)
    return result

    '''
        Write code that returns the value of the following expression: (x^3 + y^2) / (x^2 - y^3)
    '''

if __name__ == "__main__":
    
    var_1 = expression_1(2)
    print(var_1)

    var_2 = expression_2(2, 1)
    print(var_2)

    var_3 = expression_3(2, 2)
    print(var_3)
