import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('./Chicago_Crimes_2012_to_2017.csv')
primary_type_count = df['Primary Type'].value_counts().head(8)
x = primary_type_count.plot(kind='bar')

plt.title("Quantidade de crimes por tipo")
plt.xlabel("Tipo de crime")
plt.ylabel("Contagem")

fig = x.get_figure()
fig.savefig('./graph.jpg')