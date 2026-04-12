import tkinter as tk
import math
import time

window = tk.Tk()
window.title("Kettaga telefon")
window.geometry("400x500")

canvas = tk.Canvas(window, width=400, height=400, bg="white")
canvas.pack()

cx, cy = 200, 200
radius = 140

current_angle = 0
start_angle = 0
dragging = False
number_text = ""

# põhi ketas
canvas.create_oval(cx - radius, cy - radius,
                   cx + radius, cy + radius,
                   fill="#ddd")

# numbrite seadistamine
start_deg = -135
end_deg = 135
step = (end_deg - start_deg) / 9

digit_positions = []

# staatilised numbrid
for i in range(10):
    angle_deg = start_deg + step * i
    angle = math.radians(angle_deg)

    x = cx + (radius - 20) * math.cos(angle)
    y = cy + (radius - 20) * math.sin(angle)

    #  9 -> 0
    num = 9 - i

    canvas.create_text(x, y, text=str(num),
                       font=("Arial", 14, "bold"))
    digit_positions.append((angle_deg, num))

# stopper
stopper_angle = math.radians(160)
sx = cx + (radius + 5) * math.cos(stopper_angle)
sy = cy + (radius + 5) * math.sin(stopper_angle)

canvas.create_polygon(
    sx - 10, sy - 10,
    sx + 15, sy,
    sx - 10, sy + 10,
    fill="red"
)

# liigutavad augud
def draw_holes(angle_offset=0):
    canvas.delete("holes")

    for i in range(10):
        angle_deg = start_deg + step * i + angle_offset
        angle = math.radians(angle_deg)

        x = cx + (radius - 60) * math.cos(angle)
        y = cy + (radius - 60) * math.sin(angle)

        canvas.create_oval(
            x - 18, y - 18, x + 18, y + 18,
            fill="white", tags="holes"
        )

draw_holes()

label = tk.Label(window, text="Number: ")
label.pack()

result_label = tk.Label(window, text="")
result_label.pack()

def get_angle(x, y):
    dx = x - cx
    dy = y - cy
    return math.degrees(math.atan2(dy, dx))

def on_click(event):
    global dragging, start_angle
    dragging = True
    start_angle = get_angle(event.x, event.y)

def on_drag(event):
    global current_angle
    if dragging:
        angle = get_angle(event.x, event.y)
        diff = angle - start_angle

        if diff > 0 and diff < 300:  # piiramine ~300 kraadi
            current_angle = diff
            draw_holes(current_angle)

def on_release(event):
    global dragging, current_angle, number_text
    dragging = False

    # numbri määramine
    number = int(current_angle // (300 / 10))
    if number > 9:
        number = 9

    number_text += str(number)
    label.config(text="Number: " + number_text)

    # liikumine tagasi
    for i in range(int(current_angle), 0, -4):
        draw_holes(i)
        window.update()
        time.sleep(0.01)

    current_angle = 0
    draw_holes(0)

def call():
    result_label.config(text="Helistan: " + number_text)

button = tk.Button(window, text="Helista", command=call)
button.pack()

canvas.bind("<Button-1>", on_click)
canvas.bind("<B1-Motion>", on_drag)
canvas.bind("<ButtonRelease-1>", on_release)

window.mainloop()
