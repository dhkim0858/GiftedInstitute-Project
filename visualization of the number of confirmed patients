#
# 일별 코로나 확진자수 시각화하기
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/gdrive')
df = pd.read_csv('/content/gdrive/My Drive/COVID193.csv', encoding='euc-kr')
display(df.head())

df['date'] = df['Data_reported'].str.lstrip('2020-')
display(df.head())

ind = np.arange(len(df))
plt.figure(figsize=(10, 3))
plt.bar(ind,df['New_cases'],width=0.8)
#plt.xticks(rotation = 35)
plt.xlabel('Date_reported')
plt.ylabel('New_cases')
plt.show()
