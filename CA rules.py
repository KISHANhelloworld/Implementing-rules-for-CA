import itertools

def XOR(p,q,r):
    if p!=r:
        return 1
    else:
        return 0

def NOT(p):
    if p == 1:
        return 0
    else:
        return 1

def R195(p,q,r): 
    
    return NOT(p)*NOT(q)+p*q

def R54(p,q,r):
    return NOT(p)*(r) + NOT(P)*NOT(q)+NOT(q)*NOT(r)
def R150(p,q,r):
    return XOR(p,q,r)











    a=NOT(q)
    return a

def R51(p,q,r):
    b=NOT(q)
    return b



def HashFunC(L,time,RV):
    j = 0
    IV1 = L[:]
    IV2 = []
    x = 0
    RV = False
    Rec = False
    IV = L[:]
    
    for j in range(1,time):
        if Rec == True:
            
            return j-1,IV
            break
        x = 0
        IV2.clear()
        for i in IV:
            if x == 0:
                a = 0
                b = i
                c = IV[x+1]
                
                IV2.append(R195(a,b,c))
                x = x+1
            else:
                if x == 7:
                    a = IV[x-1]
                    b = i
                    c = 0
                   
                    if RV == False:
                      
                        IV2.append(R51(a,b,c))
                    else:
                       
                        IV2.append(R195(a,b,c))
                    
                    if IV2 == IV1:
                        
                        
                        Rec = True
                        IV = IV2[:]
                        break
                    IV = IV2[:]
                    break
                else:
                    a = IV[x-1]
                    b = i
                    c = IV[x+1]
                    
                    if RV == False:
                        
                        IV2.append(R195(a,b,c))
                    else:

                        if x == 1:
                           
                            IV2.append(R195(a,b,c))
                        elif x == 2:
                           
                            IV2.append(R195(a,b,c))
                        elif x == 3:
                           
                            IV2.append(R54(a,b,c))
                        elif x == 4:
                            
                            IV2.append(R204(a,b,c))
                        elif x == 5:
                           
                            IV2.append(R51(a,b,c))
                        elif x == 6:
                           
                            IV2.append(R150(a,b,c))

                    x = x+1
    return j,IV

print(HashFunC([1,1,0,1,0,0,1,1],1000000,False))
