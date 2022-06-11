import os
path = ''
filelist = os.listdir(path)

lenn = 0
max = 0
min = 0
k = 0
num1 = 0 # <100
num2 = 0 # 100-200
num3 = 0 # 200-500
num4 = 0 # 500-1000
num5 = 0 # >1000
for file in filelist:
    k = k + 1
    l = 0 # length for single pdb
    with open(file,'r') as f:
        for line in f.readlines():
            l = l + 1
        lenn = lenn + l # total length   
    if (l >= max or max == 0):
        max = l
    if (l <= min or min == 0):
        min = l
    if (l < 100):
        num1 = num1 + 1   
    if (l < 200 and l >= 100):
        num2 = num2 + 1  
    if (l < 500 and l >= 200):
        num3 = num3 + 1   
    if (l < 1000 and l >= 500):
        num4 = num4 + 1    
    if (l >= 1000):
        num5 = num5 + 1   
    if (k%1000 == 0):
        print(int(k/1000))
    #print(lenn)

