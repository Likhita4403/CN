def stuff_code(x , frame):
    d=[]
    stuff=[]
    count =0 
    l=""
    for i in range(len(x)):
        if len(l)==frame:
            d.append(l)
            l=""
        l+=x[i]
    if len(l)!=0:
        d.append(l)
    print("number of frames:" , len(d))
    print("user data framed", d)
    
    new_word=""
    for word in d:
        for j in word:
            new_word+=j
            if j=='1':
                count+=1
                if count==5:
                    new_word+='0'
                    count=0
            else:
                count=0
        new_word="01111110"+"".join(new_word) + "01111110"
        stuff.append(new_word)
        
        new_word=""
    for i in range(len(stuff)):
            print("frame" , i + 1 , end = " ")
            print(stuff[i])
    return "".join(stuff)
def removeFlag(x):
    x=x[8:]
    x=x[:-8]
    d=x.split("0111111001111110")
    # print(d)
    return d

def destuff_code(x):
    l=[]
    count=0
    for word in x:
        j=0
        new_word=""
        while( j< len(word)):
            if word[j]=='1':
                count+=1
                j+=1
                if count==5:
                    j+=1
                    count=0
                new_word+='1'
            else:
                j+=1
                new_word+='0'
                count=0
        l.append(new_word)
    return l
x="011111100"
print("user data", x)
frame = int(input("enter frame size"))
#change code such that flag bits are considered
print("sender's message on stuffing:")
d=stuff_code(x , frame)

print("receiver's side:")
d=stuff_code(x , frame)
x=removeFlag(d)
print("on removing flags",x)
print("destuffed data",destuff_code(x))
        
            

