# assignment
This project is about creating a django rest api to post data on a webpage and return the results in json format.

How to use:

Install the required libraries using requirements.txt

git clone the repository and run the server

go to localhost:8000/api/search and give the sanctionsearch list details in json format.

the web server will take the request and verifies it.

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
