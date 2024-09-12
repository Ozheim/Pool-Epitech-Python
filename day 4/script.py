# task 1.2 

askingQuestion = int(input("give me an integer please :" ))
if  askingQuestion  == 42 : 
    print("Correct answer")
else :
    print("no")

#task 1.3 

AskingOddOrEven = int(input("give me an integer please: " ))
if AskingOddOrEven%2 == 0 : 
    print("even")
else:
    print("odd")

#task 1.4

AskingOpenSesame = str(input("You are front of the door, do something : "))
if AskingOpenSesame == "open sesame" or AskingOpenSesame  == "Open sesame" or AskingOpenSesame == "Open Sesame" or AskingOpenSesame == "opensesame" : 
    print("acces guarranted")
elif AskingOpenSesame == "will you open, you goddamn fuckk, display access fucking granted" :
    print("access fucking granted")
else: 
    print("permission denied")

#task 1.5 

AskingFinalInteger = int(input("hello, integer : "))
if AskingFinalInteger == 42: 
    print("ok")
elif AskingFinalInteger <= 21 :
    print("ok")
elif AskingFinalInteger%2 == 0 : 
    print("ok")
elif AskingFinalInteger%2 and AskingFinalInteger < 21 : 
    print("Ok")
elif AskingFinalInteger%2 != 0 and AskingFinalInteger >= 45 : 
    print("ok")
else: 
    print("You got wrong my poor friend!")

#task 1.6 

a = 42
b = 41
if  a == b :
    print("A and B are the sames ")
if  b <= a :
    print("B is equal or lower as A")
if b != a:
    print("B his different from A")

# task 2.1 

#for num in range ( 0, 1000): 
#   num +=1 
#   print(num)

#task 2.2

askingAString = str(input("hey, give me a word please: ")) 
res =""
for string in askingAString :
    res+= string*2 
print(res)

#task 2.3 


count = 0

for count in range ( 1,10000): 
   if count %7 == 0 : 
    print("ces numéro sont divisble par 7 : ", count ) 
    count +=1 

 #task 2.4 

cnt = 0

for cnt in range (-30, 30 ): 

    if cnt% 3 == 0 : 
        print("fizz")
        
    elif cnt%5 == 0: 
        print("buzz")


    elif cnt%5 == 0 and cnt%3==0 : 
        print("FizzBuzz")
    else: 
        print(cnt)
cnt += 1 

#task 2.5


for i in range ( 99, 0, -1) : 
    if(i==1):
        print( "{} bottle of beer on the wall., {}  bottle of beer. Take one down, pass it around, {}  bottle of beer on the wall.".format(i,i,i))
    else: 
        print( "{} bottles of beer on the wall., {}  bottles of beer. Take one down, pass it around, {}  bottles of beer on the wall.".format(i,i,i-1))


#task 2.6 

def functionForThis(trying, n):
    i=0
    while i < n : 
        if i <n :
           i += trying
        print(i)
       
        
        if i>n :
            ("bon")
        else:
            ("stop2")
    
    for i in range (0,n): 
        i = i +  1 

trying = int(input("test something : "))
n= int(input("give me ur max : "))
while trying * 2 < n:
    functionForThis(trying, n)   
    trying+=1


#challenge : 

def challenge():
    ask_int = int(input("Write nbr : "))
    ask_str = input("Write str : ")
    vowels = str(["a", "e", "i","o","u","y"])
    if ask_int == 0:
        exit(challenge())
    elif ask_int >= 42:
            print(ask_int)
    for vowel in vowels:
        if vowel in ask_str:
            print(ask_int)
       
    else : print(ask_str)
challenge()
 


#task 3.1 

inputEncrypted= str(input("your message:  "))
inputKey = str(input("you're key: "))

dictionnary = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

