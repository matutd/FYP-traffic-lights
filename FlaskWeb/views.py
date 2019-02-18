#Import Flask module and create web server 
#render_template allows for html files to be searched in the template folder
from flask import Flask, render_template
 	

app = Flask(__name__)  					#__name__ mean this file i.e. main.py

@app.route("/")							#Default page to show with nothing after the slash
def home():								#define the default page
    return render_template("home.html")	#return html file

@app.route("/about")					#create new root for server at /about
def about():
    return render_template("about.html")
	
if __name__ == "__main__":				#assign script name to __main__ while script is running
    app.run(debug=True)					#show errors on webpage - allows easier debugging 