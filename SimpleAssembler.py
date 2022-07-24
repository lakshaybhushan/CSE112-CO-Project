import sys
dict_op={"add":0, "sub":0,"xor":0, "or":0,"and":0,"mul":0,"mov":6,"rs":1,"ls":1,"div":2,"not":2,"cmp":2,"ld":3,"st":3,"jmp":4,"jlt":4, "jgt":4, "je":4, "hlt":5}

dict_reg={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}

type_a={"add":"10000","sub":"10001","mul":"10110","xor":"11010","or":"11011","and":"11100"}

type_b={"ls":"11001","rs":"11000"}

type_c={"not":"11101","cmp":"11110","div":"10111"}

type_d={"ld":"10100","st":"10101"}

type_e={"jmp":"11111","jlt":"01100","jgt":"01101","je":"01111"}

type_f={"hlt":"01010"}

type_mov={"mov_imm":"100010","mov_reg":"10011"}

binlist=[type_a, type_b, type_c, type_d, type_e, type_f, type_mov]



# S = sys.stdin.read()
# line = S.split("\n")
# ins = []
# for i in line:
#     ele  = i.split()
#     ins.append(ele)
ins=[]
filename=("output.txt")
f=open(filename,'r')
instruct=f.readlines()
for op in instruct:
    temp=op.split()
    ins.append(temp)
count=0
finout=[]
hltcount=0
vardict={}
for sentence in ins:
    if len(sentence)==0:
        continue
    elif sentence[0]!="var": #error line
            count+=1
count=bin(count)
count=count[2:]
count=int(count)
varcount=0
for sentence in ins:
    tempout=str()
    if len(sentence)!=0 and sentence[0]=="var":
        tempvar=sentence[1]
        if len(vardict)==0:
            vardict[tempvar]=count
            varcount=1
        else:
            decimal = 0
            count=str(count)
            for digit in count:
                decimal = decimal*2 + int(digit)
            count=decimal+varcount
            count=bin(count)
            count=count[2:]
            count=int(count)
            vardict[tempvar]=count
    else:
        break
labeldict={}
labelcount=0
sencount=0
for sentence in ins:
    if len(sentence)!=0:
        labeltemp=sentence[0]
    if labeltemp[-1]==":":
        labeltemp=labeltemp[:-1]
        labelbin=bin(labelcount)
        labelbin=labelbin[2:]
        labelbin=int(labelbin)
        lenlabel=len(str(labelbin))
        zeroes=8-lenlabel
        zero=0
        labelcount2=str()
        while zero<zeroes:
            labelcount2+=str("0")
            zero+=1
        labelcount2+=str(labelbin)
        labeldict[labeltemp]=labelcount2
    if len(sentence)!=0 and sentence[0]!="var":
        labelcount+=1
