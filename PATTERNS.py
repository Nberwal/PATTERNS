
input="TitTat"
for j in range(1,len(input)):
    if ord(input[j])<=90:
        split=j
str1=input[:split].upper()
str2=input[split:].upper()
maximum=max(len(str1),len(str2))
for i in range(maximum):
    print(str1[0:i+1]+str2[0:i+1])



input="BreakingBad"
for j in range(1,len(input)):
    if ord(input[j])<=90:
        split=j
str1=input[:split].upper()
str2=input[split:].upper()
maximum=max(len(str1),len(str2))
for i in range(maximum):
    print(str1[0:i+1]+str2[0:i+1])
    
Output:    

BB
BRBA
BREBAD
BREABAD
BREAKBAD
BREAKIBAD
BREAKINBAD
BREAKINGBAD
