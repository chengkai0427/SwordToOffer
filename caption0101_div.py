class Division:
    def __init__(self, num1:int, num2:int):
        if num2 == 0:
            raise ValueError("除数不能为0！")
        self.num1 = num1
        self.num2 = num2

    def divide(self)->int:
        result=True if (self.num1>=0 and self.num2>0) or (self.num1<0 and self.num2<0) else False
        quotient=0
        value=abs(self.num2)
        num1=abs(self.num1)
        while num1>=abs(self.num2):
            q=1
            while num1>=value+value:
                value+=value
                q+=q
            num1-=value
            value=abs(self.num2)
            quotient+=q
        if num1>=abs(self.num2):
            quotient+=1
        return quotient if result else -quotient

if __name__ == '__main__':
    try:
        div=Division(*map(int, input("请输入两个整数，以空格分隔且除数不能为0：").split()))
    except ValueError:
        div = Division(*map(int, input("输入错误，请重新输入两个整数，以空格分隔且除数不能为0：").split()))
    print(div.divide())