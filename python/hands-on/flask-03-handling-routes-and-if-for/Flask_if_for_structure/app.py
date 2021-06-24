# Import Flask modules
from flask import Flask, render_template
# Create an object named app 
app = Flask(__name__)
# Create a function named head which shows the massage as "This is my first conditions experience" in `index.html` 
# and assign to the route of ('/')
@app.route('/')
def head() : 
    first = "This is my first conditions experience"
    return render_template('index.html', message = first)

# Create a function named header which prints the items 1 to 10 one by one in `index.html` 
# and assign to the route of ('/')
@app.route('/vincenzo')
def header() :
    names = ['marcus', 'stephaine', 'marie', 'thomas', 'boyka']
    return render_template('body.html', object = names)

if __name__ == '__main__' :
    # app.run(debug = True) # Kodu localda calistirmamizi saglar
    app.run(host = "0.0.0.0", port=80) # Kodun EC2 makinede calistirmamizi saglar
