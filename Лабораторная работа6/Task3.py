import pandas as pd

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

pd.DataFrame({'A':a,'B':b,'C':c}).to_csv("C:\\Users\\Administrator\\Desktop\\test.csv",index=False,sep=',')