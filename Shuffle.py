print("\t\t\t\tCLASS SHUFFLE");
print ("\t\t\t\t-------------");
import random
l=[]
for i in range(1,61):
       # if(i==1 or i==2):
#        continue;
        l.append(i)
a=[]
random.shuffle(l);
k=1
size=input("enter the size");
for j in l:
	a.append(j);
	
	if (len(a)==size):
		print "the team " + str(k)+" is\n",a,"\n"
		print "_______________________________"
		k+=1
		a=[]
	
	


