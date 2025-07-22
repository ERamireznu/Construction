# Construction
To develop useful tools for construction related issues.

houseplan_v00
A script for making a simple and fast plan for a place (a house, an appartment, etc.), using turtle module.
The idea is subdivide the place into square rooms, measuring every one of them. Aside from the measures, we need to set the coordinates for every room; it will be considered that these coordinates are in the low-left corner (when looking to the screen).
This data will be in tuples as: (x, y, long x, long y)
So, as an example for a room:
(0, 0, 372, 273): starts in (0, 0), width = 372 cm, long = 273 cm
There is a real example in the script (as "example: depto lazo"). This is also the place to set your own data for personal use.
Apart from the drawing, the option calc_data is given, whose purpose is to deliver the main measures of every room (useful for materials calculation).
