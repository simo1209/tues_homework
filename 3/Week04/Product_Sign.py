def product_sign(a, b):
  if (a>0 and b>0):
    print ("+")
  elif (a>0 and b<0):
   print("-")
  elif (a<0 and b<0):
    print ("+")
  elif (a<0 and b>0):
   print ("-")
  
print (product_sign(1, -1))
print (product_sign(1, 1))
print (product_sign(-1, -1))
print (product_sign(-1, 1))
