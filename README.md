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
2. Using the terminal window to run and update the below mentioned packages.
   sudo apt update
   sudo apt install python3-pip
   sudo apt install python3.10-venv
3. Create a new directory with Python3 as the environment.
   python3 -m venv {directory_name}
4. Enter inside the directory.
   source {directory_name}/bin/activate
5. Install libraries.
   sudo pip install pandas
   sudo pip install s3fs
   sudo pip install apache-airflow
   sudo pip install jupyter notebook
6. Create 2 new TCP connection(I personally use 8080 and 8888) in the Security section of EC2 instance, which is open connection.
## Step 2: Opening the airflow and jupyter notebook GUI:
1.  Run airflow standalone in your terminal , this will give us username and password.
   ![Screenshot 2023-08-17 200603](https://github.com/lordchan/ETL_pipeline-ApacheAirflow-AWS/assets/65250505/2b0ed9c7-f148-475a-a9cc-f58a023c69d7)

3.  Now open a new tab in browser and copy paste the Public IP4 DNS address (you can get this from AWS instance home page) and type in you port name seperated by colon. For example: {Public IP4 DNS address}:{port name}
4.  You will be shown Airflow user interface, which can be logged in using username and password.
   ![Screenshot 2023-08-18 191136](https://github.com/lordchan/ETL_pipeline-ApacheAirflow-AWS/assets/65250505/2055f835-7902-4da8-962a-4801acd0aab5)

6.  Open another terminal window from your EC2 machine. Run jupyter notebook, copy paste the IP address(Public IPv4) seperated by a new port number in another browser window. Again use the credentials to log in. Jupyter notebook is used to easily write python code and for user friendly interface. In the YouTube video however he has used VS code. Anything is fine, its upto your choice.
## Step 3: Setting up AWS S3 Bucket:
1. Set up a new S3 bucket.
2. Create IAM role to your EC2 and S3 accounts - which basically give free access for EC2 to dump files in S3.
3. Generate access key for S3 bucket.
4. Install AWS CLI
   sudo apt install awscli
5. After installing CLI, type - aws configure- and run. Provide the access code and secret key to get the secret token.
## Step 4: Generate API key from open weather website: 
You can go this link to generate one - [https://home.openweathermap.org/api_keys]
## Step 5: Start coding!
1.  Once you have opened jupyter notebook, create a new folder in airflow directory, inside this folder create a python file and start writing the code to set up dag and create tasks.
2.  In Airflow home page you will be seeing a new dag created. Which has 3 tasks: 1. checking whether the HTTP sensor is able to communicate with the website. 2. Extracting the data. 3. Transforming and loading it into S3 bucket.
3.  Create a new connection in Airflow, which will connect with the open weather website.
    Go to Airflow home page>admin>connections
    ![Screenshot 2023-08-18 191136](https://github.com/lordchan/ETL_pipeline-ApacheAirflow-AWS/assets/65250505/71b6adc5-90df-49e8-b66e-eabb086b2b08)
    Create a new connection like this
    ![Screenshot 2023-08-18 192925](https://github.com/lordchan/ETL_pipeline-ApacheAirflow-AWS/assets/65250505/3cd45b6b-39a6-4007-b24d-30724b6feb08)
4. The HTTP connection endpoint is written in the dag code which is in the form
   https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
   You can change the city name.
6.  After the data is transformed, we can save it as csv file in S3, by passing the location and aws credentials.
7.  Now run this dag, resolve the bugs and voila! You have successfully created an entire ETL pipeline.
8.  You will be seeing a csv file in your S3 bucket.
   ![Screenshot 2023-08-18 193433](https://github.com/lordchan/ETL_pipeline-ApacheAirflow-AWS/assets/65250505/d98730f7-1c11-4afe-a126-0b22f6b36673)

 The Final DAG workflow will look like this:
 ![Screenshot 2023-08-18 193616](https://github.com/lordchan/ETL_pipeline-ApacheAirflow-AWS/assets/65250505/4c521129-9512-4e9c-ba91-3fbd261190d7)

