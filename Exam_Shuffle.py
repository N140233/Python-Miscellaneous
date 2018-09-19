import random
d={}
l=[]
for i in range(1,68,1):
    l.append(i);
random.shuffle(l);
a=['a0','a1','a2','a3','a4','a5','a6','a7','a8','a9','b0','b1','b2','b3','b4','b5','b6','b7','b8','b9','c0','c1','c2','c3','c4','c5','c6','c7','c8','c9','d0','d1','d2','d3','d4','d5','d6','d7','d8','d9','e0','e1','e2','e3','e4','e5','e6','e7','e8','e9','f0','f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','a10','b10','c10','d10','e10']
random.shuffle(a);
d=dict(zip(l,a))
#print d;
for i in range(1000):
    a=input("enter ur roll number");
    if(a==0):
        exit(0);
    if(d.has_key(a)==True):
        print "your position is",d[a];
    else:
        print 'not found'
