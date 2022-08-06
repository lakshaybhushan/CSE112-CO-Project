import sys
# import matplotlib.pyplot as plt
def binDec(n):
    x=str(n)
    fin=0
    base=1
    lenx = len(x)
    for i in range(lenx-1,-1,-1):
        if (x[i] == '1'):
            fin+=base
        base=base*2
    return fin

regdict={"000":0,"001":0,"010":0,"011":0,"100":0,"101":0,"110":0}

flagdict={"V":0,"L":0,"G":0,"E":0}

vardict={}

# opdict={"10000":"add","10001":"sub","10110":"mul","11010":"xor","11011":"or","11100":"and","11001":"ls","11000":"rs","11101":"not","11110":"cmp","10111":"div","10100":"ld","10101":"st","11111":"jmp","01100":"jlt","01101":"jgt","01111":"je","01010":"hlt","10010":"mov_imm","10011":"mov_reg"}

instruct = sys.stdin.readlines()
ins = []
for i in instruct:
    ele  = i.split()
    ins.append(ele)

# filename=("inputfile.txt")
# f=open(filename,'r')
# instruct=f.readlines()
# ins=[]
# for op in instruct:
#     temp=op.split()
#     ins.append(temp)
sentence=0
testcount=0
while sentence<len(instruct):
    testcount+=1
    sentence+=1
counter=0
print(testcount, len(instruct))
sentence=0
while sentence<len(instruct):
    opcode=str(instruct[sentence][0:5])
    if opcode=="10000":     #ADD
        r1=str(instruct[sentence][7:10])
        r2=str(instruct[sentence][10:13])
        r3=str(instruct[sentence][13:16])
        regdict[r3]=regdict[r2]+regdict[r1]
        if regdict[r3]>65535:
            flagdict["V"]=1
            regdict[r3]=regdict[r3]-65536
        else:
            flagdict={"V":0,"L":0,"G":0,"E":0}
    elif opcode=="10001":   #SUB
        r1=str(instruct[sentence][7:10])
        r2=str(instruct[sentence][10:13])
        r3=str(instruct[sentence][13:16])
        if regdict[r2]>regdict[r1]:
            flagdict["V"]=1
            regdict[r3]=0
        else:
            regdict[r3]=regdict[r1]-regdict[r2]
            flagdict={"V":0,"L":0,"G":0,"E":0}
    elif opcode=="10110":   #MUL
        r1=str(instruct[sentence][7:10])
        r2=str(instruct[sentence][10:13])
        r3=str(instruct[sentence][13:16])
        regdict[r3]=regdict[r1]*regdict[r2]
        if regdict[r3]>65535:
            flagdict["V"]=1
            regdict[r3]=regdict[r3]-65536
        else:
            flagdict={"V":0,"L":0,"G":0,"E":0}
    elif opcode=="10110":   #XOR
        r1=str(instruct[sentence][7:10])
        r2=str(instruct[sentence][10:13])
        r3=str(instruct[sentence][13:16])
        regdict[r3]=regdict[r1]^regdict[r2]
        flagdict={"V":0,"L":0,"G":0,"E":0}
    elif opcode=="11011":   #OR
        r1=str(instruct[sentence][7:10])
        r2=str(instruct[sentence][10:13])
        r3=str(instruct[sentence][13:16])
        regdict[r3]=regdict[r1]|regdict[r2]
        flagdict={"V":0,"L":0,"G":0,"E":0}
    elif opcode=="11100":   #AND
        r1=str(instruct[sentence][7:10])
        r2=str(instruct[sentence][10:13])
        r3=str(instruct[sentence][13:16])
        regdict[r3]=regdict[r1]&regdict[r2]
        flagdict={"V":0,"L":0,"G":0,"E":0}


