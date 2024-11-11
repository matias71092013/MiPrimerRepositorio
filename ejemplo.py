import random

for i in range(1000):
    def random_sum():
    numero1 = random.randint(1,10)
    numero2 = random.randint(1,10)
    
    print("Numero 1: ",numero1)
    print("Numero 2: ",numero2)
    
    print("La suma es: " ,numero1 + numero2 )
    
random_sum()
def max_val (n1,n2):
    
    
    if n1 > n2:
        print ("Numero 1 es mas grande")
        
    else:
        print ("Numero 2 es mas grende")

def min_val (n1,n2):
    
    
    if n1 < n2:
        print ("Numero 1 es mas chico")
        
    else:
        print ("Numero 2 es mas chico")

def multiply (numero1,multiplicacion):
    print (numero1 * multiplicacion)
    

def divide(numero1, numero2):
    print(numero1 / numero2)
    
    
def divide_integer(numero1, numero2):
    print(numero1 // numero2) 
