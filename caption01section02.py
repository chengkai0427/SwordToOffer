class Binaryadd:#二进制加法，因python的int类不存在溢出，所以拟直接转换后相加再转换回二进制
    def __init__(self, a:str,b:str):
        if len(a)!=a.count('0')+a.count('1') or len(b)!=b.count('0')+b.count('1'):#判断输入是否合法
            raise ValueError("输入的二进制数不合法")
        self.a = a
        self.b = b

    def add(self):
        return bin(int(self.a,2) + int(self.b,2))[2:]

print(Binaryadd(*input("请输入两个二进制数，用空格分隔：").split()).add())