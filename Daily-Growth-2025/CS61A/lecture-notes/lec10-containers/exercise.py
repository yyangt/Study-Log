#write a function that takes as input
#integer n and return the sum of the first n
def iterative_sum(n):
  sum=0
  for i in range(n+1):
    sum+=i
  return sum
def recursive_sum(n):
  if n==1:
    return 1
  return recursive_sum(n-1)+n
print(recursive_sum(10),iterative_sum(10))

#list comprehensions
#从旧容器中得到新容器
odds=[1,3,5,7,9]
[x+1 for x in odds]
[x for x in odds if 25%x==0]
#计算约数：
def divisors(n):
  return [1]+[x for x in range(2, n) if n%x==0]
print(divisors(9))
#翻转字符串：
def reverse_string(s):
  if len(s)<=1:
    return s
  return s[1:]+s[0]