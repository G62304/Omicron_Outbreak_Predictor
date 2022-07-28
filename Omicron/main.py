from bs4 import BeautifulSoup as bs
import urllib.request
import numpy as np
import pandas as pd
from pandas.io.html import read_html
import requests

weburl = urllib.request.urlopen('https://www.statista.com/statistics/1279100/number-omicron-variant-worldwide-by-country/')
data = weburl.read()
soup = bs(data, 'lxml')
country_tags = soup.find_all('td')
countries = []
num_of_cases = []
a = 2

for i in list(country_tags):
    if a % 2 == 0:
        countries.append(i.text)
        a += 1
    elif a % 2 == 1:
        num_of_cases.append(i.text)
        a += 1
countries.remove('\n                                                        $39 per month*\n                        \n                                (billed annually)\n                            ')
countries.remove('\n                            Purchase now\n                        ')
for i in range(7):
    countries.remove('')
num_of_cases.remove( '\n                        Free\n                    ')
num_of_cases.remove('\n                            Register\n                        ')
for i in range (6):
    num_of_cases.remove('')

weburl2 = urllib.request.urlopen('https://statisticstimes.com/demographics/countries-by-population-density.php')
data2 = weburl2.read()
soup2 = bs(data2, 'lxml')
density_tags = soup2.find_all('td', class_='data')
density = []

country2_tags = soup2.find_all('td', class_='name')
countries2 = []

b = 3
for i in list(density_tags):
    if b % 3 == 0:
        density.append(i.text)
        b += 1
    else:
        b += 1
c = 2
for i in list(country2_tags):
    if c % 2 == 0:
        countries2.append(i.text)
        c += 1
    elif c % 2 == 1:
        c += 1
density = density[:235]
countries2 = countries2[:235]

df = pd.DataFrame(dict(Country = countries2, Population_Density = density))
df = df.sort_values(by = ['Country'])
df = df.set_axis(sorted(countries2), axis = 'index')

countries3 = ['United States', 'Moldova', 'British Virgin Islands', 'North Macedonia', 'Aruba', 'Curacao', 'Bonaire', 'Saint Martin', 'Sint Maarten', 'Vietnam', 'Iran', 'Venezuela', 'Brunei', 'Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Republic of the Congo', 'Réunion', 'Romania', 'Russia', 'Rwanda', 'Saint Barthélemy', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Korea', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Tajikistan', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Viet Nam', 'Yemen', 'Zambia', 'Zimbabwe']
countries3 = sorted(countries3)

for i in countries3:
    if (i not in countries):
        df = df.drop(i)
for i in countries:
    if (i not in countries3) and (i != 'USA') and (i != 'Reunion'):
        df = df.drop(i)
x = df['Country'].values.tolist()
for i in x:
    if i not in countries:
        df = df.drop(i)

df1 = pd.DataFrame(dict(Country = countries, Number_of_Cases = num_of_cases))
df1 = df1.sort_values(by = ['Country'])
for i in countries:
    if (i not in countries3) and (i != 'USA') and (i != 'Reunion'):
        df1 = df1.drop(i)

df1 = df1.set_axis(sorted(countries), axis = 'index')

for i in df1.loc[:, 'Country']:
    if i not in df.loc[:, 'Country']:
        df1 = df1.drop(i)
df1 = df1.drop('Country', axis = 1)

number_of_cases = df1['Number_of_Cases'].values.tolist()

df.insert(2, "Number_of_Cases", number_of_cases, True)

df = df.reset_index()
df = df.drop("index", axis = 1)

pd.set_option("display.max_rows", None, "display.max_columns", None)

Pop_Dense = df['Population_Density'].values.tolist()
Num_Case = df['Number_of_Cases'].values.tolist()
Pop_Dense2 = []
Num_Case2 = []
for i in Pop_Dense:
    if ',' in i:
        i = i.replace(',', '')
    Pop_Dense2.append(float(i))
for i in Num_Case:
    if ',' in i:
        i = i.replace(',', '')
    Num_Case2.append(float(i))

df = df.drop('Population_Density', axis = 1)
df = df.drop('Number_of_Cases', axis = 1)
df['Population_Density'] = Pop_Dense2
df['Number_of_Cases'] = Num_Case2

df['Outbreak_Rating'] = (df['Population_Density'] * df['Number_of_Cases'])/1000
df = df.sort_values(by = ['Outbreak_Rating'], ascending= False)
print(df)

"""
weburl3 = 'https://en.wikipedia.org/wiki/List_of_countries_by_past_and_projected_GDP_(nominal)'
table_name = 'sortable wikitable jquery-tablesorter' 

response = requests.get(weburl3)
soup3 = bs(response.text, 'html.parser')
soup_table = soup.find('table', {'class':table_name})
gdp_df = pd.read_html(str(soup_table))
"""