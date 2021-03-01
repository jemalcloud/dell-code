# We now need the json library so we can load and export json data
import json

from flask import Flask
    
app = Flask(__name__)

# We're using the new route that allows us to read a date from the URL
@app.route('/server/<serial>')
def server(serial):
    # Additionally, we're now loading the JSON file's data into file_data 
    # every time a request is made to this endpoint
    with open('./newservers.json', 'r') as jsonfile:
        file_data = json.loads(jsonfile.read())

       # for change in file_data['sn1003']:

        # strip the contents of trailing white spaces (new line)
           # change['hostname'] = change['hostname'].strip()
        

    # We can then find the data for the requested date and send it back as json
    return json.dumps(file_data[serial])

if __name__ == '__main__':
    app.run(debug=True)