# the next two lines always need to be atop this server.py file 
from collections import UserList
from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# all the @ stuff below will (later) be moved into separate files.  These will be replaced with controller import lines. 

# @app.route('/')          
# def welcome():
#     return render_template("index.html", horizDispCount = 1, vertDispCount = 1, color1 = "red", color2 = "black", displayValMsg = defaultValidationMsg, displayValStyle = defaultValStyle)


@app.route('/')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    
    randomNumbers = [3,1,5]

    StudentInfoList = [
        {'name' : 'MichaelangeloDonatelloLeonardoRaphael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]

    userlist = [
        {'firstName' : 'Michael', 'lastName' : 'Choi'},
        {'firstName' : 'John', 'lastName' : 'Supsupin'},
        {'firstName' : 'Mark', 'lastName' : 'Guillen'},
        {'firstName' : 'KB', 'lastName' : 'Tonel'}
        ,
        {'firstName' : 'Michael', 'lastName' : 'Choi'},
        {'firstName' : 'John', 'lastName' : 'Supsupin'},
        {'firstName' : 'Mark', 'lastName' : 'Guillen'},
        {'firstName' : 'KB', 'lastName' : 'Tonel'}
        ,
        {'firstName' : 'Michael', 'lastName' : 'Choi'},
        {'firstName' : 'John', 'lastName' : 'Supsupin'},
        {'firstName' : 'Mark', 'lastName' : 'Guillen'},
        {'firstName' : 'KB', 'lastName' : 'Tonel'}
        ,
        {'firstName' : 'Michael', 'lastName' : 'Choi'},
        {'firstName' : 'John', 'lastName' : 'Supsupin'},
        {'firstName' : 'Mark', 'lastName' : 'Guillen'},
        {'firstName' : 'KB', 'lastName' : 'Tonel'}
        ,
        {'firstName' : 'Michael', 'lastName' : 'Choi'},
        {'firstName' : 'John', 'lastName' : 'Supsupin'},
        {'firstName' : 'Mark', 'lastName' : 'Guillen'},
        {'firstName' : 'KB', 'lastName' : 'Tonel'}
    ]

    # return render_template("index.html", displayRandomNumbers = randomNumbers, displayStudentInfoList = StudentInfoList, displayUserList = userlist)
    return render_template("index.html", displayStudentInfoList = StudentInfoList, displayUserList = userlist)



"""DON'T TOUCH BELOW :-) below always needs to be at the bottom of the script, yes!"""
# below is stuff you oughta have, per TA Cameron Smith, from Coding Dojo: 

@app.route('/', defaults={'cookies': ''})
@app.route('/<path:cookies>')
def catch_all(cookies):
    return 'Sorry! No response here. Try url again.'

# below is flask boiler plate; exclude it and stuff won't work    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

