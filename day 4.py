Roll_num="AP24110011591"
D=int(Roll_num[-1])
n=int(input("Enter the No. of scores : "))
marks=[0]*n
low_risk=[]
medium_risk=[]
high_risk=[]
critical_risk=[]
for i in range(n):
    marks[i]=int(input("    Enter the score : "))

ignore=0
valid=0

for i in range(n):
    if marks[i]<0 :
       ignore = ignore+1

    elif 0<=marks[i]<=30:
         valid=valid+1
         low_risk=low_risk+[marks[i]]
 
    elif 31<=marks[i]<=60:
         valid=valid+1
         medium_risk=medium_risk+[marks[i]]

    elif 61<=marks[i]<=100:
        valid=valid+1
        high_risk=high_risk+[marks[i]]

    else :
        valid=valid+1
        critical_risk=critical_risk+[marks[i]]

print("D =",D)

print("    Low Risk =",low_risk)
print("    Medium Risk =",medium_risk)
print("    High Risk =",high_risk)
print("    Critical Risk =",critical_risk)

print("After Personalized Filtering:")

if D%2==0:
    p=len(low_risk)
    low_risk=[]
    print("    Low Risk =", low_risk)
    print("    Medium Risk =", medium_risk)
    print("    High Risk =", high_risk)
    print("    Critical Risk =", critical_risk)
    print("Total Valid Entries =", valid)
    print("Total Ignored Entries =", ignore)
    print("Removed Due To Personalization =", p)

elif D%2==1:
    q=len(critical_risk)
    critical_risk=[]
    print("    Low Risk =", low_risk)
    print("    Medium Risk =", medium_risk)
    print("    High Risk =", high_risk)
    print("    Critical Risk =", critical_risk)
    print("Total Valid Entries =", valid)
    print("Total Ignored Entries =", ignore)
    print("Removed Due To Personalization =", q)
