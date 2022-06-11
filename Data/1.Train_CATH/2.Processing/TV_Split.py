# Put two files together to generate txt3.txt for information combination
txt1=[]
with open('txt1.txt','r') as f:
    for line in f.readlines():
        txt1.append(line.strip())

txt2={}
with open('txt2.txt','r') as f:
    for line in f.readlines():
        line=line.strip('\t')
        name,num=line.split()[0],line.split()[1]
        txt2[name]=num

res=[]
for i in range(len(txt1)):
    ls=txt1[i].split()
    ends=txt2[ls[0]]
    res.append(f'{ls[0]} {ls[1]}.{ls[2]}.{ls[3]}.{ls[4]}.{ls[5]} {ls[0][4]}.{ends}')

with open('txt3.txt','w') as f:
    for line in res:
        f.write(line+'\n')

# res: the content of txt3

dic={}
for item in res:
    t='.'.join(item.split()[1].split('.')[:3])
    if t not in dic:
        dic[t]=[]
        dic[t].append(item)
    else:
        dic[t].append(item)

# dic of the form: '4.10.40': ['1g9pA00 4.10.40.10.1 A.1-45', 
#                              '1aggA00 4.10.40.10.2 A.1-48', 
#                              '2rooA00 4.10.40.10.3 A.1-43', 
#                              '3zxcA00 4.10.40.20.1 A.1-77', 
#                              '1wqjB01 4.10.40.20.2 B.8-80', 
#                              '1h59B00 4.10.40.20.3 B.1-45', 
#                              '1xi7A00 4.10.40.20.4 A.6-52', 
#                              '1cixA00 4.10.40.20.5 A.1-44', 
#                              '1hy9A00 4.10.40.30.1 A.1-41', 
#                              '2l1qA00 4.10.40.50.1 A.1-40', 
#                              '2mf3A00 4.10.40.60.1 A.1-47', 
#                              '2jryA00 4.10.40.80.1 A.1-46']
# length of dic: 1442
# dic.items(): ('6.20.450', ['2waqQ00 6.20.450.10.1 Q.38-82', '3zbeA00 6.20.450.20.1 A.1-71'])

# fin: the content that will written to the file, fin[0], fin[1], fin[2], ...
# fin contains the value of the dic.items()
fin=[[] for _ in range(10)]
dicc=[] # dicc is of length 455
for k,v in dic.items():
    if len(v)==1:
        vv=v[0]
        dicc.append(vv)
        continue
    # k: key, v: value
    num=int(len(v)/10)
    reminder=len(v)%10
    # reminder=0 -> equally distirbuted
    if reminder==0:
        for i in range(10):
            tmp=v[num*i:num*(i+1)]
            for t in tmp:
                fin[i].append(t)
    # reminder=1 -> put remaining in file1(fin[0])
    elif reminder == 1:
        for i in range(10):
            if i == 0:
                tmp=v[0:num+1]
                for t in tmp:
                    fin[i].append(t)
            elif i != 0:
                tmp=v[(num*i+1):(num*(i+1)+1)]
                for t in tmp:
                    fin[i].append(t)
    # reminder=2 -> put remaining in file1 to file2
    elif reminder == 2:
        for i in range(10):
            if (i == 0 or i == 1):
                tmp=v[(i*(num+1)):((i+1)*(num+1))]
                for t in tmp:
                    fin[i].append(t)
            elif i >= 2:
                tmp=v[(num*i+2):(num*(i+1)+2)]
                for t in tmp:
                    fin[i].append(t)
    # reminder=3 -> put remaining in file1 to file3                           
    elif reminder == 3:
        for i in range(10):
            if (i == 0 or i == 1 or i == 2):
                tmp=v[(i*(num+1)):((i+1)*(num+1))]
                for t in tmp:
                    fin[i].append(t)
            elif i >= 3:
                tmp=v[(num*i+3):(num*(i+1)+3)]
                for t in tmp:
                    fin[i].append(t)
    # reminder=4 -> put remaining in file1 to file4 
    elif reminder == 4:
        for i in range(10):
            if (i == 0 or i == 1 or i == 2 or i == 3):
                tmp=v[(i*(num+1)):((i+1)*(num+1))]
                for t in tmp:
                    fin[i].append(t)
            elif i >= 4:
                tmp=v[(num*i+4):(num*(i+1)+4)]
                for t in tmp:
                    fin[i].append(t)
    # reminder=5 -> put remaining in file6 to file10 
    elif reminder == 5:
        for i in range(10):
            if (i >= 0 and i <= 4):
                tmp=v[(i*num):((i+1)*num)]
                for t in tmp:
                    fin[i].append(t)
            elif i >= 5:
                tmp=v[(i*num+(i-5)):((i+1)*num+(i-4))]
                for t in tmp:
                    fin[i].append(t)
    # reminder=6 -> put remaining in file5 to file10 
    elif reminder == 6:
        for i in range(10):
            if (i >= 0 and i <= 3):
                tmp=v[(i*num):((i+1)*num)]
                for t in tmp:
                    fin[i].append(t)
            elif i >= 4:
                tmp=v[(i*num+(i-4)):((i+1)*num+(i-3))]
                for t in tmp:
                    fin[i].append(t)
    # reminder=7 -> put remaining in file4 to file10
    elif reminder == 7:
        for i in range(10):
            if (i >= 0 and i <= 2):
                tmp=v[(i*num):((i+1)*num)]
                for t in tmp:
                    fin[i].append(t)
            elif i >= 3:
                tmp=v[(i*num+(i-3)):((i+1)*num+(i-2))]
                for t in tmp:
                    fin[i].append(t)
    # reminder=8 -> put remaining in file3 to file10
    elif reminder == 8:
        for i in range(10):
            if (i >= 0 and i <= 1):
                tmp=v[(i*num):((i+1)*num)]
                for t in tmp:
                    fin[i].append(t)
            elif i >= 2:
                tmp=v[(i*num+(i-2)):((i+1)*num+(i-1))]
                for t in tmp:
                    fin[i].append(t)
    # reminder=9 -> put remaining in file2 to file10
    elif reminder == 9:
        for i in range(10):
            if (i == 0):
                tmp=v[(i*num):((i+1)*num)]
                for t in tmp:
                    fin[i].append(t)
            elif i >= 1:
                tmp=v[(i*num+(i-1)):((i+1)*num+i)]
                for t in tmp:
                    fin[i].append(t)                    

# distribute dicc to 10 files correspondingly
numm=int(len(dicc)/10)
for j in range(0,9):
    tmpp=dicc[(j*numm):((j+1)*numm)]
    for tt in tmpp:
        fin[j].append(tt)
tmpp=dicc[(j+1)*numm:]
for tt in tmpp:
    fin[9].append(tt)

# sum = 0 # used for check if all the index are written among the 10 files
for i in range(0,10):
    # sum = sum + len(fin[i])
    print(len(fin[i])) 
# print(sum)


for i in range(0,10):
    with open(f'list{i}.txt','w') as f:
        for line in fin[i]:
            f.write(line+'\n')