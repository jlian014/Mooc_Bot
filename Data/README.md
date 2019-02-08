# Dataset Preparation

> The notebook in this folder includes the code for collecting Udemy data

### 1. Udemy API
The Udemy Affiliate API exposes a lot of functionalities of Udemy to help developers build client applications and integrations with Udemy.

It is organized around REST. Their API is designed to have predictable, resource-oriented URLs and to use HTTP response codes to indicate API errors. They use built-in HTTP features, like HTTP authentication and HTTP verbs, which can be understood by off-the-shelf HTTP clients. They only accept https calls to the API. All responses will be returned in JSON format, including errors.

Udemy Affiliate API is currently at version 2.0 and the root endpoint is https://www.udemy.com/api-2.0/ for all resources.

[More Information about Udemy API please click here.](https://www.udemy.com/developers/affiliate/)

### 2. Data Dictionary

> Data Dictionary of the final dataframe.

|Column Name|Data type|Description|
| --- | --- | --- |
|id|int|Course ID |
|avg_rating_recent|float|The average ratings for the course|
|objectives_summary|object|Objective summary of the course|
|num_subscibers|int|The number of people who subscribe the course|
|content_info|object|The Length of course or number of quiz/questions
|headline|object|The headlines of the course
|image_304x171|object|Link to the course thumbnail|
|title|object|The title of the course
|url|object|The Link to the Udemy website
|language|object|The Language that the instructor used in the course|
|category|object|The course category

### 3. Postgres Database on AWS instance
The code in the notebook has ran in the AWS instance, the collected data are stored in the Postgres Database using [this sql file](./udemy.sql). This will prevent the data collecting process takes up the RAM memories in the local machine.

#### Step 1. Initiate the docker installed AWS instance 
 *Copy and paste the following text into Advanced Details when you set up a AWS instance*
 
 ```#!/bin/bashcurl -sSL https://get.docker.com/ | shusermod -aG docker ubuntu```
#### Step 2. Configure a postgres server with docker

```docker pull postgres```
```docker run -d --name this_postgres -v pg-dbstore:/var/lib/postgresql/data -p 5432:5432postgres ```

#### Step 3. Copy `.sql`  and `.csv ` to the docker Postgres container

```docker cp udemy.sql this_postgres:/udemy.sql```

```docker cp udemy.csv this_postgres:/udemy.csv```


#### Step 4. Run the `.sql` file in the  Postgres server
```docker exec this_postgres psql -U postgres -d postgres -a -f udemy.sql```

#### Step 5.  Access the database server side to check the existance of data

``` docker exec -it this_postgres psql postgres postgres```

#### 4. Retrieve the Data

```
IP_ADDRESS = AWS IP
DBNAME = Database Name
USER = 'postgres'
PASSWORD = Your password for the postgres
```
Access the database using `psycopg2` from the Python. 