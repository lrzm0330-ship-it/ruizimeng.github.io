def god(p,q): #使用递归函数计算p和q的最大公约数
    if q==0：
        return p #如果q=0,返回p
    return god(q,p%q) #否则，递归调用god(q,p%q)

p=int(input('p:'))
q=int(input('q:'))
print(god(p,q)) #计算并输出p和q的最大公约数

'''
print(god(p,q))中的god(p,q)不是函数本身，而是函数执行后的结果
函数执行后的结果，通常就是return返回的内容
'''
