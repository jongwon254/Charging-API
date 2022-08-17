![charging](https://user-images.githubusercontent.com/36485235/185091905-56ef8c22-dde6-424c-98b7-f1fa3f2ae183.png)

# Charging Points API
Own REST API to provide charging point services to the [Charging Map](https://github.com/jongwon254/Charging-Map).

## Technologies
- Languages: Python, TypeScript, JavaScript, HTML, and CSS
- Backend: 
  - REST API built with Django and PostgreSQL
  - Data from the Bundesnetzagentur
- Frontend: 
  - Built with Angular, Bootstrap, and MapBox
  
## Functionality
- The API has three endpoints that allow for retrieving/searching all charging points, or creating/updating/deleting a charging point
- Data is stored in a PostgreSQL database
- API Connection: 
1. GET, POST: BASE_URL/CHARGING
    - PARAMETERS (POST): ID, OPERATOR, STREET, HOUSENUMBER, ZIPCODE, CITY, POWER, NUMBER_PORTS
    - RESPONSE: ID, OPERATOR, STREET, HOUSENUMBER, ZIPCODE, CITY, POWER, NUMBER_PORTS
2. GET, PUT, DELETE: BASE_URL/CHARGING/ID
    - PARAMETERS: ID
    - RESPONSE: ID, OPERATOR, STREET, HOUSENUMBER, ZIPCODE, CITY, POWER, NUMBER_PORTS
3. GET: BASE_URL/CHARGING/SEARCH
    - PARAMETERS: ONE OR MORE OF ID, OPERATOR, STREET, HOUSENUMBER, ZIPCODE, CITY, POWER, NUMBER_PORTS
    - RESPONSE: ID, OPERATOR, STREET, HOUSENUMBER, ZIPCODE, CITY, POWER, NUMBER_PORTS
    
## Screenshots
<img width="956" alt="pg" src="https://user-images.githubusercontent.com/36485235/185093688-c28d40b9-38d5-44be-924f-4f7f01fd54da.png">


## More Info
[Visit Website](https://jongwonlee.dev/charging-map)
