def area(radius=None, height=None, width=None):
    if radius is not None:
        return radius**2*3.14
    elif height is not None and width is not None:
        return height*width
    else:
        return None

area_by_radius = area(3.3)
print(area_by_radius)
area_by_height_width = area(height=1, width=2)
print(area_by_height_width)
area_by_implicit_parameters = area(1, 2)
print(area_by_implicit_parameters)
