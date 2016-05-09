#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
import Tkinter as Tk
import Image

class Dibujo(Tk.Canvas,object):

    def __init__(self,root,bg="white", width=2000, height=1333): 
        super(Dibujo,self).__init__(root,bg=bg,width=width,height=height)
        self.configure(cursor="crosshair")

        self.root = root
        photo = Tk.PhotoImage(file="mount.gif")
        self.w = Tk.Label(root, image=photo)#, relwidth=100, height=100)
        self.w.photo=photo
        self.w.pack(expand="yes")#,fill="both")
        self.pack(expand ="yes", fill= "both")
        self.bind("<Button-1>", self.point)
        self.bind("<Button-3>", self.remove)
        self.bind("<Button-2>", self.end)

    
    points = []
    point_objs = []
    line_objs = []

    def end(self,event):
        self.root.destroy()

    def point(self,event): 
        self.point_objs.append( self.create_oval(event.x,event.y,event.x+1,event.y+1,fill="black") )
        self.points.append(event.x)
        self.points.append(event.y)
        if len(self.points)>2:
            self.line_objs.append( self.create_line(self.points, tags="theline") )

    def remove(self,event):
        if self.line_objs != []:
            self.delete(self.line_objs[-1])
            self.line_objs.pop()
        if self.point_objs != []:
            self.points = self.points[:-2]
            self.delete(self.point_objs[-1])
            self.point_objs.pop()

  
if __name__=="__main__":
    root = Tk.Tk()
    #root.resizable(0,0)
    prueba = Dibujo(root)
    
    root.mainloop()

    print prueba.points
    i=raw_input()


#f = misc.imread("mount.jpg")
#print( f.shape )
#f[:,:,0] *=  0
#f[:,:,1] *=  1
#f[:,:,2] *=  0
#
#i = np.array( [ [ [2,3,5], [2,6,6] ],  \
#                [ [2,200,5], [0,0,0] ] ])
#plt.imshow(i)
#plt.show()
