from flask import Flask, render_template, render_template_string, request
import sys
import GmlToJson as gtj

import getFriends
 
app = Flask(__name__)      



#@app.route('/')
#@app.route('/<g>')
#def home(g = None):
  #return render_template('/home.html', g = gh.returnGraph())



@app.route('/',methods=['GET', 'POST'])
def home(g = None, l = None, n = None):
    if request.method == 'POST':

        id = getFriends.main()

        list_of_people = gtj.convert_gml_to_js(id)
        number_of_communities = gtj.count_communities(list_of_people)


        return render_template('/Test.html', g = id, l = list_of_people, n = number_of_communities)



    return render_template('/home.html')

@app.route('/about')
def about():
  return render_template('/about.html')

@app.route('/test')
def graph(g = None):
    id = getFriends.main()
    gtj.convert_gml_to_js(id)
    return render_template('/Test.html', g = id)

 
if __name__ == '__main__':
      app.run(debug=True)