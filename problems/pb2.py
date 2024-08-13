# declare and fill out function here

# test case
#print(max_values([-5, -2, -1, -11])) # -> [1, 2]

def max_values(values):
  a = values[0]
  for v in values:
      if v > a: 
          a = v
  b = values[0]        
  values.remove(a)  
  for n in values:
      if n > b: 
          b = n

  maxV = [a,b]
  return maxV