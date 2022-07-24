import matplotlib.pyplot as mlt
import sys

register_dict={"000":'0000000000000000',"001":'0000000000000000',"010":'0000000000000000',"011":'0000000000000000',"100":'0000000000000000',"101":'0000000000000000',"110":'0000000000000000',"111":'0000000000000000'}

files=open('inputfile.txt','w')
files.truncate(0)
for line in sys.stdin:
    files.write(line)
files.close()
files=open('inputfile.txt','r')
f=files.read().splitlines()
for i in range(0,len(f)-1):
    if(f[i][-1]=='\n'):
        f[i]=f[i][0:-1]



memory = ['0000000000000000' for i in range(256)]
for i in range(0,len(f)):
    if f[i]!= '0000000000000000':
        memory[i]=f[i]

PC=0
cycle=0
data=[]

halt=False

def bintodec(binary):
    g=int(binary,2)
    return (g)

def dectobin(dec):
    j=bin(dec)[2:]
    while len(j)<16:
        j='0'+j
    return j




while(not halt):
    
    a=memory[PC]
    data.append([cycle,PC])
    

    if a[:5]=='00000':
        register_dict['111']='0000000000000000'
        sum=bintodec(register_dict[a[10:13]])+bintodec(register_dict[a[13:16]])
        binsum=dectobin(sum)
        if len(binsum)>16:
            binsum=binsum[-16:]
            register_dict['111']='0000000000001000'
        register_dict[a[7:10]]=binsum
        PC=bin(PC)[2:]
        while len(PC)<8:
            PC='0'+PC
        print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
        PC=bintodec(PC)
        PC=PC+1
        cycle=cycle+1

    elif a[:5]=='00001':
        register_dict['111']='0000000000000000'
        if bintodec(register_dict[a[13:16]]) > bintodec(register_dict[a[10:13]]):
            register_dict[a[7:10]]='0000000000000000'
            register_dict['111']='0000000000001000'
            PC=bin(PC)[2:]
            while len(PC)<8:
                PC='0'+PC
            print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
            PC=bintodec(PC)
            PC=PC+1
            cycle=cycle+1
        else:
            diff=bintodec(register_dict[a[10:13]])+bintodec(register_dict[a[13:16]])
            register_dict[a[7:10]]=dectobin(diff)
            PC=bin(PC)[2:]
            while len(PC)<8:
                PC='0'+PC
            print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
            PC=bintodec(PC)
            PC=PC+1
            cycle=cycle+1

    elif a[:5]=='00010':
        register_dict['111']='0000000000000000'
        register_dict[a[5:8]]='00000000'+a[8:16]
        PC=bin(PC)[2:]
        while len(PC)<8:
            PC='0'+PC
        print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
        PC=bintodec(PC)
        PC=PC+1
        cycle=cycle+1
    
    elif a[:5]=='00011':
        register_dict[a[10:13]]=register_dict[a[13:16]]
        register_dict['111']='0000000000000000'
        PC=bin(PC)[2:]
        while len(PC)<8:
            PC='0'+PC
        print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
        PC=bintodec(PC)
        PC=PC+1
        cycle=cycle+1
        

    elif a[:5]=='00100':
        data.append([cycle,int(a[-8:],2)])
        register_dict['111']='0000000000000000'
        register_dict[a[5:8]]=memory[int(a[-8:],2)]
        PC=bin(PC)[2:]
        while len(PC)<8:
            PC='0'+PC
        print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
        PC=bintodec(PC)
        PC=PC+1
        cycle=cycle+1

    elif a[:5]=='00101':
        data.append([cycle,int(a[-8:],2)])
        register_dict['111']='0000000000000000'
        memory[int(a[-8:],2)]=register_dict[a[5:8]]
        PC=bin(PC)[2:]
        while len(PC)<8:
            PC='0'+PC
        print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
        PC=bintodec(PC)
        PC=PC+1
        cycle=cycle+1

    elif a[:5]=='00110':
        register_dict['111']='0000000000000000'
        mul=bintodec(a[10:13])*bintodec(a[13:16])
        binmul=dectobin(mul)
        if len(binmul)>16:
            binmul=binmul[-16:]
            register_dict['111']='0000000000001000'
        register_dict[a[7:10]]=binmul
        PC=bin(PC)[2:]
        while len(PC)<8:
            PC='0'+PC
        print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
        PC=bintodec(PC)
        PC=PC+1
        cycle=cycle+1

    elif a[:5]=='00111':
        register_dict['111']='0000000000000000'
        register_dict['000']=bintodec(a[10:13])//bintodec(a[13:16])
        register_dict['001']=bintodec(a[10:13])%bintodec(a[13:16])
        PC=bin(PC)[2:]
        while len(PC)<8:
            PC='0'+PC
        print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
        PC=bintodec(PC)
        PC=PC+1
        cycle=cycle+1

    elif a[:5]=='01000':
        register_dict['111']='0000000000000000'
        rs=bintodec(register_dict[a[5:8]])>>int(a[8:],2)
        register_dict[a[5:8]]=dectobin(rs)
        PC=bin(PC)[2:]
        while len(PC)<8:
            PC='0'+PC
        print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
        PC=bintodec(PC)
        PC=PC+1
        cycle=cycle+1

    elif a[:5]=='01001':
        register_dict['111']='0000000000000000'
        ls=bintodec(register_dict[a[5:8]])<<int(a[8:],2)
        register_dict[a[5:8]]=dectobin(ls)
        PC=bin(PC)[2:]
        while len(PC)<8:
            PC='0'+PC
        print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
        PC=bintodec(PC)
        PC=PC+1
        cycle=cycle+1

    elif a[:5]=='01010':
        register_dict['111']='0000000000000000'
        x=(bintodec(a[10:13]))^(bintodec(a[13:]))
        register_dict[a[7:10]]=dectobin(x)
        PC=bin(PC)[2:]
        while len(PC)<8:
            PC='0'+PC
        print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
        PC=bintodec(PC)
        PC=PC+1
        cycle=cycle+1

    elif a[:5]=='01011':
        register_dict['111']='0000000000000000'
        o=(bintodec(a[10:13]))|(bintodec(a[13:]))
        register_dict[a[7:10]]=dectobin(o)
        PC=bin(PC)[2:]
        while len(PC)<8:
            PC='0'+PC
        print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
        PC=bintodec(PC)
        PC=PC+1
        cycle=cycle+1

    elif a[:5]=='01100':
        register_dict['111']='0000000000000000'
        an=(bintodec(a[10:13]))&(bintodec(a[13:]))
        register_dict[a[7:10]]=dectobin(an)
        PC=bin(PC)[2:]
        while len(PC)<8:
            PC='0'+PC
        print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
        PC=bintodec(PC)
        PC=PC+1
        cycle=cycle+1

    elif a[:5]=='01101':
        register_dict['111']='0000000000000000'
        inv=~(bintodec(a[13:]))
        register_dict[a[10:13]]=dectobin(inv)
        PC=bin(PC)[2:]
        while len(PC)<8:
            PC='0'+PC
        print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
        PC=bintodec(PC)
        PC=PC+1
        cycle=cycle+1

    elif a[:5]=='01110':
        r1=bintodec(register_dict[a[10:13]])
        r2=bintodec(register_dict[a[13:16]])
        if r1>r2:
            register_dict['111']='0000000000000010'
        elif r1<r2:
            register_dict['111']='0000000000000100'
        elif r1==r2:
            register_dict['111']='0000000000000001'
        PC=bin(PC)[2:]
        while len(PC)<8:
            PC='0'+PC
        print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
        PC=bintodec(PC)
        PC=PC+1
        cycle=cycle+1

    elif a[:5]=='01111':
        register_dict['111']='0000000000000000'
        PC=bin(PC)[2:]
        while len(PC)<8:
            PC='0'+PC
        print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
        PC=bintodec(PC)
        PC=bintodec(a[8:])
        cycle=cycle+1

    elif a[:5]=='10000':
        valueflag=register_dict['111']
        register_dict['111']='0000000000000000'
        PC=bin(PC)[2:]
        while len(PC)<8:
            PC='0'+PC
        print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
        PC=bintodec(PC)
        if valueflag[13:14]=='1':
            
            PC=bintodec(a[8:])
        else:
            PC=PC+1
        cycle=cycle+1

    elif a[:5]=='10001':
        valueflag=register_dict['111']
        register_dict['111']='0000000000000000'
        PC=bin(PC)[2:]
        while len(PC)<8:
            PC='0'+PC
        print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
        PC=bintodec(PC)
        if valueflag[14:15]=='1':
            PC=bintodec(a[8:])
        else:
            PC=PC+1
        cycle=cycle+1

    elif a[:5]=='10010':
        valueflag=register_dict['111']
        register_dict['111']='0000000000000000'
        PC=bin(PC)[2:]
        while len(PC)<8:
            PC='0'+PC
        print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
        PC=bintodec(PC)
        if valueflag[15:]=='1':
            PC=bintodec(a[8:])
        else:
            PC=PC+1
        cycle=cycle+1

    elif a[:5]=='10011':
        register_dict['111']='0000000000000000'
        PC=bin(PC)[2:]
        while len(PC)<8:
            PC='0'+PC
        print(PC+" "+register_dict['000']+" "+register_dict['001']+" "+register_dict['010']+" "+register_dict['011']+" "+register_dict['100']+" "+register_dict['101']+" "+register_dict['110']+" "+register_dict['111'])
        PC=bintodec(PC)
        halt=True



x,y=zip(*data)
mlt.scatter(x,y)
mlt.savefig('bonus.png')
for i in memory:
    print(i)