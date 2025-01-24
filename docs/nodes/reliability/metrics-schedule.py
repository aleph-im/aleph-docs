# Code used to generate the `metrics-schedule.png` illustration.

# Plotting the plans for each hour with more compact subplots
fig, axes = plt.subplots(num_hours, 1, figsize=(12, 2 * num_hours), sharex=True)

# Colors for nodes
colors = plt.cm.tab10(np.linspace(0, 1, num_nodes))

for i, (plan, ax) in enumerate(zip(plans, axes)):
    for node in range(num_nodes):
        connection_times = np.where(plan[node] == 1)[0]

        ax.scatter(connection_times, [i] * len(connection_times), color=colors[node],
                   label=f"Node {node + 1}" if i == 0 else None)

    ax.set_title(f"Measurement Plan - Hour {i + 1}", fontsize=12)
    ax.set_yticks([i])  # Only show the current hour on the y-axis
    ax.set_yticklabels([f"Hour {i + 1}"])
    ax.grid(axis='x', linestyle='--', linewidth=0.5)

# Add labels and legend

axes[-1].set_xlabel("Minutes of the Hour", fontsize=12)
fig.legend(loc='upper center', ncol=num_nodes, title="Nodes", fontsize=10, bbox_to_anchor=(0.5, -0.1))
fig.tight_layout()
plt.show()