def repeat_on_quadrants(x_coordinate, y_coordinate):
    return [
        (x_coordinate, y_coordinate),
        (x_coordinate, -y_coordinate),
        (-x_coordinate, -y_coordinate),
        (-x_coordinate, y_coordinate)
    ]
