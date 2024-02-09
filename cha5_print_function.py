# Printing the consecutive numbers till a given range 
if __name__ == '__main__':
    n = int(input())
    if 1<=n<=150:
        for num in range(1,n+1):
            print(num, end="")