import curses
import time
import math
import json

def calculate_display(window, column_count, column_order, row_count, row_order):
    maxy, maxx = window.getmaxyx()
    # Calculate column width
    box_width = math.floor(maxx / column_count)
    begin_x = (box_width * (column_order)) + 1
    # Calculate row height 
    box_height = math.floor(maxy / row_count) + 1
    begin_y = box_height * (row_order) + 1
    return box_height, box_width, begin_y, begin_x

def init():
    screen = curses.initscr()
    curses.noecho()  # disable the keypress echo to prevent double input
    curses.cbreak()  # disable line buffers to run the keypress immediately
    #curses.curs_set(0)
    # Setup color
    curses.start_color()
    #curses.init_color(COLOR_RED,700, 0, 0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    screen.keypad(1)  # enable keyboard use
    screen.clear()
    return screen

def create_frame(screen):
    maxy, maxx = screen.getmaxyx()
    box_height = maxy
    box_width = maxx
    outer_frame = curses.newwin(box_height, box_width, 0, 0)
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
            box_height, box_width, begin_y, begin_x = calculate_display(frame, column_count, columnid, row_count, rowid)
            dynamic_box = curses.newwin(box_height, box_width, begin_y, begin_x)
            inner_box = curses.newwin(box_height -2, box_width -2, begin_y + 1, begin_x + 1)
            column["inner_box"] = inner_box
            dynamic_box.box()
            dynamic_box.refresh()
            columnid += 1
        rowid += 1

def populate_dashboard(data,layout):
    for item in data["boxes"]:
        for row in layout["rows"]:
            if row["name"] == item["row"]:
                for column in row["columns"]:
                    if column["name"] == item["column"]:
                        height, width = column["inner_box"].getmaxyx() # get the window size
                        
                        # Set background color
                        column["inner_box"].bkgd(curses.color_pair(3))
                        # Write a header and footer, first write colored strip, then write text
                        column["inner_box"].addstr(0, 0, " " * width,curses.color_pair(1) )
                        column["inner_box"].addstr(0, 0, "{}".format(item["header"]) ,curses.color_pair(1) )
                        column["inner_box"].addstr(1, 0, "{}".format(item["content"]))
                        #column["box"].addstr(height-1, 0, " Key Commands : q - to quit " ,curses.color_pair(1) )
                        column["inner_box"].refresh()

def main():
    with open('layout.json') as layout_f:
        layout = json.load(layout_f)
    with open('data.json') as data_f:
        data = json.load(data_f)

    screen = init()
    outer_frame = create_frame(screen)
    create_layout(outer_frame, layout)

    populate_dashboard(data,layout)

if __name__ == '__main__':
    main()