# Defining a function
def palind(r):
    e = len(r) -1
    s = 0
    # While loop
    while(s<e):
        if (r[s] != r[e]):
            return False
        s += 1
        e -= 1
    return True

# Tuple
r =(1, 2, 3, 3, 2, 1)

# If condition
if(palind(r)):
    print("The tuple is FlipFlop !")
else:
    print("The tuple is not FlipFlop !")