len_tile = int(input("Enter the length of the tile: "))
breadth_tile = int(input("Enter the breadth of the tile: "))
length_floor = int(input("Enter the length of the floor: "))
breadth_floor = int(input("Enter the breadth of the floor: "))

area_floor = length_floor * breadth_floor
area_tile = len_tile * breadth_tile

tiles_needed = area_floor / area_tile
print("Number of tiles needed:", tiles_needed)
