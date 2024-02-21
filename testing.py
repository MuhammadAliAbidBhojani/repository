import pandas as pd
import matplotlib.pyplot as plt


dict = {"Gender":['Men', 'Women', 'Other'],
        "Count":[4986, 1356, 659]
}

df = pd.DataFrame(dict)

fig, ax = plt.subplots()
ax.barh(width=dict['Count'], y=dict['Gender'])
ax.set_xlabel('Gender')
ax.set_ylabel('Count')

print('Working...')