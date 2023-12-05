import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import time
import random
import numpy as np
from matplotlib import animation
from matplotlib import cm

#plt.ion()

window = tk.Tk()
window.title("Gimbal Gui")

fig = Figure(figsize=(5,4), dpi=100)
rssi_axe = fig.add_subplot()

rssi_axe.autoscale(False)
rssi_axe.set_xlim(0, 500)
rssi_axe.set_ylim(0,500)

x_data = [1,2,3,4,5]
y_data = [2,4,5,6,7]

scatter_collection = rssi_axe.scatter(x_data, y_data, vmin=0, vmax=100)

canvas = FigureCanvasTkAgg(fig, master=window)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=0, padx=10, pady=10)

data_points_x = []
data_points_y = []
data_points_c = []

def generate_unefficient(num_points):
    start_time = time.time()
    for i in range(num_points):
        loop_start_time = time.time()
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        c = random.randint(0, 100)
        data_points_x.append(x)
        data_points_y.append(y)
        color = cm.viridis(c/100)
        data_points_c.append(color)
        if(i==num_points-1):
            print(data_points_x)
        print(f"mid1time: {time.time() - loop_start_time}")
        mid1time = time.time()
        scatter_collection.set_offsets(np.c_[data_points_x, data_points_y])
        print(f"mid2time: {time.time() - mid1time}")
        mid2time = time.time()
        scatter_collection.set_facecolors(data_points_c)
        print(f"mid3time: {time.time() - mid2time}")
        mid3time = time.time()
        fig.canvas.draw_idle()
        print(f"mid4time: {time.time() - mid3time}")
    print(f"Took {time.time() - start_time} to generate")

def generate_efficient(num_points):
    start_time = time.time()
    x_buf = []
    y_buf = []
    c_buf = []
    for i in range(num_points):
        x = random.randint(0, 500)
        x_buf.append(x)
        y = random.randint(0, 500)
        y_buf.append(y)
        c = random.randint(0, 100)
        c_buf.append(c)
    rssi_axe.scatter(x_buf, y_buf, c=c_buf, vmin=0, vmax=100)
    fig.canvas.draw()
    print(f"Took {time.time() - start_time} to generate")

def generate_ultra_efficient(num_points):
    start_time = time.time()
    x_buf = []
    y_buf = []
    c_buf = []
    for i in range(num_points):
        x = random.randint(0, 500)
        x_buf.append(x)
        y = random.randint(0, 500)
        y_buf.append(y)
        c = random.randint(0, 100)
        c_buf.append(c)
    data_points_x.extend(x_buf)
    data_points_y.extend(y_buf)
    #print(data_points_x)
    scatter_collection.set_offsets(np.c_[data_points_x, data_points_y])
    fig.canvas.draw()
    print(f"Took {time.time() - start_time} to generate")    


x_buffer = []
y_buffer = []

def add_to_buffer(num_points):
    for i in range(num_points):
        x = random.randint(0, 500)
        x_buffer.append(x)
        y = random.randint(0, 500)
        y_buffer.append(y)

generate_button = ttk.Button(window, text="Generate", command=lambda: generate_unefficient(100))
generate_button.grid(row=1, column=0, pady=10)

generate_efficient_button = ttk.Button(window, text="Generate Efficient", command=lambda: generate_efficient(100))
generate_efficient_button.grid(row=2, column=0, pady=10)

generate_ultra_efficient_button = ttk.Button(window, text="Generate ultra_Efficient", command=lambda: generate_ultra_efficient(100))
generate_ultra_efficient_button.grid(row=4, column=0, pady=10)

add_to_buffer_button = ttk.Button(window, text="Add to buffer", command=lambda: add_to_buffer(100))
add_to_buffer_button.grid(row=3, column=0, pady=10)


"""
scat = rssi_axe.scatter([], [])

def init():
    return scat,

def animate(_):
    print(x_buffer)
    print(y_buffer)
    scat.set_offsets(np.c_[x_buffer, y_buffer])
    return scat

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=1, interval=4, blit=False, repeat=False)

"""

window.mainloop()