for sentence in ins:
    sencount+=1
    if hltcount==1 and sentence!=None:
        print("Error: hlt is not the last instruction")
        quit()
    for keyw in dict_op:
        count+=1
        senlen=len(sentence)
        word=0
        while word<senlen:
            if sentence[word]==keyw:
                index=dict_op[keyw]
                for binfind in binlist[index]:
                    if binfind==sentence[word]:
                        tempout=(binlist[index][binfind])
                if index==0:
                    tempout+=str("00")
                    word+=1
                    for reg in dict_reg:
                        if reg==sentence[word]:
                            if reg=="FLAGS":
                                print("Error in line:",sencount,", Flag is used as Register")
                                quit()
                            tempout+=str(dict_reg[reg])
                            word+=1
                            break
                        if sentence[word] not in dict_reg:
                            print("Error in line:",sencount,", Register Error")
                            quit()
                    for reg in dict_reg:
                        if reg==sentence[word]:
                            if reg=="FLAGS":
                                print("Error in line:",sencount,", Flag is used as Register")
                                quit()
                            tempout+=str(dict_reg[reg])
                            word+=1
                            break
                        if sentence[word] not in dict_reg:
                            print("Error in line:",sencount,", Register Error")
                            quit()
                    for reg in dict_reg:
                        if reg==sentence[word]:
                            if reg=="FLAGS":
                                print("Error in line:",sencount,", Flag is used as Register")
                                quit()
                            tempout+=str(dict_reg[reg])
                            break
                        if sentence[word] not in dict_reg:
                            print("Error in line:",sencount,", Register Error")
                            quit()
                    finout.append(tempout)
                elif index==1:
                    word+=1
                    for reg in dict_reg:
                        if reg==sentence[word]:
                            if reg=="FLAGS":
                                print("Error in line:",sencount,", Flag is used as Register")
                                quit()
                            tempout+=str(dict_reg[reg])
                            word+=1
                            break
                    imm=sentence[word][1:]
                    imm=int(imm)
                    if imm<0 or imm>255:
                        print("Error in line:",sencount,", Incorrect Immediate Value")
                        quit()
                    imm=bin(imm)
                    imm=imm[2:]
                    imm=int(imm)
                    lenimm=len(str(imm))
                    zeroes=8-lenimm
                    zero=0
                    while zero<zeroes:
                        tempout+=str("0")
                        zero+=1
                    tempout+=str(imm)
                    finout.append(tempout)
                elif index==2:
                    tempout+=str("00000")
                    word+=1
                    for reg in dict_reg:
                        if reg==sentence[word]:
                            if reg=="FLAGS":
                                print("Error in line:",sencount,", Flag is used as Register")
                                quit()
                            tempout+=str(dict_reg[reg])
                            word+=1
                            break
                    for reg in dict_reg:
                        if reg==sentence[word]:
                            if reg=="FLAGS":
                                print("Error in line:",sencount,", Flag is used as Register")
                                quit()
                            tempout+=str(dict_reg[reg])
                            break
                    finout.append(tempout)
                elif index==3:
                    word+=1
                    for reg in dict_reg:
                        if reg==sentence[word]:
                            if reg=="FLAGS":
                                print("Error in line:",sencount,", Flag is used as Register")
                                quit()
                            tempout+=(dict_reg[reg])
                            word+=1
                            break
                    lencount=len(str(count))
                    zeroes=8-lencount
                    zero=0
                    while zero<zeroes:
                        tempout+=("0")
                        zero+=1
                    for var in vardict:
                        if var==sentence[word]:
                            tempout+=str(vardict[var])
                            break
                        if sentence[word] not in vardict:
                            if sentence[word] in labeldict:
                                print("Error in line:",sencount,", Misused Label as Variable")
                                quit()
                            print("Error in line:",sencount,", Variable Not Defined")
                            quit()
                    finout.append(tempout)
                elif index==4:
                    word+=1
                    tempout+=str("000")
                    while zero<zeroes:
                        tempout+=("0")
                        zero+=1
                    for addr in labeldict:
                        if sentence[word]==addr:
                            tempout+=str(labeldict[addr])
                            break
                        if sentence[word] not in labeldict:
                            if sentence[word] in vardict:
                                print("Error in line:",sencount,", Misused Valiable as Label")
                                quit()
                            print("Error in line:",sencount,", Label Not Defined")
                            quit()
                    finout.append(tempout)
                    word+=1
                elif index==5:
                    word+=1
                    tempout+=("00000000000")
                    hltcount=1
                    finout.append(tempout)
                    break
                elif index==6:
                    word+=2
                    if sentence[word][0]=="$":
                        tempout=str("10010")
                        word-=1
                        for reg in dict_reg:
                            if reg==sentence[word]:
                                tempout+=(dict_reg[reg])
                                word+=1
                                break
                        imm=sentence[word][1:]
                        imm=int(imm)
                        if imm<0 or imm>255:
                            print("Error in line:",sencount,", Incorrect Immediate Value")
                            quit()
                        imm=bin(imm)
                        imm=imm[2:]
                        imm=int(imm)
                        lenimm=len(str(imm))
                        zeroes=8-lenimm
                        zero=0
                        while zero<zeroes:
                            tempout+=str("0")
                            zero+=1
                        tempout+=str(imm)
                        finout.append(tempout)
                    else:
                        tempout=str("1001100000")
                        word-=1
                        for reg in dict_reg:
                            if reg==sentence[word]:
                                tempout+=str(dict_reg[reg])
                                word+=1
                                break
                        for reg in dict_reg:
                            if reg==sentence[word]:
                                tempout+=str(dict_reg[reg])
                                break
                        finout.append(tempout)
                else:
                    word+=1
            elif sentence[0]=="var" and sentence[1] not in vardict:
                print("Error in line:",sencount,", Variable not defined at start")
                quit()
            else:
                if sentence[0] not in dict_op and sentence[0]!="var":
                    if sentence[0][-1]!=":":
                        print("Error in line:",sencount,", Opcode Error")
                        quit()
                    elif sentence[1] not in dict_op:
                        print("Error in line:",sencount,", Opcode Error")
                        quit()
                word+=1
if (ins[-1][0])!="hlt":
    if (ins[-1][0][-1]!=":"):
        print("hlt not used")
        quit()
for i in finout:
    print(i)

#Sameer Budhiraja
#Twisha Kacker
#Lakshay Bhushan
