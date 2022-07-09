#
# 코로나19 누적확진자수 예측 모델 (ver 2)
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/gdrive')
df = pd.read_csv('/content/gdrive/My Drive/COVID19.csv', encoding='euc-kr')

df['date'] = [(date // 100)*100 + (date%100*99/29) if date//100==2 else
              (date // 100)*100 + (date%100*99/30) if date//100==4 or date//100==6 or date//100==9 or date//100==11 else
              (date // 100)*100 + (date%100*99/31)
              for date in df['Date_reported']]

display(df.head())
mean_x, mean_y = np.mean(df['date']), np.mean(df['Cumulative_cases'])

xy = np.sum((df['date'] - mean_x)*(df['Cumulative_cases'] - mean_y))
xx = np.sum((df['date'] - mean_x)**2)

b = xy/xx
a = mean_y - b * mean_x

y_pred = a + b*df['date']
print('y =', a, '+', b, 'x')

plt.scatter(df['date'],df['Cumulative_cases'], marker='o', s=20)
plt.plot(df['date'],y_pred,'r')
plt.xlabel('Date_reported')
plt.ylabel('Cumulative_cases')
plt.show()
