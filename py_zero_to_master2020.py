



import tkinter
import random

class player(object):
    def __init__(self, canvas, color):
        self.color = color
        size = random.randint(1, 100)
        x1 = random.randint(100, 700)
        y1 = random.randint(100, 700)
        x2 = x1 + size
        y2 = y1 + size
        self.coords = [x1, y1, x2, y2]    
        self.piece = canvas.create_rectangle(self.coords, tags = color)
        canvas.itemconfig(self.piece, fill=color)
    def move(self,direction):
        if direction == "u":
            self.coords[1] -= 10
            self.coords[3] -= 10
            canvas.coords(self.piece, self.coords)
        if direction == "d":
            self.coords[1] += 10
            self.coords[3] += 10
            canvas.coords(self.piece, self.coords)
        if direction == "l":
            self.coords[0] -= 10
            self.coords[2] -= 10
            canvas.coords(self.piece, self.coords)
        if direction == "r":
            self.coords[0] += 10
            self.coords[2] += 10
            canvas.coords(self.piece, self.coords)
        
        
        
def handle(event):
    yellow_xy = canvas.bbox(1)
    overlapping = canvas.find_overlapping(yellow_xy[0], yellow_xy[1], yellow_xy[2], yellow_xy[3])
    if 2 in overlapping:
        canvas.create_text(200, 100, font=("Arial",30), text="BOOM!!!")  
    
    if event.char == 'w': player1.move('u')        
    if event.char == 's': player1.move('d')      
    if event.char == 'a': player1.move('l')  
    if event.char == 'd': player1.move('r')  
    if event.char == 'i': player2.move('u')  
    if event.char == 'k': player2.move('d')  
    if event.char == 'j': player2.move('l')  
    if event.char == 'l': player2.move('r')      
        
        
window = tkinter.Tk()
window.geometry("1100x800")
window.title("boom!")
canvas = tkinter.Canvas(window)
canvas.pack(expand=1, fill="both")
player1 = player(canvas, "blue")
player2 = player(canvas, "yellow")
canvas.bind_all('<Key>', handle)
window.mainloop()        


