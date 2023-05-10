import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'Malgun Gothic'

filename = 'ex802.csv'
df = pd.read_csv(filename, index_col='type', encoding='utf-8')
print(df)

df.plot(kind='line', legend=True, title='지역별 차종 교통량',
        use_index=True,figsize=(10,6))

filename = 'ex802Graph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
plt.show()
print(filename + 'Saved...')