# program to print fibonacci numbers by using loops
print('The fibonacci series')
n = int(input('enter the number of terms : '))
x = 0
y = 1
print(x)
print(y)
for i in range (n):
    x , y = y , x+y
    print(y)
    
    
