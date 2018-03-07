# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Reset default params
sns.set()

# Set context to `"paper"`
sns.set_context("paper")

# Load iris data
data1 = pd.read_csv('C:\Users\Joris\Google Drive\Gima\Module_2\Case_Study\SPSS\dataset.csv', sep = ';', decimal =',')


# Construct iris plot
sns.regplot(x="trip_freq", 
 y="avg_trip_lengt_night", 
 data=data1)
ax.set(xlabel = 'Average trip length in meters', ylabel = 'Frequency')
ax.grid(False)

# Show plot
plt.show()