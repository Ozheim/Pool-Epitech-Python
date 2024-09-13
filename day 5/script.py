# task 1.1  

list=[1,2,3,4,5,6] 

print(list[0])

#task 1.2 

print(list[3])

#task 1.4

print(list)

#task 1.5 

del(list[-1])

#task 1.6 

list.insert(0,0)
print(list)

#task 1.7

print(list[1:5])

#task 1.8 

newList= list[::-1]
print(newList)

#task 1.9

print(list[::2])

#task 1.10 

list[7:] = 7,8,9,10,11,12,13,14,15,16,17,18

print(list)

# task 1.11

my_first_list = [4 , 5 , 6]
my_second_list = [1 , 2 , 3]
my_first_list . extend ( my_second_list )

print(my_first_list)    

my_first_list = [7 , 8 , 9]
my_second_list = [4 , 5 , 6]
my_first_list = [* my_first_list , * my_second_list ]

print(my_first_list) #the both code do the same thing

#task 2.1

listOfTen = [1,2,3,4,5,6,7,8,9,10]
r= 1 
for element in listOfTen: 
    
    r*= element

print(r)

#task 2.2 

print([x + 10 for x in [3, 2, 6, 7, 1, 4]]) #ca ajoute la dizaine a chaque element


# task 2.3 

#print(list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4])))

#task 2.4

print(max(list))
print(min(list))

#task 2.5 

print(list[0:7])

#task 2.6 


list.sort(reverse=True)
print(list)

#task 2.7 

t= [x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]] # ca divise par deux si x est pair sinon ca multiplie par 2 
print(t)

#task 2.8

#y= list(filter(lambda x: x > 10, [42, 3, 4, 18, 3, 10])) # ca parcours toute la liste et retourne ce qui est strictement supérieur a 10 
#print(y)


#task 2.9 


print([*enumerate([42, 3, 4, 18, 3, 10])]) # ca ajoute un compteur qui commence a 0 dans ce cas et permet de de compter chaaque index ( chiffre a gauche dans le print)

#task 3.1 

student = {
  "key": "heikel",
  "values": "Epitech",
  "units": [
    {
      "name": "Web Development",
      "credits": 2,
      "grade": "A"
    },
    {
      "name": "Network and System Administration",
      "credits": 3,
      "grade": "B"
    },
    {
      "name": "Java",
      "credits": 4,
      "grade": "C"
    } 
  ],
}

print(student["units"][0]["grade"])
    
x= 0
for unit in student["units"]:
    x+= unit["credits"]
    totalCredit = x 
    student["total_credit"] = totalCredit
print(student)


#task 3.3 

grade_weight_mapping=[
    {"key":"A", "values": 4 },
    {"key": "B", "Values": 3},
    {"key": "C", "values": 2},
    {"key": "D", "values": 1},
    {"key":"E", "values": 0}
]

student["GPA"]= 9/3

print(student["units"][0]["grade"])

#task 3.4 

arrayOfStudent = [
    {"name": "Amine", "credits": 5 , "grade": "D"},
    {"name": "Colin", "credits": 6, "grade": "E"},
    {"name": "Mohammed", "credits": 7, "grade": "B"}
]
        
    
    
