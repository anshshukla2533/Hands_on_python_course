"""
Marks Range Category
90 - 100 Excellent
75 - 89 Very Good
60 - 74 Good
40-  59 Average
0  -39 Fail
 <0 or >100 Invalid
"""

### if marks is equal to my registartion number ending with 21 then i will add bonus twice  21
valid=0
failed=0
marks=[]
n=int(input("Enter the number of students: "))
for i in range(n):
    i=int(input("Enter the marks of student: "))
    if i==21:
        marks.append(i+21)
    else:
        marks.append(i)
    
print(marks)
for mk in marks:
    if mk>=90 and mk<=100:
        valid=valid+1
        print("EXCELLENT")
    elif mk>=75 and mk<=89:
        valid=valid+1
        print("very good")
    elif mk>=60 and mk<=74:
        valid=valid+1
        print("good")
    elif mk>=40 and mk<=59:
        
            
        valid=valid+1
        print("average")
    elif mk>=0 and mk<=39:
        failed=failed+1
        print("fail")
    else:
        print("invalid")
print("the number of failed student is",failed)
print("the number of passed student is ",valid)