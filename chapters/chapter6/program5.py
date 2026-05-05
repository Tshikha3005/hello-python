# factorial

n = int(input("Enter number you want the factorial"))

i = 1
fact_no = 1

# while(i <= n):
#   fact_no *= i
#   i+=1
# print(fact_no)


for i in range(1, n+1):
  fact_no *= i
print(fact_no)