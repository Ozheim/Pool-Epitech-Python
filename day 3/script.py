#task  1.1 

string= "bigstringToWorkForAnyTask"

print(str)

#task 1.2

print(string[0])
print(string[5])

#task 1.3

print(string[-1])

#task 1.4

print(string[4:10])

#task 2.1 

strLowerCase = "StrUPPERCASE" 
print(strLowerCase.lower())  # la méthode lower() permet de passer de majuscule a minuscule 

#chr() ca sert a aller chercher les lettre directement 

#task 2.2

var = "tutu on the tuki-kata"

varReplaced = var.replace( "tutu", "taka")  # la méthode replace() permet de changer un text 

print(varReplaced)

#task 2.3 

strHello = " hello world "
position = strHello.find ("a")
print ( position )

# .find() permet de chercher avec précision une lettre dans ce cas , mais c'est probalement plus puissant que ca, si il ne la trouve pas il retourne -1

#task 2.4 

p = "abcdefghij"
print( p [:: -2]) #les  :: permettent de sauter un caractère sur deux sur toute la liste et les récuperer 
print(p [:5]) # les : permettent de prendre les 5 premiers d'une listes 
print(p [:: -1]) # je prend toute la liste en commencant par la fin 
print (p [3:]) # je prend toute la liste a partir du 3 ieme index de la liste 

# task 2.5 

pRes = "abcdefghij"

print(pRes [:: -2][:2])

#task 2.6

strTenTime = "abcdefghij"

for i in range( 0,11 ): 
    print(strTenTime)
    i += 1 


#task 2.7 

print(strTenTime*10)

#task 2.8 

s1 = " Hello "
s2 = str(42)
concat = s1 + s2
print ( concat )

#task 2.9 

string1 = " 42 "
string2 = "is"
string3 = " the answer "
concat = string1 + string2 + string3 
print (" The string " +  concat  + " contain 16 characters.")

#challenge before 3.1 : 

snippet = "thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN"
snippetLower = snippet.lower();
print(snippetLower.count("cat"))
print(snippetLower.count("mice"))
print(snippetLower.count("garden"))
snippedReversed = snippetLower
print(snippedReversed)

#task 3.1
username = input("what's your name ?")
print("hello" ,username)

#task 3.2 

usernameBis = input("what's your name ?")
print("hello" ,usernameBis[0].capitalize()+ usernameBis[1:])

#task 3.3

userNameNumOne = input("give me 2 numbers, first one please : ")
userNameNumBis= input("second One please : ")

print( "The sum of the two provided numbers is", int(userNameNumOne) + int(userNameNumBis))

#task 3.4 

Question = input("give me a number please :")
print(type(int(Question)))

