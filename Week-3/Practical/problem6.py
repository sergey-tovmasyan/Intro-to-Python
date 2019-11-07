list5 = ["hi",42,True,12,"yes",89]
newlist = list5
print("list5:",list5)
print("newlist:",newlist)
del newlist[5]
del newlist[4]
del newlist[0] 
print("newlist after changes:",newlist)