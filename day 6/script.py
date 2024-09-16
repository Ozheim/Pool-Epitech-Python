# task 1.1 

def f ( x ) :
    return 2 * x + 1
def g () :
    return 7
y = f (2)
print ( y )
y = f (5) + g ()
print ( y )

#task 1.2 

def bread () :
    return " <////////// > "
def lettuce () :
    return " ~~~~~~~~~~~~ "
def tomato () :
    return "O O O O O O"
def ham () :
    return " ============ "


def res(): 
    print(bread())
    print(lettuce())
    print(tomato())
    print(ham())
    print(ham())
    print(bread())


#task 1.3 

def multiple (): 
    for x in range (0,42):
        res()
        x+=1



#task 1.4 

#def numberOfSwandich(x): 
#    if x>=1:
#   for y in range(0,x):
#        res()
#    else: 
#       print("i can't do this")



#numberOfSwandich(5)


#Task 1.5 

def legume():
    return "LEGUUUUUUUUUUUUUUUUUME"

def vegetarianSwandich() : 
    print(bread())
    print(lettuce())
    print(tomato())
    print(legume())
    print(legume())
    print(bread())

def numberOfSwandich(x,v): 
    if v >= 1: 
        for y in range(0,x):
            vegetarianSwandich()
          
    else: 
        if x>=1:
            for y in range(0,x):
             res()
        else: 
            print("i can't do this")
numberOfSwandich(0,0)

#task 1.6 

#challenge: 
 
#x= 84 
#for i in range(0,x):
#    res = 42**x
#print(res)

#task 2.1
punctuation = '''!()-[]{};:'",<>./?@#$%^&*_~'''


def palindrome(mot): 
    mot= str(mot)
    mot= mot.lower()
    
    for lettre in mot :
        if lettre in punctuation:   
            mot= mot.replace(lettre,"")
        mot= mot.replace(" ", "")   
 
    print(mot)


palindrome("Ka /yak")