def odd_even(number):
    
    number = float(number)
    quotient = number/2
    quotient = int(quotient)
    if quotient * 2 == number:
        return True
    else:
        return False
    






###################################################

def digit_counter(number):
    
    counter = 0
    counter2 = 1
    answer = 0
    
    while True:
    
        if number >= 10**counter and number < 10**counter2:
            answer = answer + 1
            return answer
            
        elif number > 10**counter2:
            counter = counter + 1
            counter2 = counter2 + 1
            answer = answer + 1
        



####################################################


def digit_add(number): 
    total = 0
   
    while number >= 1:
        total = total + (number % 10)
        number = number/10
    
   
    
    return total
    
    
     
    
    
    
    
    
    
    
        
        
    

    
    


###########################################################

def add_less_than(number):
    
    sum = 0
    counter = 1
    numero = 1
    
    while numero > 0:
        numero = (number - counter)
        sum = sum + numero
        counter = counter + 1
        
        
    return sum
        
    












##################################################

def factorial_finder(number):
    counter = number

    final = 0
    
    while counter > 0:
        
        final = 1
        
        final = final * number
        number = number - 1
        counter =  counter - 1
    
    return final














#################################

def factor_finder(number,numero):
    number = float(number)
    numero = float(numero)
    
    answer = number/numero
    answer = int(answer)
    
    if answer * numero == number:
        return True
    else:
        return False
    
    
    

############################################################

def prime_finder(number):

    falseMessage = "Enter a number GREATER than 2"
    
    number = float(number)
    if number < 2:
        return falseMessage
    
    divisor = 2
    
    while True:
        quotient = number/divisor
        
        quotient = int(quotient)
        
          
        if divisor == number:
            return True
        
        
        elif quotient * divisor == number:
            return False
        
       
        
        divisor = divisor + 1
        
        
    
###################################################################


def is_perfect(number):
    
    divisor = 2
    quotient = 2
        
    total = 0
        
    while quotient >= 1:
            
        quotient = number/divisor
            
        if quotient * divisor == number:
                    
            total = total + quotient
        else:
            total = total
            
        divisor = divisor + 1
        
    if total == 0:
        return False 
    
    elif total == number:
        return True
    
    
    else:
        return False
                
        
     
            
            
            









######################################################################

def digit_add_divisor(number):
    
    numero = digit_add(number)
    
    
    
    
    quotient = number/numero
    
    final = quotient * numero
    
    if final == number:
        return True
    else:
        return False
    
    
    
    




     
        
        
        
        





























    



