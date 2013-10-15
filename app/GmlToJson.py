# -*- coding: utf-8 -*-

import networkx as nx

import re
import json
import fileinput
import community as com
import fb_friend_graph as fb
def convert_gml_to_js(id):
    print "loading gml..."
    g = nx.read_graphml("static/facebookData/" + id + "/" + id + ".graphml")
    print "gml now graph"
    g= g.to_undirected()
    partition = com.best_partition(g)

    print partition
    sameas = {'nodes': [], 'links': []}
    node_ids = {}


    for key in partition:
        for p in fb.list_of_people:
            if("friend" + str(p.id) == key ):
                p.community = partition.get(key)



    print "finding communities..."
    for key, value in partition.iteritems() :
        for n in g:
            if n == key:
                g.node[key]['community'] = value

    #adding name to g
    for person in fb.list_of_people:
        for n in g:
            if n == person.id:
                g.node[n]['name'] = person.name

    print "HER KOMMER NAAAAAAVN"
    for n in g.nodes():
        print g.node[n].__getitem__('name')


    print "appending nodes..."
    i = 0
    for node in g.nodes():
        sameas['nodes'].append({'nodeName': node, 'group': int(g.node[node].__getitem__('community') + 1),'name': g.node[node].__getitem__('name').encode('utf-8') })
        node_ids[node] = i                                                                                              #use encode to be able to use ÆØÅ
        i += 1

    print "appending edges..."
    for source, target in g.edges():
        e = {'source': node_ids[source], 'target': node_ids[target], 'value':1}
        sameas['links'].append(e)

    print "saving graph as txt..."

    from os import path
    javascript = "var fbGraph = " + str(sameas)
    path = path.relpath( "static/facebookData/"+id + "/" + id + ".js")
    print path
    print path

    text_file = (path  , "w+")
    text_file = open (path , "w")
    text_file.write(str(javascript))
    text_file.close()

    print "Done!"
    return fb.list_of_people

# counter
def count_communities(list):
    counter = 0
    for n in list:
        if n.community > counter:
            counter = n.community

    return counter