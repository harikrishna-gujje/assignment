# assignment
This project is about creating a django rest api to post data on a webpage and return the results in json format.

How to use:

Install the required libraries using requirements.txt

git clone the repository and run the server

go to localhost:8000/api/search and give the sanctionsearch list details in json format.

the web server will take the request and verifies it through a serializer which is created based on a model.

after successful validation, it will post the same data in https://sanctionssearch.ofac.treas.gov/ using selenium web driver and gathers the results.

the same result will be returned to the user.

example:

if we give,
    {
        "Type": "All",
        "Name": "david",
        "Address": null,
        "City": null,
        "ID_Field": null,
        "State": null,
        "Program": "All",
        "Country": "All",
        "MinNameScore": 100,
        "List": "All"
    }
   
result will be sanctionedsearch results in json format with matching the required criteria.

[{'Name': 'CABELLO RONDON, Jose David', 'Address': ' ', 'Type': 'Individual', 'Programs': 'VENEZUELA', 'List': 'SDN', 'Score': '100'}, {'Name': 'CHAPFIKA, David', 'Ad
dress': ' ', 'Type': 'Individual', 'Programs': 'ZIMBABWE', 'List': 'SDN', 'Score': '100'}, {'Name': 'DAVID, Andoson', 'Address': ' ', 'Type': 'Individual', 'Programs'
: 'DPRK3', 'List': 'SDN', 'Score': '100'}, {'Name': 'DE LIMA SALAS, David Eugenio', 'Address': 'Villas Martinique Casa 131 El Morro', 'Type': 'Individual', 'Programs'
: 'VENEZUELA', 'List': 'SDN', 'Score': '100'}, {'Name': 'FERRARI, Sergio David', 'Address': 'Chivilcoy 3157 Piso 2 Depto D', 'Type': 'Individual', 'Programs': 'SDNTK'
, 'List': 'SDN', 'Score': '100'}, {'Name': 'GOMEZ ORTIZ, David', 'Address': 'c/o GESTORES DEL ECUADOR GESTORUM S.A.', 'Type': 'Individual', 'Programs': 'SDNTK', 'List
': 'SDN', 'Score': '100'}, {'Name': 'GOTMAN, David', 'Address': ' ', 'Type': 'Individual', 'Programs': 'CYBER2', 'List': 'SDN', 'Score': '100'}, {'Name': 'GUBERMAN, D
avid', 'Address': ' ', 'Type': 'Individual', 'Programs': 'CYBER2', 'List': 'SDN', 'Score': '100'}, {'Name': 'HERNANDEZ GRISALES, Jesus David', 'Address': ' ', 'Type':
 'Individual', 'Programs': 'SDNTK', 'List': 'SDN', 'Score': '100'}, {'Name': 'HODWALKER MARTINEZ, Martin David', 'Address': ' ', 'Type': 'Individual', 'Programs': 'SD
NT', 'List': 'SDN', 'Score': '100'}, {'Name': 'KYAGULANYI, David', 'Address': ' ', 'Type': 'Individual', 'Programs': 'DRCONGO', 'List': 'SDN', 'Score': '100'}, {'Name
': 'MAYER, David', 'Address': ' ', 'Type': 'Individual', 'Programs': 'SDGT', 'List': 'SDN', 'Score': '100'}, {'Name': 'NASSER DAVID, Julio Cesar', 'Address': 'Calle 7
4 No. 53-30', 'Type': 'Individual', 'Programs': 'SDNT', 'List': 'SDN', 'Score': '100'}, {'Name': 'PARIRENYATWA, David Pagwese', 'Address': 'P.O. Box 66222; Kopje', 'T
ype': 'Individual', 'Programs': 'ZIMBABWE', 'List': 'SDN', 'Score': '100'}, {'Name': 'RUBIO CONDE, David', 'Address': ' ', 'Type': 'Individual', 'Programs': 'SDNTK',
'List': 'SDN', 'Score': '100'}, {'Name': 'RUBIO GONZALEZ, David Nicolas', 'Address': ' ', 'Type': 'Individual', 'Programs': 'VENEZUELA-EO13850', 'List': 'SDN', 'Score
': '100'}, {'Name': 'SWORD OF DAVID', 'Address': ' ', 'Type': 'Entity', 'Programs': 'FTO; SDGT', 'List': 'SDN', 'Score': '100'}, {'Name': 'THE RABBI MEIR DAVID KAHANE
 MEMORIAL FUND', 'Address': ' ', 'Type': 'Entity', 'Programs': 'FTO; SDGT', 'List': 'SDN', 'Score': '100'}, {'Name': 'TUITO, David', 'Address': ' ', 'Type': 'Individu
al', 'Programs': 'SDNTK', 'List': 'SDN', 'Score': '100'}, {'Name': 'USUGA DAVID, Dairo Antonio', 'Address': ' ', 'Type': 'Individual', 'Programs': 'SDNTK', 'List': 'S
DN', 'Score': '100'}, {'Name': 'USUGA DAVID, Juan de Dios', 'Address': ' ', 'Type': 'Individual', 'Programs': 'SDNTK', 'List': 'SDN', 'Score': '100'}]

