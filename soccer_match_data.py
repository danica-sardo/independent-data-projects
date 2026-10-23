import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1 load dataset directly in python
data = {
    'player_id': ['P01', 'P02', 'P03', 'P04'],
    'position': ['Center Mid', 'Center Def', 'Forward', 'Winger'],
    'passes_completed': [45, 38, 14, 28],
    'passes_attempted': [50, 42, 22, 35],
    'tackle_success_pct': [0.82, 0.91, 0.45, 0.60],
    'distance_covered_km': [9.4, 7.8, 8.2, 10.1],
    'goal_contributions': [2, 0, 3, 1]
}

df = pd.DataFrame(data)

#2 calculate pass completion rate
df['pass_accuracy'] = (df['passes_completed'] / df['passes_attempted']) * 100

#3 compute weighted player impact score
# weights: pass accuracy (40%), tackle success (30%), goal contribution (30%)
df['impact_score'] = (
    (df['pass_accuracy'] * 0.4) +
    (df['tackle_success_pct'] * 100 * 0.3) +
    (df['goal_contributions'] * 10 * 0.3)
)

print("--- Player Performance Summary ---")
print(df[['player_id', 'position', 'pass_accuracy', 'impact_score']].sort_values(by='impact_score', ascending=False))

#4 visualize impact score across positions
plt.figure(figsize=(9, 5))
plt.bar(df['player_id'], df['impact_score'], color='royalblue', edgecolor='black')
plt.title('Player Impact Score Comparison')
plt.xlabel('Player ID')
plt.ylabel('Impact Score')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.savefig('player_impact_scores.png')
plt.show()