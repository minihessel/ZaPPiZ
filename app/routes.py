from flask import Flask, render_template, render_template_string, request
import sys
import GraphAnalyzer as gtj

import getFriends
 
app = Flask(__name__)      




#Routing method for the home page.
######### PARAMS ##########
# g = the id of an user
# l = list of people
# n = number of communities
# c = colors that should be used when painting the graph
@app.route('/')
def home():


    return render_template('/home.html')



#Renders the about page
@app.route('/about')
def about():
  return render_template('/about.html')

#Renders the test page
# g = id
@app.route('/graph',methods=['get', 'POST'])
def test(f_id = None, list_of_people = [], communities = None, c = None, most_important = None, smallest_node = None , test = None):
    if request.method == 'POST':

        if request.form['btnStart'] !=None:

            friend_id = getFriends.main()
            list, graph = gtj.convert_gml_to_js(friend_id) # gets an easy readable list of people and the graph for further analyzes
            most_important_node  = gtj.find_imporant_node(graph)
            find_smallest_node = gtj.find_smallest_node(graph)
            number_of_communities = gtj.count_communities(list)
            colors = ["#1f77b4", "#aec7e8", "#ff7f0e", "#ffbb78", "#2ca02c", "#98df8a", "#d62728", "#ff9896", "#9467bd", "#c5b0d5", "#8c564b", "#c49c94", "#e377c2", "#f7b6d2", "#7f7f7f", "#c7c7c7", "#bcbd22", "#dbdb8d", "#17becf", "#9edae5"]
            return render_template('/graph.html', f_id = friend_id, list_of_people = list,communities = number_of_communities, c = colors, most_important = most_important_node,smallest_node = find_smallest_node)
    return render_template('/home.html')


 
if __name__ == '__main__':
      app.run(debug=True)