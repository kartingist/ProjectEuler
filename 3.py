'''
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
'''

def one():
    res=[]
    x=600851475143
    z=2
    while z*z<=x:
        if x%z==0:
            res.append(z)
            z+=1
        else:
            z+=1
    return(res)
def two():
    count=0
    res2=[]
    for i in one():
        for j in range(1, i+1):
            if i%j==0:
                count+=1
                if count>2:
                    count=0
                    break
                elif i==j and count==2:
                    res2.append(i)
                    count=0
    print (max(res2))



two()