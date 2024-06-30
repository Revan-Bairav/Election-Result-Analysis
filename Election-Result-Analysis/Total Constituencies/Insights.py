# Insight 1: Total Seats Won by Each Party
total_seats = df[['Party', 'Total']].set_index('Party')

# Insight 2: Percentage of Total Seats Won by Each Party
total_seats['Percentage'] = (total_seats['Total'] / total_seats['Total'].sum()) * 100

# Insight 3: Top 5 Parties by Total Seats Won
top_5_parties = total_seats.sort_values(by='Total', ascending=False).head(5)



print(total_seats,top_5_parties)

