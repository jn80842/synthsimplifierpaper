import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("../data/num_rules_found", delim_whitespace=True, header=None)
data.columns = ["expressions", "rules"]

print(data)

fig, ax = plt.subplots(figsize=(5,2))
ax.plot(data['expressions'], data['rules'])
ax.set(xlabel='Unique Expressions', ylabel='New Rules',
       title='Rules Found Per # of Unique Expressions')
#plt.show()
plt.savefig("num-rules-found.pdf", bbox_inches="tight")
