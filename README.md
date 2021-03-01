# REST API server using a python Flask 

#### Step 1 
##### Bootstrap the server csv file, read the data and dump them into JSON file.

```bash
python -m bootstrap.py 
```
##### The above command will generate / output newservers.json file in the project directory.

#### Step 2 

##### In this step, leverage the json file output from step 1 and create a route that allows us to read a server serial number from the URL. 

```bash
python -m app.py
```
##### Upon executing the above python script , the json data will loaded up and accessible on , 
```
http://127.0.0.1:5000/server/{serial}
Example : http://127.0.0.1:5000/server/sn1003
```
