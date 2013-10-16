# -*- coding: utf-8 -*-

import networkx as nx

from os import path
import community as com
import fb_friend_graph as fb
from operator import itemgetter, attrgetter


# This method generates an readable javascript format for the Protovis.js from the graphml file
# returned by the the fb_friend_graph.py.
# Also retursn a list of people in the graph with the most important information like
# What community it belongs to, name and id.
def convert_gml_to_js(id):
    g = nx.read_graphml("static/facebookData/" + id + "/" + id + ".graphml")
    g= g.to_undirected()
    partition = com.best_partition(g)
    sameas = {'nodes': [], 'links': []}
    node_ids = {}

    #Who belongs to what community
    for key in partition:
        for p in fb.list_of_people:
            if("friend" + str(p.id) == key ):
                p.community = partition.get(key)

    #Adding community property to each person
    for key, value in partition.iteritems() :
        for n in g:
            if n == key:
                g.node[key]['community'] = value

    #appending name to the graph
    for person in fb.list_of_people:
        for n in g:
            if n == person.id:
                g.node[n]['name'] = person.name

    #appending nodes
    i = 0
    for node in g.nodes():
        sameas['nodes'].append({'nodeName': node, 'group': int(g.node[node].__getitem__('community') + 1),'name': g.node[node].__getitem__('name').encode('utf-8') })
        node_ids[node] = i                                                                                              #use encode to be able to use ÆØÅ
        i += 1

    #appending edges
    for source, target in g.edges():
        e = {'source': node_ids[source], 'target': node_ids[target], 'value':1}
        sameas['links'].append(e)


    #Save the file in the correct format for protovis
    from os import path
    javascript = "var fbGraph = " + str(sameas)
    path = path.relpath( "static/facebookData/"+id + "/" + id + ".js")
    print path
    print path
    text_file = (path  , "w+")
    text_file = open (path , "w")
    text_file.write(str(javascript))
    text_file.close()

    #Return a easy readable list of people and the graph itself, nice to have for futher analyzes
    return fb.list_of_people, g



# A method to count the number of communities in a list
# of poeple (a list like the one returned convert_gml_to_js)
def count_communities(list):
    counter = 0
    for n in list:
        if n.community > counter:
            counter = n.community
    return counter

# Find node_id on the top and lowest node degree
# @param g = graph to analyze
# @param number = number of nodes to find degree on
# @sort = smallest og largest degree, if wrong name entret, will take smallest
def find_smallest_and_largest_nodes_degree(g, number, sort):
    if sort == "largest":
        result_list = sorted(g.degree_iter(),key=itemgetter(1),reverse=True)[0:number]
    else:
        result_list =sorted(g.degree_iter(),key=itemgetter(1))[0:number]
    return result_list

#A method to find the most "Important" node based on
# the betweeness
def find_imporant_node(g):
    node_and_degree=g.degree()
    (largest_node_id,degree)=sorted(node_and_degree.items(),key=itemgetter(1))[-1]
    dic = nx.betweenness_centrality(g)
    top_node = find_smallest_and_largest_nodes_degree(g, 1, "largest")
    #result contains, id, name, degree, betweeness
    result = []
    for person in fb.list_of_people:
        if "friend" + str(person.id) == largest_node_id:
            result.append(person.id)
            result.append(person.name)
            break
    result.append(degree)
    result.append(dic[largest_node_id])
    return result

#A method to find the most "lessst imporant" node based on
# the betweeness
def find_smallest_node(g):
    node_and_degree=g.degree()
    (smallest_node_id,degree)=sorted(node_and_degree.items(),key=itemgetter(1))[1]
    dic = nx.betweenness_centrality(g)
    top_node = find_smallest_and_largest_nodes_degree(g, 1, "smallest")
    #result contains, id, name, degree, betweeness
    result = []
    for person in fb.list_of_people:
        if "friend" + str(person.id) == smallest_node_id:
            result.append(person.id)
            result.append(person.name)
            break
    result.append(degree)
    result.append(dic[smallest_node_id])
    return result

