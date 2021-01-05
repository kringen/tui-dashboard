import curses
import time
import math

def calculate_display(window, box_count, box_order):
    maxy, maxx = window.getmaxyx()
    box_width = math.floor(maxx / box_count)
    begin_x = box_width * (box_order)
    box_height = maxy
    begin_y = 0
    return box_height, box_width, begin_y, begin_x

def init(title,data):
    screen = curses.initscr()
    curses.noecho()  # disable the keypress echo to prevent double input
    curses.cbreak()  # disable line buffers to run the keypress immediately
    curses.curs_set(0)
    screen.keypad(1)  # enable keyboard use
    screen.addstr(1, 2, title, curses.A_UNDERLINE)
    # Calculate
    boxes = []
    box_count = len(data)
    n = 0
    for item in data:
        box_height, box_width, begin_y, begin_x = calculate_display(screen, box_count, n)
        dynamic_box = curses.newwin(box_height, box_width, begin_y, begin_x)
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
        box.addstr(1,1, "TEST")
        inner_box = curses.newwin(box_height - 2, box_width - 2, begin_y + 2, begin_x+1)
        inner_box.addstr(1, 1, data[n]["one"])
        inner_box.refresh()
        box.refresh()
        n += 1

def main():
    data = [
        {
            "one":"This is a really long string that is intended to wrap.  If it doesn't wrap, it won't impact.",
            "two":"two",
            "three":"three"
        },
        {
            "one":"one",
            "two":"two",
            "three":"three"
        },
        {
            "one":"one",
            "two":"two",
            "three":"three"
        },
        {
            "one":"one",
            "two":"two",
            "three":"three"
        },
        {
            "one":"one",
            "two":"two",
            "three":"three"
        }
    ]

    screen, boxes = init("Dashboard",data)
    try:
        while True:
            update_screen(screen,boxes,data)
            time.sleep(1)
    except KeyboardInterrupt:
        curses.endwin()

if __name__ == '__main__':
    main()