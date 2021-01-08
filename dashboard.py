import curses
import time
import math

def calculate_display(window, box_count, box_order):
    maxy, maxx = window.getmaxyx()
    box_width = math.floor(maxx / box_count)
    begin_x = box_width * (box_order)
    begin_y = 0
    box_height = maxy - begin_y
    return box_height, box_width, begin_y, begin_x

def init():
    screen = curses.initscr()
    curses.noecho()  # disable the keypress echo to prevent double input
    curses.cbreak()  # disable line buffers to run the keypress immediately
    curses.curs_set(0)
    screen.keypad(1)  # enable keyboard use
    return screen

def create_frame(screen):
    box_height, box_width, begin_y, begin_x = calculate_display(screen, 1, 0)
    outer_frame = curses.newwin(box_height, box_width, begin_y, begin_x)
    outer_frame.box()
    outer_frame.refresh()
    return outer_frame

#def create_row(parent, box_count, height, margin):
#    n = 0
#    for item in range(box_count):
#        box = 
#        n += 1

def create_box():
    box_height, box_width, begin_y, begin_x = calculate_display(parent, box_count, n)
    box = curses.newwin(box_height - margin - margin, box_width - margin, begin_y + margin, begin_x + margin)
    box.box()
    box.refresh()
    return box

def create_boxes():
    # Calculate
    boxes = []
    box_count = len(data)
    n = 0
    for item in data:
        box_height, box_width, begin_y, begin_x = calculate_display(screen, box_count, n)
        dynamic_box = curses.newwin(box_height, box_width, begin_y + 2, begin_x)
        dynamic_box.box()
        boxes.append(dynamic_box)
        n += 1

    return screen, boxes

def update_screen(screen, boxes, data):
    maxy, maxx = screen.getmaxyx()

    date = str(time.strftime("%c"))
    screen.addstr(1, maxx - len(date) - 2, date)
   
    screen.refresh()
    n = 0
    for box in boxes:
        box_height, box_width, begin_y, begin_x = calculate_display(screen, len(boxes), n)
        # Create an inner box to add padding for text
        box.addstr(1,1, data[n]["title"])
        inner_box = curses.newwin(box_height - 2, box_width - 2, begin_y + 2, begin_x+1)
        inner_box.addstr(1, 1, data[n]["content"])
        inner_box.refresh()
        box.refresh()
        n += 1

def main():
    layout =  {
            "row1": {"name":"column1"},
            "row2": {"name":"column1"},
            "row3": {"name":"column1"}
    }
    data = [
        {
            "title":"GPS Data",
            "content":"two",
            "three":"three"
        },
        {
            "title":"Temperature",
            "content":"two",
            "three":"three"
        }
    ]

    layout
    #screen = init()
    #outer_frame = create_frame(screen)
    #create_row(outer_frame, 3, 3, 1)

    #try:
    #    while True:
    #        update_screen(screen,boxes,data)
    #        time.sleep(1)
    #except KeyboardInterrupt:
    #    curses.endwin()

if __name__ == '__main__':
    main()