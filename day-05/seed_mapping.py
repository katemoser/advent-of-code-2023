seeds = []
seed_soil_map = []
soil_fertilzer_map = []
fertilizer_water_map = []
water_light_map = []
light_temperature_map = []
temperature_humidity_map = []
humidity_location_map = []

maps = [
    seed_soil_map,
    soil_fertilzer_map,
    fertilizer_water_map,
    water_light_map,
    light_temperature_map,
    temperature_humidity_map,
    humidity_location_map
]

def populate_maps_from_file(filepath):

    with open(filepath, "r") as file:
        output = file.read()
        map_strings = output.split("\n\n")

        for seed in map_strings.pop(0).split(":")[1].strip().split(" "):
            seeds.append(int(seed))
        print("seeds", seeds)



        # maps

        for i in range(len(maps)):
            lines = map_strings[i].split(":")[1].strip().split("\n")
            for line in lines:
                maps[i].append([int(n) for n in line.split(" ")])

        print(maps)

def sort_mappings():
    for map in maps:
        map.sort()

def traverse_mappings(seed):
    for map in maps:
        # print(f"starting new map, seed is {seed}")
        for section in map:
            [destination_start, source_start, range_length] = section
            # print(f"seed is {seed}, range is {destination_start} - {destination_start + range_length}")
            if source_start <= seed < source_start + range_length:
                # print(f"hit! {seed} is in ^^ that range")

                jump_amount = destination_start - source_start
                seed += jump_amount
                # print("about to break, seed=", seed)
                break

    return seed

def find_closest_location(filepath):
    populate_maps_from_file(filepath)
    locations = [traverse_mappings(seed) for seed in seeds]
    print(locations)
    return min(locations)

def find_closest_location_ranges(filepath):

    populate_maps_from_file(filepath)

    seed_ranges = []

    for i in range(0, len(seeds), 2):
        seed_ranges.append( (seeds[i], seeds[i] + seeds[i+1] - 1))

    # all_seeds = []

    min_location = float('inf')

    for r in seed_ranges:
        (start, end) = r
        seed = start
        while seed <= end:
            print("seed:", seed)
            location = traverse_mappings(seed)
            if location < min_location:
                min_location = location
            seed += 1

    # min_location = float('inf')
    # for seed in all_seeds:
    #     print("seed:", seed)
    #     location = traverse_mappings(seed)
    #     if location < min_location:
    #         min_location = location
    # locations = [traverse_mappings(seed) for seed in all_seeds]
    # min_location = min(locations)
    print("THE MINIMUM LOCATION IS ", min_location)
    return min_location

