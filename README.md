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
The project is demonstrated by Tuplespectra on his Youtube channel. A big tank you!

So let us begin!

## Step 1: Setting up the required tools and libraries:
1. Set up an EC2 account in AWS. Select Linux based OS with atleast 2GB of memory. I chose t2.small.
2. Using the command line interface run and update the below mentioned packages.
3. Update the system, install Python3 pip, install python![Screenshot 2023-08-17 195817](https://github.com/lordchan/ETL_pipeline_airflow/assets/65250505/f97da785-f12d-4a00-8b53-84cf91ab16dd)
3.10 virtual environment.
4. Create a new directory with Python3 as the environment.
5. In this directory install Pandas library, Apache Airflow and Jupyter notebook.
## Step 2: Opening the airflow and jupyter notebook GUI:
1.  Run airflow standalone, this will give us username and password. Now open a new tab in browser and copy paste the Public IP4 DNS address (you can get this from AWS instance home page) and type in you port name seperated by colon. You will be shown Airflow user interface, which can be logged in using username and password.
2.  Open another terminal window from your EC2 machine. Run jupyter notebook, copy paste the IP address(Public IPv4) seperated by port no. in another browser window. Again use the credentials to log in. Jupyter notebook is used to easily write python code and for user friendly interface. In the YouTube video however he has used VS code. Anything is fine, its upto your choice.
## Step 3: Setting up AWS S3 Bucket:
1. Set up a new S3 bucket.
2. Create IAM role to your EC2 and S3 accounts - which basically give free access for EC2 to dump files in S3.
3. Generate access key for S3 bucket.
4. Install AWS CLI and use the access code and secret key to get the secret token.
## Step 4: Generate API key from open weather website: 
You can go this link to generate one - [https://home.openweathermap.org/api_keys]
## Step 5: Start coding!
1.  Once you have opened jupyter notebook, create a new folder in airflow directory, inside this folder create a python file and start writing the code to set up dag and create tasks.
2.  In Airflow home page you will be seeing a new dag created. Which has 3 tasks: 1. checking whether the HTTP sensor is able to communicate with the website. 2. Extracting the data. 3. Transforming and loading it into S3 bucket.
3.  Create a new connection in Airflow, which will connect with the open weather website.
4.  After the data is transformed, we can save it as csv file in S3, by passing the location and aws credentials.
5.  Now run this dag, resolve the bugs and voila! You have successfully created an entire ETL pipeline.
6.  You will be seeing a csv file in your S3 bucket.

