#Task 1.1 

print(1+1);

print(30+12);

print(777+(-732));

print(1 + 2 + 3 + 5 + 7 + 11 + 13
);

#task 1.2

print(84-42)

print(0-(-42))

print(2*21)

print((3+(3*4-2*2)*3-2)*2-3)

#task 1.3

print(6//2) #division des entiers 
print(6/2)

#task 1.4

#print(84/(8+(-3)+(-7)+2)) #division par zero error 


#task 2.1

res= 0

i = 1
while i < 10:
    res += int('1'*i)
    i = i + 1
    print(res)

res = 0

for i in range(1,10):
    
    res += int('1'*i)

print(res)

#task  2.2

print(17**1024)

#task 3.1

print(42%4);


#task 3.2

num= 4255876886275287624248585

if num%2 == 0 :
    print("odd")
else: 
    print("even")

#task 3.3

firstListOfNumber = 123434565;
secondListOfNumber = 345567426;
lastLisstOfNumber = 44490320097;

sum = 0 

for num in str(firstListOfNumber): 
    sum += int(num)
print(sum)
    

sum= 0 

for num in str(secondListOfNumber): 
    sum += int(num)
print(sum)

sum= 0 

for num in str(lastLisstOfNumber): 
    sum += int(num)
print(sum)

#task 3.4

numberOne = 12.24;
lastNumber= 424242.8412;

res= numberOne - int(numberOne)
print(res)

secondRes= lastNumber-int(lastNumber);
print(secondRes);   

#challenge: Rewrite the previous task with the least possible number of characters.

#print(round(res,2)); 
#print(round(secondRes,2));
print(format(res,('.2f')));
print(format(secondRes,(".2f")));

#task 4.1

precision = 1
for _ in range(30):
    print(1/precision)
    precision += 2

pi = π = 4 * (1/1 - 1/3 + 1/5 - 1/7+1/9);

print(format(pi,(".2f")));

#task 4.1


