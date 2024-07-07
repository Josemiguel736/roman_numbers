valors = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}


def to_roman(n):
     
    result=""
    while n!=0:
      order, d = calc_d_order(n)
      if d <= 3:
          result+= d * valors[order]
          n=n-d*order
      elif d == 4:
          result+= valors[order] + valors[5*order]
          n=n-d*order
      elif d < 9:
         result+= valors[5*order] + (d - 5) * valors[order]
         n=n-d*order
      elif d == 9:
          result += valors[order] + valors[10*order]
          n=n-d*order

    return result


def calc_d_order(n):
    order = 10**(len(str(n))-1)
    d = n//order
    return order, d





def divide_miles(n):
    lista=[]
    entero=n//1000
    modulo=n%1000
    if entero>1000:
       n=entero
       lista.append(modulo)   
       while entero>1000:     
        entero=n//1000
        modulo=n%1000
        if entero>1000:
           n=entero
           lista.append(modulo)
        elif entero<4:
           lista.append(n)
        else:
           lista.append(modulo)    
           lista.append(entero)
    elif entero<4:
      lista.append(n)
    else:
       lista.append(modulo)    
       lista.append(entero) 
   
   
    return lista




def roman_mil(n):
   roman=[]
   count=0
   resultado=""
   for n in divide_miles(n):
      if n!=0:
         roman.append(to_roman(n)+"*"*count)
      count+=1
   romani=reversed(roman)
   for r in list(romani):
      resultado+=r


   return resultado

print(roman_mil(4))
