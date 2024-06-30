# Plotting
plt.figure(figsize=(10, 10))
plt.pie(df['Won'], labels=df['Party'], autopct='%1.1f%%', startangle=140, colors=plt.cm.tab10.colors)
plt.title('Seats Won by Parties')
plt.axis('equal')  
plt.tight_layout()
plt.show()