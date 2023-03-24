import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('flights')
print(df.head())
plt.figure()
sns.lineplot(x='month', y='passengers', hue='year', data=df)
plt.show(block = True)