import math
class Polynomial:
    
    def __init__(self, placeholder):
        
        tuple_list =[] 
        if type (placeholder[0]) != tuple:
            length = len(placeholder)
            for n in range(0, length):
                tuple_list += [(placeholder[n],n)]

        elif type(placeholder[0]) == tuple:
            tuple_list = placeholder
        
        length = len (tuple_list)
        coexp = []
        for n in range(0, length):
            if tuple_list[n][0] != 0:
                coexp += [(tuple_list[n][0], tuple_list[n][1])]
            elif len(tuple_list) == 1 and tuple_list[0][1] == 0:
                coexp += [(0,0)]
        
        def getKey (item):
            return item[1]
        self.coexp = sorted(coexp, key = getKey, reverse = True)
        #coefficient first, exponent second
        
        exponent_dict = {}
        temp = self.coexp
        length = len(temp)
        third_list = []
        
        for n in range(0, length):
            exponent_dict.setdefault(temp[n][1], []).append(temp[n][0])
        
        for key in exponent_dict:
            coeff = 0
            for value in exponent_dict[key]:
                coeff += value
            third_list += [(coeff, key)] 
        
        self.coexp = third_list 
    
    
    def __str__ (self):
        length = len (self.coexp)
        printed_poly = ''
        for n in range(0, length):
            poly = str(self.coexp[n][0]) + 'x^'+ str(self.coexp[n][1])
            if n < length-1:
                if self.coexp[n][0] == 0:
                    printed_poly += ''
                else: 
                    printed_poly += poly + ' + '
            elif n == length-1:
                printed_poly += poly
        return str(printed_poly)

    
    def degree (self):
        return (self.coexp[0][1])
    
    def __add__ (self, other):
        exponent_dict = {}
        temp = self.coexp + other.coexp
        length = len(temp)
        third_list = []
        for n in range(0, length):
            exponent_dict.setdefault(temp[n][1], []).append(temp[n][0])
        for key in exponent_dict:
            coeff = 0
            for value in exponent_dict[key]:
                coeff += value
            third_list += [(coeff, key)]
        return Polynomial(third_list)

    def __sub__ (self, other):
        #change signs of subtracting polynomial
        sub_list = other.coexp
        length = len(sub_list)
        new_sub_list = []
        for n in range (0, length):
            new_sub_list += [(-1 * sub_list[n][0], sub_list[n][1])]
            
        exponent_dict = {}
        temp = self.coexp + new_sub_list
        length = len(temp)
        third_list = []
        for n in range(0, length):
            exponent_dict.setdefault(temp[n][1], []).append(temp[n][0])
        for key in exponent_dict:
            coeff = 0
            for value in exponent_dict[key]:
                coeff += value
            third_list += [(coeff, key)]
        return Polynomial(third_list)    

    def __mul__ (self, other):
        length1 = 0
        length2 = 0
        list1 = []
        list2 = []
        mult_list = []
    
        if len(self.coexp) >= len(other.coexp):
            length1 = len(self.coexp)
            length2 = len(other.coexp)
            list1 = self.coexp
            list2 = other.coexp
            
        elif len(self.coexp) < len(other.coexp):
            length1 = len(other.coexp)
            length2 = len(self.coexp)
            list1 = other.coexp
            list2 = self.coexp
            
        for n in range (0, length1):
            for x in range(0, length2):
                mult_list += [(list2[x][0] * list1[n][0],list2[x][1] + list1[n][1])]
        
        empty_list = [(0,0)]
        empty_poly = Polynomial(empty_list)
        mult_poly = Polynomial (mult_list)
        final_mult = mult_poly + empty_poly
        return (final_mult)
        
    def __call__ (self, x):
        length = len(self.coexp)
        solved_poly = 0
        for n in range (0, length):
            solved_poly += self.coexp[n][0] * x ** self.coexp[n][1]
        return solved_poly
    
    def evaluate (self, x):
        polynomial_evaluate = Polynomial(self.coexp)
        evaluate_function = polynomial_evaluate(x)
        return evaluate_function
    
    def derivative (self):
        length = len(self.coexp)
        derivative_poly = []
        if len(self.coexp) == 1 and self.coexp[0][1] == 0:
            derivative_poly += [(0,0)]
        else: 
            for n in range (0,length):
                if self.coexp[n][1] != 0:
                    derivative_poly += [(self.coexp[n][0]*self.coexp[n][1],self.coexp[n][1] - 1)]
                elif self.coexp[n][1] == 0:
                    pass
        final_derivative_poly = Polynomial (derivative_poly)
        return final_derivative_poly
    
    def integral (self):
        length = len(self.coexp)
        integral_poly = []
        
        for n in range (0,length):
            if self.coexp[n][1] != 0:
                coeff = self.coexp[n][0]/self.coexp[n][1]
                coefficient = float("{:.2f}".format(coeff))
                exponent = self.coexp[n][1] + 1 
                integral_poly += [(coefficient, exponent)]
            if self.coexp[n][1] == 0:
                coeff = self.coexp[n][0]
                coefficient = float("{:.2f}".format(coeff))
                exponent = self.coexp[n][1] + 1 
                integral_poly += [(coefficient, exponent)]  
                
        final_integral_poly = Polynomial(integral_poly)
        return final_integral_poly
    
    def zeros (self, x, max_iterations):
        f = self.coexp
        f_poly = Polynomial(f)
        df = f_poly.derivative()
        x1 = x
        for n in range (0, max_iterations):
            fx1 = f_poly(x1)
            if abs(fx1) < 1e-8:
                print ('zero found after', n, 'iterations')
                return x1
            dfx1 = df(x1)
            if dfx1 == 0:
                print ('no solution')
                return None
            x1 = x1 - fx1/dfx1
        print ('Exceeded maximum iterations. No solution found')
        return None
    
