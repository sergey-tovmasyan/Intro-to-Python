t2 = (2,75,"candy",84,3,21,"cake",2001)
print("Before changing:",t2)
t2 = list(t2)
t2[4] = "hello"
t2 = tuple(t2)
print("After changing:",t2)