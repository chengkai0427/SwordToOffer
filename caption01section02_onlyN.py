class OnlyN:
    def __init__(self, nums:list[int], n:int,m:int):#数组中只一个数字出现了N次，其他数字出现了M次
        if not(n % m) and not(m % n):
            raise ValueError("N不能被M整除，M也不能被N整除，请调整参数")
        self.nums=nums
        self.n=n
        self.m=m
    def findn(self)->int:
        bit_width=max(self.nums).bit_length()
        result_c=''
        for i in range(bit_width):
            count=0
            for j in self.nums:
                count+=1 if j&(1<<i) else 0
            result_c=('1' if count % self.m else '0') + result_c
        return int(result_c,2)

if __name__ == '__main__':#测试用例
    nums=[25,25,26,26,26,27,27,27]
    n=2
    m=3
    onlyn=OnlyN(nums,n,m)
    print(onlyn.findn())