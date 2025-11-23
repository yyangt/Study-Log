#1.创建第一个函数用于分割数字
def split(n):
  return n//10,n%10
#2.创建第二个函数用于计算每一位之和
def sum_digit(n):
  if n<10:
    return n
  else:
    all_but_last,last=split(n)
    return last+sum_digit(all_but_last)#递归调用，向下达到最基础条件
print(sum_digit(1234))
#创建第三个函数，计算基于信用卡算法的位数之和：从右往左偶数位×2，如果超过10，计算两位之和，最终返还所有位数之和
def lum_sum(n):
  if n<10:
    return n
  else:
    all_but_last,last=split(n)
    return lum_sum_double(all_but_last)+last
#创建第四个函数，计算对应偶数位×2
'''def lum_sum_double(n):
  all_but_last,last=split(n)
  lum_digit=sum_digit(last*2)
  if n<10:
    return lum_digit
  else:
    return lum_sum(all_but_last)+lum_digit
print(lum_sum(138743))'''
def lum_sum_double(n):
  
  if n==0:
    return n
  else:
    all_but_last,last=split(n)
    lum_digit=sum_digit(last*2)
    return lum_sum(all_but_last)+lum_digit
print(lum_sum(138743))