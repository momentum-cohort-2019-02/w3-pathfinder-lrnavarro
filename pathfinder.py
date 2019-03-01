def get_2d_array(text_file):
     
    with open(text_file) as file:
        elevation_list = [line.split() for line in file]
        # print(elevation_list)
        # print(f'the length of the list of lists is {len(elevation_list)}')
        # print(f'the length of each list is {len(elevation_list[0])}')
        return ('elevation_list')

small_elevation_array = get_2d_array('elevation_small.txt')
# try actions on simpler example



# simple_array = [['1', '2', '3','4', '5'],
#                 ['1', '2', '3','4', '5'],
#                 ['1', '2', '3','4', '5'],
#                 ['1', '2', '3','4', '5'],
#                 ['1', '2', '3','4', '5']]

#simple_int_array = [[int(number) for number in row] for row in simple_array]
#print(simple_array)
#turns each string into integers

# small_elevation_array = [[int(number) for number in row] for row in simple_array]



# simple_array = [['1', '2', '3','4', '5'],
#                 ['1', '2', '3','4', '5'],
#                 ['1', '2', '3','4', '5'],
#                 ['1', '2', '3','4', '5'],
#                 ['8', '6', '9','7', '5']]

# simple_int_array = [[int(number) for number in row] for row in simple_array]
#gets min from each row
# min(simple_int_array)
#gets max from each row
# max(simple_int_array)
# print(maxs)

# mins = [min(row) for row in simple_int_array]
# print(mins)
# maxs = [max(row) for row in simple_int_array]
# print(mins)

#gets min from all the mins
# smallest_min = min(mins)
# print(smallest_min)

#gets min from all the mins
# largest_max = max(maxs)
# print(largest_max)



# print(min(simple_int_array))
#finds min row in list of lists
















