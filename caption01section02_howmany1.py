class Countof1:#计算前N个数各自二进制表示中1的个数
    def __init__(self, n:int):
        if n < 0 or  not isinstance(n,int):
            raise ValueError("n应为非负整数")
        self.n = n
    def count1(self)->list:
        result=[0]
        for i in range(1,self.n):
            result.append(result[i&(i-1)]+1)#也可以用result.append(result[i>>1]+(i&1))
        return result

print(Countof1(int(input("请输入一个非负整数："))).count1())#输入10，则输出[0, 1, 1, 2, 1, 2, 2, 3, 1, 2]