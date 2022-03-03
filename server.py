# the next two lines always need to be atop this server.py file 
from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# all the @ stuff below will (later) be moved into separate files.  These will be replaced with controller import lines. 

# @app.route('/')          
# def welcome():
#     return render_template("index.html", horizDispCount = 1, vertDispCount = 1, color1 = "red", color2 = "black", displayValMsg = defaultValidationMsg, displayValStyle = defaultValStyle)


@app.route('/')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("index.html", random_numbers = [3,1,5], students = student_info)



"""DON'T TOUCH BELOW :-) below always needs to be at the bottom of the script, yes!"""
# below is stuff you oughta have, per TA Cameron Smith, from Coding Dojo: 

@app.route('/', defaults={'cookies': ''})
@app.route('/<path:cookies>')
def catch_all(cookies):
    return 'Sorry! No response here. Try url again.'

# below is flask boiler plate; exclude it and stuff won't work    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

