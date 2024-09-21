import requests
import csv
import os.path

url = 'https://www.wozwaardeloket.nl/wozwaardeloket-api/v1/wozwaarde/nummeraanduiding/0983010000152150'
cookies = {"LB_STICKY": "42be11828cf8a109", "JSESSIONID": "9B44B8A50AADEA765FBAF6D96267F3FE"}

# Retrieve data and change format
response = requests.get(url, cookies=cookies)
data = response.json()

wozobject = data.get('wozObject')
wozwaarden = data.get('wozWaarden')

# Create empty list to append categories
wozwaarden_list = []

# Loop over dictionary (in list) with all woz-values
for dictionary in wozwaarden:
    value = dictionary['vastgesteldeWaarde']
    wozwaarden_list.append(value)

# Write code to see if file exists
file_exists = os.path.isfile("wozwaardenloket-output.csv")

# Create new csv file to add data to
with open("wozwaardenloket-output.csv", "a", newline='') as file:
    writer = csv.writer(file, delimiter=',', dialect='unix')
    headers = ["woz2023", "woz2022", "woz2021", "woz2020", "woz2019", "woz2018", "woz2017", "woz2016", "woz2015", "woz2014"]

    # Only add headers when the file is newly created
    if not file_exists:
        # Assuming the header needs to be a generic header, as we don't know exact fieldnames
        writer.writerow(headers)

    # Write the entire list in one row
    writer.writerow(wozwaarden_list)

print('WOZ information retrieved!')

#limburg 0983010000152150
#haarlem 0392200000021580
#friesland 0080200011085401
#NUMMERAANDUIDING
