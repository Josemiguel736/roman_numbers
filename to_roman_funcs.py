symbols={1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",5:"V",4:"IV",1:"I"}

def to_roman(n):
    result=""
    new_n=n
        
    while new_n!=0 or new_n <0:
        for key in symbols:
           if key<=new_n:
            result+=symbols[key]
            new_n-=key
            break

    return result 

def to_arabigo(roman):
   result=0
   last_key=0
   for letter in roman:
      for key in symbols:
         if letter==symbols[key]:             
             result+=key
             if key>last_key:
                result-=last_key*2
             last_key=key
           
   return result




         
