## Retrieve Weather Data
This project has been submitted as an assignment.
##### Task
Create a Django app store and retrieve weather data from [UK Metoffice](https://www.metoffice.gov.uk/climate/uk/summaries/datasets#Yearorder) for locations:
- *UK*
- *England*
- *Wales*
- *Scotland* 

based on following metrics:
- *Tmax* (max temperature)
- *Tmin* (min temperature)
- *Rainfall*

The data is scrapped into JSON and stored at AWS S3.
The url format on S3 is:
https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/{metric}-{location}.json
E.g:
https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Rainfall-England.json
#### Requirements:
- Django==2.1.5
- Python==3.6.7
- djangorestframework==3.9.1
- mysqlclient==1.4.2.post1
- django-mysql==2.4.1

#### Configuring MySQL:
For MySQL support, replace `DATABASES` dictionary in `settings.py` file with:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },
    }
}
```
Also, create the `/path/to/my.cnf` file with settings:
```
[client]
database = DB_NAME
host = localhost
user = DB_USER
password = DB_PASSWORD
default-character-set = utf8
```

#### Execution steps:
##### 1. Store Data using Management Command
Following custom django management command fetches data from S3 urls for above locations & metrics and store in models. 
```
python manage.py store_data
```
##### 2. Retrieve Data via REST API
Return weather data of a metric between start date and end date for a particular location. 

* **Endpoint**
 */api/*
* **Method:**
  `GET`
*  **URL Params**

   *Required:*
   
   `start_date=[DD-MM-YYYY]`
   
    `end_date=[DD-MM-YYYY]`
    
   `metric_type=Tmax|Tmin|Rainfall`
   
   `location=UK|England|Wales|Scotland`
   
*  **Sample Call**
`/api/?start_date=01-02-1999&end_date=01-02-2019&metric_type=Tmax&location=UK`











