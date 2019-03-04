from PIL import Image, ImageDraw

def get_2d_array(text_file):

    with open(text_file) as file:
        elevation_list = [line.split() for line in file]
    return elevation_list

#assigning value I get from the function to the small_elevation_list variable I made to use later
small_elevation_list = get_2d_array('elevation_small.txt')

#turns each string into integers
def get_int_array(small_elevation_list):
    return [[int(number) for number in row] for row in small_elevation_list]

simple_int_array = get_int_array(small_elevation_list)

#gets min from each row, then overall min
def get_smallest_min(simple_int_array):
    mins = [min(row) for row in simple_int_array]
    return min(mins)
smallest_min = get_smallest_min(simple_int_array)

#gets max from each row, then overall max
def get_largest_max(simple_int_array):
    maxs = [max(row) for row in simple_int_array]
    return max(maxs)
largest_max = get_largest_max(simple_int_array)

#gets overall size of image
y_count = len(simple_int_array)
x_count = len(simple_int_array[0])
# print(y_count)
# print(x_count)

#creating new image with size specification
def create_map(y_count, x_count, simple_int_array, smallest_min, largest_max):
    im = Image.new('RGBA', (x_count, y_count))
    for y in range(y_count):
        for x in range(x_count):
            #creating color
            rgb_value = int(((simple_int_array[y][x] - smallest_min) / (largest_max - smallest_min)) * 255)
            #assigning position and color
            im.putpixel((x, y), (rgb_value, rgb_value, rgb_value))
    return im
map_image = create_map(y_count, x_count, simple_int_array, smallest_min, largest_max)

map_image.save('map.png', 'png')

















