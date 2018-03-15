list1=[['1', '2'], ['100', '200']]
print(list1)

# import numpy
# numpy.savetxt('abc.csv', list1, delimiter = ',')

import pandas as pd
df=pd.DataFrame(list1, columns=['a','b'])
print(df)
df.to_csv("abc.csv",header=False,index=False)


