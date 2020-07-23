import math


if __name__ == '__main__':
    n = int(input())
    for i in range(1,11): #1부터 11미만의 수를 합한다.
        result = n * i
        print( "%d x %d = %d" %(n,i,result))
        
