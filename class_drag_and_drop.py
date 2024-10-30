from Pile import Pile
from class_file import File

class DragAndDrop:
    list_drop=[]
    pile_list_drop=[]
    liste=File()
    liste_jeu=File()
    def __init__(self,widget,fenetre,pioche,drop,drag):
        self.drag=drag
        self.drop=drop
        self.pioche=pioche
        self.widget=widget
        self.fenetre=fenetre
        
        if self.drag==True:
            
            if DragAndDrop.liste.est_vide()==False:
                DragAndDrop.liste.defiler().destroy()
            DragAndDrop.liste.enfiler(self.widget)

            self.widget=DragAndDrop.liste.bout_file()
            self.set_drag(self.widget)
            print(DragAndDrop.liste.file)

        if self.drop==True:
            DragAndDrop.list_drop.append(self.widget)
            DragAndDrop.pile_list_drop.append(self.pioche)
            

    def set_drag(self,widget):
        self.widget.bind("<Button-1>",self.on_click_start)
        self.widget.bind("<B1-Motion>",self.on_click)
        self.widget.bind("<ButtonRelease-1>",self.on_drop)
        self.widget["cursor"] = "hand1"
        
    def on_click_start(self,event):
        self.widget_x=self.widget.winfo_x()
        self.widget_y=self.widget.winfo_y()

    def on_click(self,event):
        
        self.widget.place(x=event.x_root - self.fenetre.winfo_rootx(), y=event.y_root - self.fenetre.winfo_rooty())
        self.image=self.widget.cget("image")

    def on_drop(self,event):
        widget_dropped = False
        for target in DragAndDrop.list_drop:
            coord_target_x,coord_target_y=target.winfo_x(),target.winfo_y()
            coord_target_x_max,coord_target_y_max=coord_target_x+target.winfo_width(),coord_target_y+target.winfo_height()
            if self.widget.winfo_x()>=coord_target_x and self.widget.winfo_x()<=coord_target_x_max and self.widget.winfo_y()>=coord_target_y and self.widget.winfo_y()<=coord_target_y_max:
                try:
                    self.widget.place(x=coord_target_x,y=coord_target_y)
                    pile=DragAndDrop.pile_list_drop[DragAndDrop.list_drop.index(target)]
                    pile.empiler(self.pioche.sommet(1))
                    self.pioche.depiler()

                    
                    self.pioche=pile
                    widget_dropped = True
                    DragAndDrop.liste_jeu.changement_file(DragAndDrop.liste)
                    add_dragable()
                    
                except Exception as e:
                    print(f"Error occurred: {e}")
            if not widget_dropped:
                self.widget.place(x=self.widget_x, y=self.widget_y)
                
