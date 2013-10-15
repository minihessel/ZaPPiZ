from flask import Flask, render_template, render_template_string, request
import sys
import GmlToJson as gtj

import getFriends
 
app = Flask(__name__)      



#@app.route('/')
#@app.route('/<g>')
#def home(g = None):
  #return render_template('/home.html', g = gh.returnGraph())



@app.route('/',methods=['get', 'POST'])
def home(g = None, l = None, n = None, c = None):
    if request.method == 'POST':
        id = getFriends.main()
        list_of_people = gtj.convert_gml_to_js(id)
        number_of_communities = gtj.count_communities(list_of_people)
        #Group colors
        colors = ["#1f77b4", "#aec7e8", "#ff7f0e", "#ffbb78", "#2ca02c", "#98df8a", "#d62728", "#ff9896", "#9467bd", "#c5b0d5", "#8c564b", "#c49c94", "#e377c2", "#f7b6d2", "#7f7f7f", "#c7c7c7", "#bcbd22", "#dbdb8d", "#17becf", "#9edae5"]
        return render_template('/Test.html', g = id, l = list_of_people, n = number_of_communities, c = colors)



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