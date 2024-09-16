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
 
    return print(mot == mot[::-1])


palindrome("never odd or even")

#task 3.1 

def funA(s,n):
    total = 0
    
    for letter in s: 
        total += letter.islower()
    if total >= n: 
        return True
    else:
        return False
    
#print(funA("sssss",2))

def funB(s,n):
    total = 0
    for letter in s: 
        total += letter.isupper()
    return total >= n
    
#print(funB("hello world", 2))

def funC(s,n):
    total = 0
    for letter in s: 
        total += len(letter)
    return total >= n

#print(funC("lalalal",5 ))


sp = "!@#$%^&*()-+?_=,<>"
def funD(s,n): 
    total =0
    for car in s: 
        if car in sp:
            total += 1
    return total>=n

#print( funD( "strin!", 2))

def funE(x,y):
    total = 0
    for number in x:
        total += number.isnumeric()
    if total >= y:
       return True
    else :
        return False

#print(funE("dsmsp8989", 4))