#End of type A


    elif opcode=="11101":   #NOT
        r1=str(instruct[sentence][10:13])
        r2=str(instruct[sentence][13:16])
        regdict[r2]=~regdict[r1]
        flagdict={"V":0,"L":0,"G":0,"E":0}
    elif opcode=="11110":   #CMP
        flagdict={"V":0,"L":0,"G":0,"E":0}
        r1=str(instruct[sentence][10:13])
        r2=str(instruct[sentence][13:16])
        if r1==r2:
            flagdict["E"]=1
        elif r1<r2:
            flagdict["G"]=1
        else:
            flagdict["L"]=1
    elif opcode=="10111":   #DIV
        r1=str(instruct[sentence][10:13])
        r2=str(instruct[sentence][13:16])
        regdict["000"]=regdict[r1]//regdict[r2]
        regdict["001"]=regdict[r1]%regdict[r2]
        flagdict={"V":0,"L":0,"G":0,"E":0}
    elif opcode=="10011": #MOV_REG
        r1=str(instruct[sentence][10:13])
        r2=str(instruct[sentence][13:16])
        if r1!=111:
            regdict[r2]=regdict[r1]
        else:
            temp=8*flagdict["V"]+4*flagdict["L"]+2*flagdict["G"]+flagdict["E"]
            regdict[r2]=temp
        flagdict={"V":0,"L":0,"G":0,"E":0}


#End of Type C


    elif opcode=="10100":   #LOAD
        r1=str(instruct[sentence][5:8])
        var=str(instruct[sentence][8:16])
        if var not in vardict:
            r1=0
        else:
            r1=vardict[var]
        flagdict={"V":0,"L":0,"G":0,"E":0}
    elif opcode=="10101":   #ST
        r1=str(instruct[sentence][5:8])
        var=str(instruct[sentence][8:16])
        vardict[var]=r1
        flagdict={"V":0,"L":0,"G":0,"E":0}
    

#End of Type D


    elif opcode=="11000":   #RS
        r1=str(instruct[sentence][5:8])
        val=str(instruct[sentence][8:16])
        val=int(val)
        val=binDec(val)
        regdict[r1]=regdict[r1]>>val
        flagdict={"V":0,"L":0,"G":0,"E":0}
    elif opcode=="11001":   #LS
        r1=str(instruct[sentence][5:8])
        val=str(instruct[sentence][8:16])
        val=int(val)
        val=binDec(val)
        regdict[r2]=regdict[r1]<<val
        flagdict={"V":0,"L":0,"G":0,"E":0}
    elif opcode=="10010":   #MOV_IMM
        r1=str(instruct[sentence][5:8])
        val=str(instruct[sentence][8:16])
        val=int(val)
        val=binDec(val)
        regdict[r1]=val
        flagdict={"V":0,"L":0,"G":0,"E":0}


#End of Type B


    elif opcode=="11111":   #JUMP
        addr=str(instruct[sentence][8:16])
        addr=int(addr)
        addr=binDec(addr)
        sentence=addr
        flagdict={"V":0,"L":0,"G":0,"E":0}
    elif opcode=="01101":   #JGT
        addr=str(instruct[sentence][8:16])
        addr=int(addr)
        addr=binDec(addr)
        if flagdict["G"]==1:
            sentence=addr
        flagdict={"V":0,"L":0,"G":0,"E":0}
    elif opcode=="01100":   #JLT
        addr=str(instruct[sentence][8:16])
        addr=int(addr)
        addr=binDec(addr)
        if flagdict["L"]==1:
            sentence=addr
        flagdict={"V":0,"L":0,"G":0,"E":0}


#End of Type E


    # elif opcode=="01010":   #HLT
    #     break

    sentence+=1
    bincount=bin(counter)
    bincount=bincount[2:]
    bincount=int(bincount)
    lenbin=len(str(bincount))
    zeroes=8-lenbin
    zero=0
    while zero<zeroes:
        print("0", end="")
        zero+=1
    print(bincount,end=" ")
    counter+=1
    for i in regdict:
        out=regdict[i]
        binout=bin(out)
        binout=binout[2:]
        binout=int(binout)
        lenbin=len(str(binout))
        zeroes=16-lenbin
        zero=0
        while zero<zeroes:
            print("0",end="")
            zero+=1
        print(binout,end=" ")
    print("000000000000",end="")
    for i in flagdict:
        print(flagdict[i],end="")
    print("")
for i in ins:
    for j in i:
        print(j)
empty=256-counter
i=0
while i<empty:
    print("0000000000000000")
    i+=1

# x,y=zip(*info)
# plt.scatter(x,y)
# plt.savefig('ques4.png')
# for i in memory:
#     print(i)