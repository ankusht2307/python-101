# Basic loop

for i in range(5):
    print(i)
print('=======')

for i in range(0, 5):
    print(i)
print('=======')

# Loop with step(skip)
for i in range(0, 10, 2):
    print(i)
print('=======')

# Loop backwards
for i in range(10, 0, -1):
    print(i)
    
print('=======')
    
# traverse through string
str = "Jhon Doe"

for i in str:
    print(i)    
print('========')

# Loop with control statements

for i in range(10):
    if i == 5:
        break
    print(i)    
print('========')

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
print('========')
    
for i in range(10):
    if i == 2:
        pass # pass is null operation, it does nothing
    print(i)
