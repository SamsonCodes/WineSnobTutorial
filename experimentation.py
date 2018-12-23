# Demo file for Spyder Tutorial
# Hans Fangohr, University of Southampton, UK
from tkinter import *
import time

data = [[0,0,0],[1,0,0],[0,1,1],[1,1,1]]
FRAME_WIDTH = 800
FRAME_HEIGHT = 800
separator = " "
log = []
background = 'black'
cell = 'white'

class Node:
    def __init__(node,layer,x):
        node.layer = layer
        node.x = x
        node.children = []
        for i in range(2):
            node.children.append(0)        
    def connect(node,childA, childB):
        node.children[0] = childA
        node.children[1] = childB

def createTree(depth):
    nodes = []      
    n1 = Node(0, 0)
    nodes.append(n1)
    for l in range(depth):
        index = 0
        for n in nodes:
            if (n.layer == l - 1):
                na = Node(l, index)
                nodes.append(na)
                index+=1
                nb = Node(l, index)
                nodes.append(nb)
                index+=1
                n.connect(na,nb)
    for n in range(len(nodes)):
        x = nodes[n].x
        y = nodes[n].layer       
        print(n,x,y)            
    return nodes

def drawTree(nodes, canvas):
    canvas.create_polygon(0, 0, FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT, 0, FRAME_HEIGHT, fill = background)
    grid = 20
    for n in range(len(nodes)):
        x = nodes[n].x
        y = nodes[n].layer             
        canvas.create_polygon(x*grid, y*grid, x*grid + grid/2, y*grid, x*grid + grid/2, y*grid + grid/2, x*grid, y*grid+grid/2, fill = cell)
        

# Main program starts here
gui = Tk()
gui.title("Treehugging")
tree = createTree(5)

#gui.geometry(str(FRAME_WIDTH) + "x" + str(FRAME_HEIGHT))
#f1.printField()T))

c = Canvas(gui ,width=FRAME_WIDTH ,height=FRAME_HEIGHT)

c.pack()

while True:
    drawTree(tree, c)
    gui.update()
    c.delete("all")
    time.sleep(.01)

