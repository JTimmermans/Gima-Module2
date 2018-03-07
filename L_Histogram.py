# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Reset default params
sns.set()

# Set context to `"paper"`
sns.set_context("paper")

# Load iris data
data = pd.read_csv('C:\Users\Joris\Google Drive\Gima\Module_2\Case_Study\SPSS\dataset.csv', sep = ';', decimal =',')
x=data['avg_trip_length']

# Construct iris plot
ax = sns.distplot(x, kde=False)
ax.set(xlabel = 'Average trip length in meters', ylabel = 'Frequency')
ax.grid(False)

# Show plot
plt.show()

