# ETL_pipeline_airflow
In this Project I have extracted weather data from [https://openweathermap.org/api] transformed it on Apache Airflow and loaded it into AWS S3 bucket. All this is done on EC2 machine.
Here I have mentioned step-by-step process of building an ETL (Extract, Transform and Load) Pipeline from scratch. 

## Outcome of the project.
To get a csv file in AWS S3 where we have the most recent weather details of Banglore (or any other city) like temperature, humidity, pressure etc.

## Tools used:
Apache Airflow, Python programming,
AWS cloud computing (S3, EC2),
Linux based SSH commands.

## Credits:
The project is demonstrated by Tuplespectra on his Youtube channel [https://www.youtube.com/watch?v=uhQ54Dgp6To&t=1703s]. A big tank you!

So let us begin!

## Step 1: Setting up the required tools and libraries:
1. Set up an EC2 account in AWS. Select Linux based OS with atleast 2GB of memory. I chose t2.small.
2. 


