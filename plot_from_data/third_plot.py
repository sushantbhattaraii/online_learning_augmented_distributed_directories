import pandas as pd
import matplotlib.pyplot as plt

# File mapping for each node count (using the raw CSV versions of the uploaded files)
file_mapping = {
    128: "128nodes_diameter77_cutoff2.5-repetitions50-overlap100.xlsx",
    256: "256nodes_diameter96_cutoff2.5-repetitions50-overlap100.xlsx",
    512: "512nodes_diameter96_cutoff2.5-repetitions50-overlap100.xlsx",
    1024: "1024nodes_diameter103_cutoff2.5-repetitions50-overlap100.xlsx"
}

node_sizes = [128, 256, 512, 1024]

# Initialize lists to store mean values
stats = {
    # 'stretch_f64': [],
    'stretch_f128': [],
    # 'stretch_arrow_f64': [],
    'stretch_arrow_f128': [],
    'stretch_parrow_f128': []
}
cmap = plt.get_cmap('tab20')

# Process each file to compute means
for n in node_sizes:
    df = pd.read_excel(f"./../results/internet_graphs/first_way/1/{file_mapping[n]}")
    
    # Calculate means for fraction 64
    # stats['stretch_f64'].append(df[df['fraction'] == 64]['stretch'].mean())
    # stats['stretch_arrow_f64'].append(df[df['fraction'] == 64]['stretch_arrow'].mean())

    # Calculate means for fraction 128
    stats['stretch_f128'].append(df[df['fraction'] == 128]['stretch'].mean())
    stats['stretch_arrow_f128'].append(df[df['fraction'] == 128]['stretch_arrow'].mean())
    stats['stretch_parrow_f128'].append(df[df['fraction'] == 128]['stretch_parrow'].mean())

# Create the plot
plt.figure(figsize=(2.35, 2.35*5/7), dpi=300)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

# Plotting the 4 line graphs
plt.plot([str(x) for x in node_sizes], stats['stretch_arrow_f128'], marker='v', linestyle='-.', label=f'Arrow', color=cmap(2), linewidth=1.1, markersize=4, zorder=2)
plt.plot([str(x) for x in node_sizes], stats['stretch_parrow_f128'], marker='^', linestyle=':', label=f'PArrow', color=cmap(4), linewidth=1.1, markersize=4, zorder=3)
plt.plot([str(x) for x in node_sizes], stats['stretch_f128'], marker='.', linestyle='-', label=f'OPArrow', color=cmap(0), linewidth=1.1, markersize=4, zorder=1)


# plt.plot([str(x) for x in node_sizes], stats['stretch_f64'], marker='.', linestyle='-', label=f'Stretch$_{'O'}$$_{'P'}$$_{'A'}$$_{'r'}$$_{'r'}$$_{'o'}$$_{'w'} $(#${'opr'}$ = 64)', color=cmap(2), linewidth=1)
# plt.plot([str(x) for x in node_sizes], stats['stretch_arrow_f64'], marker='v', linestyle='-.', label=f'Stretch$_{'A'}$$_{'r'}$$_{'r'}$$_{'o'}$$_{'w'} $(#${'opr'}$ = 64)', color=cmap(3), linewidth=1)


# Formatting the plot
plt.xlabel('Network Size ($n$)', fontsize=9, labelpad=2)
plt.ylabel('Stretch', fontsize=9, labelpad=2)
# plt.title('Network size vs Mean Stretch for err $\leq$ 0.0', fontsize=92)
plt.legend(loc='lower right', fontsize=8, frameon=True,
                borderpad=0.25,
                labelspacing=0.2,
                handletextpad=0.4,
                handlelength=2.2)
# plt.grid(False, which='both', linestyle='--', alpha=0.7)
plt.xticks([str(x) for x in node_sizes])
plt.tight_layout(pad=0.05)

# Save and display
# plt.savefig('stretch_metrics_plot.png')
plt.show()