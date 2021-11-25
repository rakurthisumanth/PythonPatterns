# Tringle

# --> 1)First
n1=int(input())
for i in range(1,n1+1):
    for j in range(1,n1+1):
        print(j,end="")
    print()
# Out Put

# 12345
# 12345
# 12345
# 12345

# --> 2) Secound
n1=int(input())
for i in range(1,n1+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# Out Put
# 1
# 12
# 123
# 1234
# 12345

# -->3) Third

n=int(input())
s=''
for i in range(1,n+1):
    s+=str(i)
    print(' '*(n-i)+s)

#          1
#       1  2
#     1 2  3
#   1 2 3  4
# 1 2  3 4  5

#--> 4 Fourth 

n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
# Out Put
# 12345
# 1234
# 123
# 12
# 1

# --> 5 Five Sum

n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print((i+j+1)%2,end="")
    print()


# Out pUT 
# 1
# 01
# 101
# 0101
# 10101

# Sum 6-->

n=int(input())
for i in range(1,n//2+2):
    for j in range(1,n+1):
        if j==i or j==n-i+1:
            print(j,end="")
        else:
            print(" ",end="")
    print()
        

# Out Put -->
# 1   5
#  2 4
#   3


#Sum 7 -->

n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==i:
            print(j,end="")
        else:
            print(" ",end="")
    print()

# OUT PUT-->
# 1
#  2
#   3
#    4
#     5

# Sum 8 -->

def findMax(a,b):
    if a>b:
        return a
    else:
        return b
n=int(input())
for i in range(1,2*n):
    for j in range(1,2*n):
        print(findMax(abs(i-n),abs(j-n))+1,end=' ')
    print()

# OUT PUT

# N = 3

# 3 3 3 3 3
# 3 2 2 2 3
# 3 2 1 2 3
# 3 2 2 2 3
# 3 3 3 3 3




# Sum 9) -->

n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)

   ## Out pUT 
    #      *
    #     * *
    #    * * *
    #   * * * *
    #  * * * * *
    # * * * * * *


  # 10) Sum-->


n=int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)


# Out Put --->

# * * * * * 
#  * * * *
#   * * *
#    * *
#     *


# 11)--->Sum


n= int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)


# Out Put --->

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *


# 12)-->Sum 

n=int(input())
for i in range(n,0,-1):
    print("* "*i)


#Out Put --> 
   
# * * * * * 
# * * * *
# * * *
# * *
# *


# 13) Sum-->


n=int(input())
for i in range(1,n+1):
    print("* "*i)
for i in range(n,0,-1):
    print("* "*i)


# Out Put-->


# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


# 14) Sum -->



for i in range(7):
    for j in range(5):
        if ( (j==0 or j==4) and i!=0) or ((i==0 or i==3  ) and (j>0 and j<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()



# OUT Put -->

#  ***
# *   *
# *   *
# *****
# *   *
# *   *
# *   *


# 15) Sum -->

for i in range(7):
    for j in range(5):
        if (j==0 ) or (j==4 and(i!=0 and i!=3 and i!=6)) or ((i==0 or i==3 or i==6) and (j>0 and j<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
    

# out put -->

# **** 
# *   *
# *   *
# ****
# *   *
# *   *
# ****

