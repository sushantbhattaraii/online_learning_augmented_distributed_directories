import pandas as pd
import matplotlib.pyplot as plt

# File mapping for each node count (using the raw CSV versions of the uploaded files)
file_mapping = {
    128: "128nodes_diameter7_cutoffinf-repetitions50-overlap100.xlsx",
    256: "256nodes_diameter5_cutoffinf-repetitions50-overlap100.xlsx",
    512: "512nodes_diameter4_cutoffinf-repetitions50-overlap100.xlsx",
    1024: "1024nodes_diameter4_cutoffinf-repetitions50-overlap100.xlsx"
}

node_sizes = [128, 256, 512, 1024]

# Initialize lists to store mean values
stats = {
    'stretch_f64': [],
    'stretch_f256': [],
    'stretch_arrow_f64': [],
    'stretch_arrow_f256': []
}
cmap = plt.get_cmap('tab20')

# Process each file to compute means
for n in node_sizes:
    df = pd.read_excel(f"./../results/data_for_paper/third/{file_mapping[n]}")
    
    # Calculate means for fraction 64
    stats['stretch_f64'].append(df[df['fraction'] == 64]['stretch'].mean())
    stats['stretch_arrow_f64'].append(df[df['fraction'] == 64]['stretch_arrow'].mean())

    # Calculate means for fraction 256
    stats['stretch_f256'].append(df[df['fraction'] == 256]['stretch'].mean())
    stats['stretch_arrow_f256'].append(df[df['fraction'] == 256]['stretch_arrow'].mean())

# Create the plot
plt.figure(figsize=(640/100, 480/100), dpi=100)
plt.xticks(fontsize=9)

# Plotting the 4 line graphs
plt.plot([str(x) for x in node_sizes], stats['stretch_f256'], marker='.', linestyle='-', label=f'Stretch$_{'O'}$$_{'P'}$$_{'A'}$$_{'r'}$$_{'r'}$$_{'o'}$$_{'w'} $(#${'opr'}$ = 256)', color=cmap(0), linewidth=1)
plt.plot([str(x) for x in node_sizes], stats['stretch_arrow_f256'], marker='v', linestyle='-.', label=f'Stretch$_{'A'}$$_{'r'}$$_{'r'}$$_{'o'}$$_{'w'} $(#${'opr'}$ = 256)', color=cmap(1), linewidth=1)
plt.plot([str(x) for x in node_sizes], stats['stretch_f64'], marker='.', linestyle='-', label=f'Stretch$_{'O'}$$_{'P'}$$_{'A'}$$_{'r'}$$_{'r'}$$_{'o'}$$_{'w'} $(#${'opr'}$ = 64)', color=cmap(2), linewidth=1)
plt.plot([str(x) for x in node_sizes], stats['stretch_arrow_f64'], marker='v', linestyle='-.', label=f'Stretch$_{'A'}$$_{'r'}$$_{'r'}$$_{'o'}$$_{'w'} $(#${'opr'}$ = 64)', color=cmap(3), linewidth=1)


# Formatting the plot
plt.xlabel('Network Size ($n$)', fontsize=12)
plt.ylabel('Mean Stretch', fontsize=12)
plt.title('Network size vs Mean Stretch for err $\leq$ 0.0', fontsize=12)
plt.legend(loc='best', fontsize=9)
# plt.grid(False, which='both', linestyle='--', alpha=0.7)
plt.xticks([str(x) for x in node_sizes])
plt.tight_layout()

# Save and display
# plt.savefig('stretch_metrics_plot.png')
plt.show()