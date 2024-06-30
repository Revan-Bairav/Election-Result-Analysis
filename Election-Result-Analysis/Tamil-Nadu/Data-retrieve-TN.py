#importing libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


#Getting request to access the url
url='https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S22.htm'
html=requests.get(url)
print(html.text)


#heading into results
soup1= BeautifulSoup(html.content,'html.parser')
table1 = soup1.find('table', class_='table')





#Extracting data

Tamil_Naduparties = []
won_TamilNadu = []
total_TamilNadu = []


for row in table.find('tbody').find_all('tr'):
    columns = row.find_all('td')
    partys = columns[0].text.strip()
    won_counts = columns[1].text.strip()
    total_counts = columns[3].text.strip()

    Tamil_Naduparties.append(partys)
    won_TamilNadu.append(won_counts)
    total_TamilNadu.append(total_counts)

#storing data in csv file
datas = {
    'Party': Tamil_Naduparties,
    'Won': won_TamilNadu,
    'Total': total_TamilNadu
}
df = pd.DataFrame(datas)

# Save the DataFrame to a CSV file
csv_file_path = 'TamilNadu_party_wise_results.csv'
df.to_csv(csv_file_path, index=False)

csv_file_paths = 'TamilNadu_party_wise_results.csv'
df = pd.read_csv(csv_file_paths)