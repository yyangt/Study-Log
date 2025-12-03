"""
1.减少不必要的参数 - 如果某个值可以通过计算得到，就不要传递它
2.先写基本情况 - 养成习惯先处理边界条件
3.相信递归 - 不要试图在脑海中展开所有层次，相信子问题已解决
4.练习"自顶向下"思考 - 先想"如果子问题解决了，我如何用它"，再想"如何分解成子问题"
5.对比迭代版本 - 用循环实现同一题目，理解递归和迭代的转换
"""



#1.递归实现 flatten（扁平化嵌套结构）
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
return flatten(s1[0], s2) + flatten(s1[1:], s2)
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
#-------------------------
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

#2.count_turns(n)：
'''

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

#-------------------------
# 3.汉诺塔
# 将n个盘子从A柱移动到C柱（经过B柱）
def hanoi(n, start, end, spare):
  if n==1:
    print(f"将圆盘 1 从 {start} 移动到 {end}")
    return
  hanoi(n-1,start,spare,end)
  print(f"将圆盘 {n} 从 {start} 移动到 {end}")
  hanoi(n-1,spare,end,start)
hanoi(3,1,2,3)