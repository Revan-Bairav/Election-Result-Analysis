#importing libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

#Getting request to access the url
url='https://results.eci.gov.in/PcResultGenJune2024/index.htm'
html=requests.get(url)
print(html.text)

#heading into results
soup= BeautifulSoup(html.content,'html.parser')
table = soup.find('table', class_='table')



#Extracting data and converting into a csv file

parties = []
won = []
leading = []
total = []

for row in table.find('tbody').find_all('tr'):
    columns = row.find_all('td')
    party = columns[0].text.strip()
    won_count = columns[1].text.strip()
    leading_count = columns[2].text.strip()
    total_count = columns[3].text.strip()

    parties.append(party)
    won.append(won_count)
    leading.append(leading_count)
    total.append(total_count)


#storing data in csv file
data = {
    'Party': parties,
    'Won': won,
    'Leading': leading,
    'Total': total
}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_file_path = 'party_wise_results.csv'
df.to_csv(csv_file_path, index=False)

print(f'Data has been successfully saved to {csv_file_path}')