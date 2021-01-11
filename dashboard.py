import curses
import time
import math
import json

def calculate_display(window, column_count, column_order, row_count, row_order):
    maxy, maxx = window.getmaxyx()
    # Calculate column width
    box_width = math.floor(maxx / column_count)
    begin_x = box_width * (column_order)
    # Calculate row height 
    box_height = math.floor(maxy / row_count)
    begin_y = box_height * (row_order)
    return box_height, box_width, begin_y, begin_x

def init():
    screen = curses.initscr()
    curses.noecho()  # disable the keypress echo to prevent double input
    curses.cbreak()  # disable line buffers to run the keypress immediately
    curses.curs_set(0)
    screen.keypad(1)  # enable keyboard use
    return screen

def create_frame(screen):
    box_height, box_width, begin_y, begin_x = calculate_display(screen, 1,0, 1, 0)
    outer_frame = curses.newwin(box_height, box_width, begin_y, begin_x)
    outer_frame.box()
    outer_frame.refresh()
    return outer_frame

def create_layout(frame,layout):
    row_count = len(layout["rows"])
    rowid = 0
    for row in layout["rows"]:
        column_count = len(row["columns"])
        columnid = 0
        for column in row["columns"]:   
            box_height, box_width, begin_y, begin_x = calculate_display(parframeent, column_count, columnid, row_count, rowid)
            dynamic_row = curses.newwin(box_height, box_width, begin_y, begin_x)
            dynamic_row.box()
            dynamic_row.refresh()
            column["box"] = dynamic_row
            columnid += 1
        #boxes.append(dynamic_box)
        rowid += 1

def update_layout(frame,layout):
    row_count = len(layout["rows"])
    rowid = 0
    for row in layout["rows"]:
        column_count = len(row["columns"])
        columnid = 0
        for column in row["columns"]:   
            box_height, box_width, begin_y, begin_x = calculate_display(parframeent, column_count, columnid, row_count, rowid)
            dynamic_row = curses.newwin(box_height, box_width, begin_y, begin_x)
            dynamic_row.box()
            dynamic_row.refresh()
            column["box"] = dynamic_row
            columnid += 1
        #boxes.append(dynamic_box)
        rowid += 1

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
    with open('layout.json') as layout_f:
        layout = json.load(layout_f)
    data = [
        {
            "title":"GPS Data",
            "content":"This is GPS data",
            "row": "row0",
            "column": "c4"
        },
        {
            "title":"Temperature",
            "content":"This is Temperature data",
            "row":"row2",
            "column": "c3"
        }
    ]

    screen = init()
    outer_frame = create_frame(screen)
    create_layout(outer_frame, layout)
    f = open("layout.txt", "w") 
    f.write(str(layout))

    for item in data:
        for row in layout["rows"]:
            if row["name"] == item["row"]:
                for column in row["columns"]:
                    if column["name"] == item["column"]:
                        column["box"].addstr(1,1,"This is a test")
                        column["box"].refresh()
    #layout = set_layout(outer_frame, layout)
    #create_row(outer_frame, 3, 3, 1)

    #try:
    #    while True:
    #        update_screen(screen,boxes,data)
    #        time.sleep(1)
    #except KeyboardInterrupt:
    #    curses.endwin()

if __name__ == '__main__':
    main()