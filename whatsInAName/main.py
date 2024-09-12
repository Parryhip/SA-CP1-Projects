def calculate_area(height, width):
    area = width * height
    return area

def calculate_volume(height, width, depth):
    base_area = calculate_area(height, width)
    volume = base_area * depth
    return volume

heightForArea = 5
widthForArea = 3
rectangle_area = calculate_area(heightForArea, widthForArea)
print(f"The rectangle's area is: {rectangle_area}")

heightForVolume = 4
widthForVolume = 6
depthForVolume = 2
rectanglular_prism_volume = calculate_volume(heightForVolume, widthForVolume, depthForVolume)
print(f"The rectangular prism's volume is: {rectanglular_prism_volume}")