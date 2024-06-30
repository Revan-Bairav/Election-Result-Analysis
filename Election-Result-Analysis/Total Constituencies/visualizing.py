import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
csv_file_path = 'party_wise_results.csv'
df = pd.read_csv(csv_file_path)

# Convert columns to numeric (if they are not already)
df['Won'] = pd.to_numeric(df['Won'], errors='coerce')
df['Leading'] = pd.to_numeric(df['Leading'], errors='coerce')
df['Total'] = pd.to_numeric(df['Total'], errors='coerce')

# Set the style for seaborn
sns.set(style="whitegrid")

# Create a figure and axis
fig, ax = plt.subplots(figsize=(20, 15))

# Plot the total seats won by each party as a bar chart
sns.barplot(x='Party', y='Total', data=df, ax=ax, palette='viridis')

# Set the labels and title
ax.set_xlabel('Party')
ax.set_ylabel('Total Seats')
ax.set_title('Party-wise Total Seats in Election')

# Rotate the x labels for better readability
plt.xticks(rotation=90)

# Show the plot
plt.tight_layout()
plt.show()
