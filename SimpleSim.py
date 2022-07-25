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



