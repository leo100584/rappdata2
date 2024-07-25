import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(0,5,(10,5))

#save file:
df.to_excel("excel_test1.xlsx",sheet_name="Sheet1")

#load file:
print(pd.read_excel("excel_test1.xlsx","Sheet1",index_col=None, na_values=["NA"])


