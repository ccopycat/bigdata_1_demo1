import pandas as pd 
import numpy as np 


# ages=[18,20,24,25,29,33,35,42,45,60,65,100]
# # 划分 18-25 25-35 35-60 60-100
# bins=[18,25,35,60,100]

# cuts=pd.cut(ages,bins)
# print(cuts)
# print(pd.value_counts(cuts))

# data=pd.read_json("D:/movies.json",encoding="utf-8")
# bins=(7.5,8.0,8.5,9.0,9.5,10)
# cuts=pd.cut(data['score'],bins)
# print(cuts)pd 
# print(pd.value_counts(cuts))

# data=np.random.rand(10)
# print(pd.cut(data,4,precision=2))


# df=pd.DataFrame(np.random.randn(10,3))
# col=df[1]
# a=np.abs(col)
# print(col[np.abs(col)>1])

# df=pd.DataFrame(np.arange(20).reshape(5,4))
# # 随机返回顺序
# s=np.random.permutation(5)
# # print(df.take(s))
# print(df.sample(n=3,axis=1))

data={
    "key":['a','b','c'],
    "num":range(3)
}
df=pd.DataFrame(data)
print(df)
print(pd.get_dummies(df['key']))