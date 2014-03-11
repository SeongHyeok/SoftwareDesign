"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""

class Point(object):
    """Represents a point in 2-D space."""


def print_point(p):
    """Print a Point object in human-readable format."""
    print '(%g, %g)' % (p.x, p.y)

def distance_between_points(p1, p2):
    """Return the distance between given two points"""
    return (abs(p1.x - p2.x) ** 2 + abs(p1.y - p2.y) ** 2) ** 0.5


class Rectangle(object):
    """Represents a rectangle.

    attributes: width, height, corner.
    """


def find_center(rect):
    """Returns a Point at the center of a Rectangle."""
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p


def grow_rectangle(rect, dwidth, dheight):
    """Modify the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight

def move_rectangle(rect, dx, dy):
    """Change the location of the rectangle"""
    rect.corner.x += dx
    rect.corner.y += dy

def move_rectangle2(rect, dx, dy):
    """Create a new rectangle from given rectangle and move it"""
    new_rect = Rectangle()

    new_rect.width = rect.width
    new_rect.height = rect.height

    new_rect.corner = Point()
    new_rect.corner.x = rect.corner.x + dx
    new_rect.corner.y = rect.corner.y + dy

    return new_rect


def main():
    blank = Point()
    blank.x = 3
    blank.y = 4
    print 'blank',
    print_point(blank)

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    center = find_center(box)
    print 'center',
    print_point(center)

    print box.width
    print box.height
    print 'grow'
    grow_rectangle(box, 50, 100)
    print box.width
    print box.height

    print "=========="
    # 15.1
    print distance_between_points(box.corner, blank)

    # 15.2
    print_point(box.corner)
    move_rectangle(box, 30, 30)
    print_point(box.corner)

    # 15.3
    new_box = move_rectangle2(box, 20, 20)
    print_point(new_box.corner)


if __name__ == '__main__':
    main()

