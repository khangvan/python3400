print('Masterdata 2018');

# Python version
import sys
print('Python: {}'.format(sys.version))
# scipy
import scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy as np
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas as pd
print('pandas: {}'.format(pd.__version__))
# scikit-learn
# import sklearn
# print('sklearn: {}'.format(sklearn.__version__))
# import os
# cwd= os.getcwd();

# 1read excel
xl=pd.ExcelFile(".\\PyPractice\masterdata\MM-3400-Jan2018.XLSX")
xl.sheet_names
df=xl.parse('Sheet1')
df.head
df=pd.DataFrame(df)
df
##view colum name
df.columns.tolist() #ok
# filter col name consumtion & forceast

# df=df[(df.T != 0).any()]
# 2select some colum

   
# 3unpivot
# 4group by hienrachy
pv=df.pivot_table(index=['Fam. Grp. Descr.','Product hierarchy level 1'],values="Annual demand", aggfunc=sum,dropna=True)
pv=pv.loc[~(pv==0).all(axis=1)]
pv.to_excel("D:\Python\PyPractice\masterdata\\test.xlsx","test")
# 5charting