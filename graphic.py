import networkx as nx
import matplotlib.pyplot as plt
import network
import matplotlib.animation as animation
import time 
import config

import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook





class graphic:
    def __init__(self, brain):
        self.brain = brain


    def simple_draw(self):
        print("simple draw")



    
    
    def draw(self):
        print("draw \n")
        G = nx.Graph()
        G.add_node(0,pos=(self.mynetwork.xsize/2,self.mynetwork.xsize/2))
        for node in self.mynetwork.nodes:
            if(node.is_alive == True):
                # print("for node in self.mynetwork.nodes {0} and cluster head {1}".format(node,node.parent))

                G.add_node(node.id,pos=(node.x,node.y))
                
                if(len(node.parent)!=0):
                    if(node.parent[0].is_alive==True):
                        G.add_edge(0,node.parent[0].id)
                if(len(node.parent)!=0):
                    if(node.parent[0].is_alive==True):
                        G.add_edge(node.id,node.parent[0].id)

        nodelistCH = []
        for node in self.mynetwork.nodes:
            if(node.is_alive == True):
                if(node.is_CH == True):
                    nodelistCH.append(node.id)
        # print(nodelistCH)
        nx.draw(G, nx.get_node_attributes(G, 'pos'), with_labels=True, node_size=400)
        #ani = animation.FuncAnimation(fig, animate, interval=1000)
        nx.draw_networkx(G, nx.get_node_attributes(G, 'pos'), nodelist=[0], node_size=1000, node_color='#66ff66')
        nx.draw_networkx(G, nx.get_node_attributes(G, 'pos'), nodelist=nodelistCH, node_size=700, node_color='#ff80ff')
        mng = plt.get_current_fig_manager()
        #mng.full_screen_toggle()
        mng.set_window_title("draw")

        plt.pause(5)
        plt.clf()
        plt.close()
