import tkinter as tk
from PIL import Image, ImageDraw
from utils import check

# Constants for canvas size and brush size
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
BRUSH_SIZE = 12

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App")

        # Create a main frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create a canvas in the main frame
        self.canvas = tk.Canvas(self.main_frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='black')
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a sidebar frame
        self.sidebar = tk.Frame(self.main_frame, width=100)
        self.sidebar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a button in the sidebar
        self.save_button = tk.Button(self.sidebar, text="Evaluate", command=self.save_image)
        self.save_button.pack(pady=20)
        
        self.reset_button = tk.Button(self.sidebar, text="Reset Canvas", command=self.reset_canvas)
        self.reset_button.pack(pady=20)

        self.text_widget = tk.Text(self.sidebar, height=15, width=10)
        self.text_widget.pack(pady=20)
        self.text_widget.insert(tk.END, "") 
        font = ("TkDefaultFont", 14)
        self.text_widget.configure(font=font)





        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.draw_on_canvas)

        # Create a PIL image and draw object
        self.image = Image.new("RGB", (CANVAS_WIDTH, CANVAS_HEIGHT), "black")
        self.draw = ImageDraw.Draw(self.image)

    def draw_on_canvas(self, event):
        x1, y1 = (event.x - BRUSH_SIZE), (event.y - BRUSH_SIZE)
        x2, y2 = (event.x + BRUSH_SIZE), (event.y + BRUSH_SIZE)
        self.canvas.create_oval(x1, y1, x2, y2, fill='white', width=BRUSH_SIZE)
        self.draw.line([x1, y1, x2, y2], fill='white', width=BRUSH_SIZE)

    def save_image(self):
        file_path = "img/drawing.png"  # Change this to your desired file path and filename
        self.image.save(file_path)
        ch = check()
        print(f"You wrote: {ch}")
        self.text_widget.insert(tk.END, f"You wrote: {ch}\n")

    def reset_canvas(self):
        # Delete all items on the canvas
        self.canvas.delete("all")
        # Clear the PIL image
        self.image = Image.new("RGB", (CANVAS_WIDTH, CANVAS_HEIGHT), "black")
        self.draw = ImageDraw.Draw(self.image)
        
def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
