import matplotlib.pyplot as plt
from data_load import new_filtered_list_1
minutes = []
for i in new_filtered_list_1:
     minutes.append(i[2])

plt.hist(minutes, bins=20, color='blue', edgecolor='black')
plt.title("Journey Time Histogram")
plt.xlabel("Journey Time (minutes)")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.75)

# Show or save the histogram
plt.show()
