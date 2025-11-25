#SICP Exercise 1.11（树形递归 vs 迭代）
'''A function f is defined by the rule that:

f(n) = n if n < 3, and

f(n) = f(n-1) + 2f(n-2) + 3f(n-3) if n ≥ 3

Write a procedure that computes f by means of a recursive process. Write a procedure that computes f by means of an iterative process."
'''
def f1(n):
  if n<3:
    return n
  else:
    return f1(n-1) + 2*f1(n-2) + 3*f1(n-3)
def f2(n):
  if n<3:
    return n
  a=0
  b=1
  c=2
  i=3
  while i<=n:
    i+=1
    ans=c+2*b+3*a
    a,b,c=b,c,ans
  return ans
#2.SICP Exercise 1.12（帕斯卡三角形）
'''
"The following pattern of numbers is called Pascal's triangle:
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
   ...
The numbers at the edge of the triangle are all 1, and each number inside the triangle is the sum of the two numbers above it. Write a procedure that computes elements of Pascal's triangle by means of a recursive process."
'''
def triangle(row,col):
  if col==0 or row==col:
    return 1
  else:
    return triangle(row-1,col)+triangle(row-1,col-1)
#3.61A Fa20 Midterm 2 #4: Paths（上下顺序决定输出顺序）
