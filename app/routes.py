from flask import Flask, render_template, render_template_string
import network
import sys
import xml.etree.ElementTree as ET
 
app = Flask(__name__)      



#@app.route('/')
#@app.route('/<g>')
#def home(g = None):
  #return render_template('/home.html', g = gh.returnGraph())




@app.route('/')
def home():

  image = network.test()


  return render_template('/image.html')

@app.route('/about')
def about():
  return render_template('/about.html')
 
if __name__ == '__main__':
  app.run(debug=True)
