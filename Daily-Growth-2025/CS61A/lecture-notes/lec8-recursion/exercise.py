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
#1. 计算数字 n 有多少位
def count_digit(n):
  if n<10:
    return 1
  return count_digit(n//10)+1
#2. 数字各位和
def sum_digits(n):
  if n<10:
    return n
  return n%10+sum_digits(n//10)
# print(sum_digits(1234))
#3. 判断数字是否为某个整数的幂（如 2 的幂）
def is_power_of_two(n):
  if n==1:
    return True
  if n%2!=0:
    return False
  if n<=0:
    return False
  return is_power_of_two(n//2)
#4. 交替加减序列
# 1 - 2 + 3 - 4 + 5 - 6 + … + n
# 用递归写出第 n 项的值。
def nth_sum(n):
  if n==1:
    return 1
  elif n%2==0:
    return nth_sum(n-1)-n
  else:
    return nth_sum(n-1)+n
#5. 计算分段函数
'''f(n) = n             if n < 10
f(n) = f(n//10) + n  otherwise'''
def f(n):
  if n<10:
    return n
  return f(n//10)+n

#6. 递归实现 max（不允许循环）
'''def recursive_max(s):
  def solustion(s,cur):
    if cur<=s[0]:
      return solustion(s[1:],s[0])
    if len(s)==1:
      return cur
    if cur>s[0]:
      return solustion(s[1:],cur)
  return solustion(s,s[0])'''
def maxx(s):
  if len(s)==1:
    return s[0]
  sub=maxx(s[1:])
  return s[0] if s[0]>sub else sub
print(maxx([2,3,4,1,8,7,20,11]))

#7. 数组和，但是必须用 divide & conquer（递归分治）
'''def sum(s):
  if len(s)<=1:
    return s[0]
  return s[0]+sum(s[1:])'''
def sum(s):
  if len(s)==1:
    return s[0]
  mid=len(s)//2
  return sum(s[:mid])+sum(s[mid:])
print(sum([1,2,3,4,5]))

#8. zigzag(n,k)
'''
定义一个序列：
1, 2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1
1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1,
“从 1 数到 k 再数回 1，然后 k + 1 再来一遍”
要求求第 n 项（不能用 while）。

'''
#想法：我将1至k至2作为一段，那么第i段：(k-1)*2，如果给一个参数代表第这第n项在减去第i段后在第几个，那么只要算出在这个第i+1段的对应位的值便可
def zigzag(n,k):
  def solution(index,kk):
    if (kk-1)*2<index:
      return solution(index-(kk-1)*2,kk+1)
    if index<=kk:
      return index
    if index>kk:
      return 2*kk-index
  return solution(n,k)

#9. 递归方向翻转序列
'''
与 pingpong 非常接近：
定义方向：
1 → 正
每当遇到 7 的倍数，就翻转。
求第 n 次操作的总和。'''
def pingpong2(n):
  def solution(cur,value,direction,sum):
    if cur==n:
      return sum
    if cur%7==0:
      return solution(cur+1,value-direction,-direction,sum+value-direction)
    return solution(cur+1,value+direction,direction,sum+value+direction)
  return solution(1,1,1,1)


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if x==0:
        return 0
    return num_eights(x//10)+(x%10==8)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    '''if n<=8:
        return n
    else :
        return pingpong(n-1)+direction(n-1)'''
    def solution(values,index,direction):
        if index ==n:
            return values
        if index%8==0 or num_eights(index)>0:
            return solution(values-direction,index+1,-direction)
        return solution(values+direction,index+1,direction)
    return solution(1,1,1)
def direction (n):
    if n==8:
        return -1
    return direction(n-1) * (-1 if num_eights(n) or n%8==0 else 1)


#10. 比 pingpong 更难：
'''
count_turns(n)：
从 1 数到 n，一共有多少次方向翻转（触发条件同 pingpong: 8 或含 8）'''
def count_turns(n):
  def solution(values,index,direction,count):
        if index ==n:
            return count
        if index%8==0 or num_eights(index)>0:
            return solution(values-direction,index+1,-direction,count+1)
        return solution(values+direction,index+1,direction,count)
  return solution(1,1,1,0)
#纯递归版：
def count_turns2(n):
  def turns(k):
    if k<=1:
      return 0
    if k%8==0 or num_eights(k)>0:
      return turns(k-1)+1
    return turns(k-1)
  return turns(n)

#11.互相递归（Mutual Recursion）
# f(n) = n - g(f(n - 1))
# g(n) = n - f(g(n - 1))
# f(1) = 1, g(1) = 1
def f(n):
  if n==1:
    return 1
  return n-g(f(n - 1))
def g(n):
  if n==1:
    return 1
  return n - f(g(n - 1))
# print(f(4))
#12.递归统计某序列的局部极值点数量
'''给定：
一个序列 s，求序列中有多少个“局部峰值”和“局部谷值”。
局部峰值：s[i] > s[i-1] and s[i] > s[i+1]
局部谷值：s[i] < s[i-1] and s[i] < s[i+1]'''
def jizhi(s,c):
  if len(s)<3:
    return c
  if (s[1] > s[0] and s[1] > s[2]) or (s[1] < s[0] and s[1] < s[2]):
    return jizhi(s[1:],c+1)
  return jizhi(s[1:],c)
# print(jizhi([1,3,2,4,3],0))

#13.递归实现 flatten（扁平化嵌套结构）
'''不能用列表推导、不能用循环。
输入：[1, [2, [3, 4], 5], [6], 7]
输出：[1, 2, 3, 4, 5, 6, 7]'''
def flatten(s1,s2):
  if len(s1)==0:
      return s2
  if type(s1[0])==int :
    
    return flatten(s1[1:],s2+[s1[0]])
  # return flatten(s1[0],s2)+flatten(s1[1:],s2)  ×
  return flatten(s1[1:],flatten(s1[0],s2)) #     √
#把第一次递归的结果作为第二次递归的输入
'''代码试图用 + 连接两个递归结果，但这违背了累加器模式的原则。
累加器模式的核心思想
累加器应该像一个"传递的篮子"：
1.每次递归把新元素放入篮子
2.篮子一路传递到底
3.最后返回装满的篮子
错误代码:
pythonreturn flatten(s1[0], s2) + flatten(s1[1:], s2)
这相当于：

1.创建两个独立的篮子，都从 s2 开始
2.分别装不同的东西
3.最后把两个篮子的内容倒在一起

这不是累加器模式，这是分治模式'''
#--------------------------
'''
# 分治算法：
def flatten(s):
  if len(s)==0:
    return []
  if type(s[0])==int :
    return [s[0]]+flatten(s[1:])
  return flatten(s[0])+flatten(s[1:])
'''
print(flatten([1, [2, [3, 4], 5], [6], 7],[]))

#14.递归版的“二分查找”
'''输入：一个已排序列表 s 和目标值 x
要求用递归实现：binary_search(s, x) → True/False
'''

def binary_search(s,x):
  def helper(l,r):
    if l>r:
      return False
    mid=(l+r)//2
    if s[mid]>x:
      return helper(l,mid-1)
    elif s[mid]<x :
      return helper(mid+1,r)
    elif s[mid]==x:
      return True
    return False
  return helper(0,len(s))
print(binary_search([3],2))
#15.递归分割整数（Partition Count）

'''count_partitions(n, k)：
求 n 能用不超过 k 的正整数分解的方案数。'''
def count_partitions(n, k):
  if n==0:
    return 1
  if n<0:
    return 0
  if k==0:
    return 0
  return count_partitions(n-k,k)+count_partitions(n,k-1)
print(count_partitions(6,4))