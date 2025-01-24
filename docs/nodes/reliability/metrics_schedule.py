# Code used to generate the `metrics-schedule.png` illustration.

import matplotlib.pyplot as plt
import numpy as np

# Parameters for the network
num_nodes = 10
num_minutes = 60
num_hours = 3  # Number of hours to show in subplots

# Generate a random plan for each hour
plans = []
np.random.seed(42)  # For reproducibility
for hour in range(num_hours):
    plan = np.zeros((num_nodes, num_minutes))
    for node in range(num_nodes):
        connection_time = np.random.choice(num_minutes, size=1, replace=False)
        plan[node, connection_time] = 1
    plans.append(plan)

# Define a custom list of colors if tab10 is unavailable
colors = [
    "#1f77b4",
    "#ff7f0e",
    "#2ca02c",
    "#d62728",
    "#9467bd",
    "#8c564b",
    "#e377c2",
    "#7f7f7f",
    "#bcbd22",
    "#17becf",
]

# Plotting the plans for each hour with more compact subplots
fig, axes = plt.subplots(num_hours, 1, figsize=(12, 2 * num_hours), sharex=True)

for i, (plan, ax) in enumerate(zip(plans, axes)):
    for node in range(num_nodes):
        connection_times = np.where(plan[node] == 1)[0]
        ax.scatter(
            connection_times,
            [i] * len(connection_times),
            color=colors[node % len(colors)],
            label=f"Node {node+1}" if i == 0 else None,
        )

    ax.set_title(f"Measurement Plan - Hour {i + 1}", fontsize=12)
    ax.set_yticks([i])  # Only show the current hour on the y-axis
    ax.set_yticklabels([f"Hour {i + 1}"])
    ax.grid(axis="x", linestyle="--", linewidth=0.5)

# Add labels and legend
axes[-1].set_xlabel("Minutes of the Hour", fontsize=12)
fig.legend(
    loc="upper center",
    ncol=num_nodes,
    title="Nodes",
    fontsize=10,
    bbox_to_anchor=(0.5, -0.1),
)
fig.tight_layout()
plt.show()
