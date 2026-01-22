import pandas as pd
import matplotlib.pyplot as plt

# Filenames for the raw data
file_inf = "512nodes_diameter37_cutoffinf-repetitions50-overlap100.xlsx"
# file_2_0 = "512nodes_diameter4_cutoff2.0-repetitions50-overlap100.xlsx"

# Load the datasets
df_inf = pd.read_excel(f"./../results/data_for_paper5 - thresh16.0 - new graph/first/{file_inf}")
# df_2_0 = pd.read_excel(f"./../results/data_for_paper2/first/{file_2_0}")

# Group by fraction and calculate the mean for both metrics
summary_inf = df_inf.groupby('fraction')[['stretch', 'stretch_arrow', 'stretch_parrow']].mean().reset_index()
# summary_2_0 = df_2_0.groupby('fraction')[['stretch', 'stretch_arrow', 'stretch_parrow']].mean().reset_index()

# Combine data for plotting
# combined = summary_inf.merge(summary_2_0, on='fraction', suffixes=('_inf', '_2.0'))
cmap = plt.get_cmap('tab20')

# Create the plot
plt.figure(figsize=(7, 5), dpi=180)
plt.xticks(fontsize=9)


fractions = summary_inf['fraction']

# Plotting the 4 lines

# plt.plot([str(x) for x in fractions], combined['stretch_2.0'], marker='.', linestyle='-', label=f'Stretch$_{'O'}$$_{'P'}$$_{'A'}$$_{'r'}$$_{'r'}$$_{'o'}$$_{'w'} $(${'err'}$ ≤ 0.5)', color=cmap(0), linewidth=1)
# plt.plot([str(x) for x in fractions], combined['stretch_arrow_2.0'], marker='v', linestyle='-.', label=f'Stretch$_{'A'}$$_{'r'}$$_{'r'}$$_{'o'}$$_{'w'} $(${'err'}$ ≤ 0.5)', color=cmap(1), linewidth=1)
# plt.plot([str(x) for x in fractions], combined['stretch_parrow_2.0'], marker='^', linestyle=':', label=f'Stretch$_{'P'}$$_{'A'}$$_{'r'}$$_{'r'}$$_{'o'}$$_{'w'} $(${'err'}$ ≤ 0.5)', color=cmap(2), linewidth=1)

# plt.plot([str(x) for x in fractions], summary_inf['stretch'], marker='.', linestyle='-', label=f'Stretch$_{'O'}$$_{'P'}$$_{'A'}$$_{'r'}$$_{'r'}$$_{'o'}$$_{'w'} $(${'err'}$ ≤ 0.0)', color=cmap(0), linewidth=1)
# plt.plot([str(x) for x in fractions], summary_inf['stretch_arrow'], marker='v', linestyle='-.', label=f'Stretch$_{'A'}$$_{'r'}$$_{'r'}$$_{'o'}$$_{'w'} $(${'err'}$ ≤ 0.0)', color=cmap(1), linewidth=1)
# plt.plot([str(x) for x in fractions], summary_inf['stretch_parrow'], marker='^', linestyle=':', label=f'Stretch$_{'P'}$$_{'A'}$$_{'r'}$$_{'r'}$$_{'o'}$$_{'w'} $(${'err'}$ ≤ 0.0)', color=cmap(2), linewidth=1)

plt.plot([str(x) for x in fractions], summary_inf['stretch_arrow'], marker='v', linestyle='-.', label=f'Arrow', color=cmap(2), linewidth=1)
plt.plot([str(x) for x in fractions], summary_inf['stretch_parrow'], marker='^', linestyle=':', label=f'PArrow', color=cmap(4), linewidth=1)
plt.plot([str(x) for x in fractions], summary_inf['stretch'], marker='.', linestyle='-', label=f'OPArrow', color=cmap(0), linewidth=1)


# Formatting the chart
plt.xlabel('Number of Operations', fontsize=12)
plt.ylabel('Stretch', fontsize=12)
# plt.title('Number of operations vs Mean Stretch for a network size n = 512', fontsize=12)
plt.legend(loc='best')
# plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks([str(x) for x in fractions])
plt.tight_layout()

# Save and show
# plt.savefig('stretch_fractions_plot.png')
plt.show()

# Optional: Export summary to CSV
# combined.to_csv('summary_plot_fractions.csv', index=False)