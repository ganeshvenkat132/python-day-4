Roll_num="AP24110011591"
D=int(Roll_num[-1])
n=int(input("Enter the No. of scores : "))
marks=[0]*n
lowRisk=[]
mediumRisk=[]
highRisk=[]
criticalRisk=[]
for i in range(n):
    marks[i]=int(input("    Enter the score : "))

ignore=0
valid=0

for i in range(n):
    if marks[i]<0 :
       ignore = ignore+1

    elif 0<=marks[i]<=30:
         valid=valid+1
         lowRisk=lowRisk+[marks[i]]
 
    elif 31<=marks[i]<=60:
         valid=valid+1
         mediumRisk=mediumRisk+[marks[i]]

    elif 61<=marks[i]<100:
        valid=valid+1
        highRisk=highRisk+[marks[i]]

    elif marks[i]>=100:
        valid=valid+1
        criticalRisk=criticalRisk+[marks[i]]

print("Registered Digit(D)",D)

print("    Low Risk =",lowRisk)
print("    Medium Risk =",mediumRisk)
print("    High Risk =",highRisk)
print("    Critical Risk =",criticalRisk)

print("After Personalized Filtering:")

if D%2==0:
    p=len(lowRisk)
    lowRisk=[]
    print("    Low Risk =", lowRisk)
    print("    Medium Risk =", mediumRisk)
    print("    High Risk =", highRisk)
    print("    Critical Risk =", criticalRisk)
    print("Total Valid Entries =", valid)
    print("Total Ignored Entries =", ignore)
    print("Removed Due To Personalization =", p)

elif D%2==1:
    q=len(criticalRisk)
    criticalRisk=[]
    print("    Low Risk =", lowRisk)
    print("    Medium Risk =", mediumRisk)
    print("    High Risk =", highRisk)
    print("    Critical Risk =", criticalRisk)
    print("Total Valid Entries =", valid)
    print("Total Ignored Entries =", ignore)
    print("Removed Due To Personalization =", q)
