__author__ = 'Sindre'
import networkx as nx
import matplotlib.pyplot as plt
import StringIO
import community



def makeGraph():
    return nx.complete_graph(5)

def makeImage(g):
    return g.canvas.draw()

def test():

    g =nx.read_gml('facebook.gml')



    nx.draw(g)

    imgdata = StringIO.StringIO()
    plt.savefig(imgdata, format='png')

    imgdata.seek(0)
    fbGraph = imgdata.buf


    return fbGraph



