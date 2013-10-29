# -*- coding: utf-8 -*-
from __future__ import division

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
    print "analyzing smallest top 5 nodes"
    smallest_nodes = find_smallest_and_largest_nodes_degree(g, 5, "largest")
    result = []
    index = 0
    while index < len(smallest_nodes):
        current_person_id = smallest_nodes[index][0]
        for person in fb.list_of_people:
            if "friend" + str(person.id) == current_person_id:
                person.id = person.id.replace('friend', '')
                person.degree = smallest_nodes[index][1]
                betweeness_cent = (len(person.degree) / len(g))
                person.degree_betweness_centrality = betweeness_cent
                result.append(person)
                break
        index += 1
    print "analyzing smallest top 5 DONE"

    return result

def find_smallest_node(g):
    print "analyzing smallest 5 nodes"
    smallest_nodes = find_smallest_and_largest_nodes_degree(g, 5, "smallest")
    result = []
    index = 0
    while index < len(smallest_nodes):
        current_person_id = smallest_nodes[index][0]
        for person in fb.list_of_people:
            if "friend" + str(person.id) == current_person_id:
                person.id = person.id.replace('friend', '')
                person.degree = smallest_nodes[index][0][1]
                betweeness_cent = (len(person.degree) / len(g))
                person.degree_betweness_centrality = betweeness_cent
                result.append(person)
                break
        index += 1
    print "analyzing smallest 5 DONE"

    return result

