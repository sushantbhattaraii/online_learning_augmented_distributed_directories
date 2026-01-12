import pandas as pd
import matplotlib.pyplot as plt

# Define categories and the corresponding cutoff strings found in filenames
categories = ['$\leq 0.0$', '$\leq 0.1$', '$\leq 0.2$', '$\leq 0.3$', '$\leq 0.4$', '$\leq 0.5$']
cutoffs = ['inf', '10.0', '5.0', '3.3333333333333335', '2.5', '2.0']

# Data structures to store results for 4 line graphs
results = {
    'Category': categories,
    'mean_stretch_256': [],
    'mean_stretch_arrow_256': [],
    'mean_stretch_1024': [],
    'mean_stretch_arrow_1024': []
}
cmap = plt.get_cmap('tab20')

# Process files for each category
for cutoff in cutoffs:
    # Construct filenames for 256 and 1024 nodes
    file_256 = f"256nodes_diameter5_cutoff{cutoff}-repetitions50-overlap100.xlsx"
    file_1024 = f"1024nodes_diameter4_cutoff{cutoff}-repetitions50-overlap100.xlsx"
    
    # Load and aggregate data for 256 nodes
    # df_256 = pd.read_excel(file_256)
    df_256 = pd.read_excel(f"./../results/data_for_paper/second/{file_256}")
    results['mean_stretch_256'].append(df_256['stretch'].mean())
    results['mean_stretch_arrow_256'].append(df_256['stretch_arrow'].mean())
    
    # Load and aggregate data for 1024 nodes
    df_1024 = pd.read_excel(f"./../results/data_for_paper/second/{file_1024}")
    results['mean_stretch_1024'].append(df_1024['stretch'].mean())
    results['mean_stretch_arrow_1024'].append(df_1024['stretch_arrow'].mean())

# Create the plot
plt.figure(figsize=(640/100, 480/100), dpi=100)
plt.xticks(fontsize=9)

# Plotting the 4 lines
plt.plot([str(x) for x in categories], results['mean_stretch_1024'], marker='.', linestyle='-', label=f'Stretch$_{'O'}$$_{'P'}$$_{'A'}$$_{'r'}$$_{'r'}$$_{'o'}$$_{'w'} $(n = 1024)', color=cmap(0), linewidth=1)
plt.plot([str(x) for x in categories], results['mean_stretch_arrow_1024'], marker='v', linestyle='-.', label=f'Stretch$_{'A'}$$_{'r'}$$_{'r'}$$_{'o'}$$_{'w'} $(n = 1024)', color=cmap(1), linewidth=1)
plt.plot([str(x) for x in categories], results['mean_stretch_256'], marker='.', linestyle='-', label=f'Stretch$_{'O'}$$_{'P'}$$_{'A'}$$_{'r'}$$_{'r'}$$_{'o'}$$_{'w'}$ (n = 256)', color=cmap(2), linewidth=1)
plt.plot([str(x) for x in categories], results['mean_stretch_arrow_256'], marker='v', linestyle='-.', label=f'Stretch$_{'A'}$$_{'r'}$$_{'r'}$$_{'o'}$$_{'w'} $(n = 256)', color=cmap(3), linewidth=1)


# Labels and Formatting
plt.xlabel('Maximum Error Bound', fontsize=12)
plt.ylabel('Mean Stretch', fontsize=12)
plt.title('Maximum Error Bound vs Mean Stretch for $\# opr = 256$', fontsize=12)
plt.legend(loc='best')
# plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks([str(x) for x in categories])
plt.tight_layout()

# Save the plot
# plt.savefig('stretch_metrics_by_error_bound.png')
plt.show()

# Output the summary to CSV
# pd.DataFrame(results).to_csv('summary_error_bounds.csv', index=False)