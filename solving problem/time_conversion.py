import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    a = s[-2:] #PM
    s1 = s[:-2]
    hour = s1[:2] #07
    rest = s1[2:] #:09:45
    
    check = hour+rest
    conversion = int(hour)
    
#print(int(h)-12) #prints everything except last two letters 12:09:45
#print(a) #prints Last two letters PM

    if a.upper()=="PM":
        if conversion == 12:
            return(s[:-2])
        else:
            conversion2 =  conversion + 12
            conversion1 = str(conversion2)
            return(conversion1+rest)
    else:
        if conversion ==12:
            hour ='00'
            return(hour+rest)
        else:
            return(s[:-2])


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
