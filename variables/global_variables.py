x = 'awesome'

def say():
    x = 'great'
    print('Python is: ', x)
    
say()
    
print('Python is: ', x)


# The gloabal keyword

def masterGlobal():
    global x 
    x = 'fantastic'
    print('Python is :', x)
    
masterGlobal()