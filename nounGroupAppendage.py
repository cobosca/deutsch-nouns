import sys
import json


flag = input("Der, Das oder Die?: ").lower()

with open(f"{flag}List.json", "r") as jfile:
    noun_list = json.load(jfile)

der_groups = ["animals", "cars", "currency", "days, months and seasons", "directions", "drinks: alcoholic and plant-based", "male persons", "mountains and mountain ranges", "non-german rivers", "space", "rocks, minerals", "weather"]

die_groups = ["airplanes, motorcycles % ships ( makes, models, names)", "animals", "female persons", "numerals as nouns", "rivers within Germany, Austria, Switzerland", "Trees, Fruits, Flowers"]

das_groups = ["alphabet letters, music notes", "continents, cities, provinces, most countries", "gerunds, colours, languages, English -ing forms and other parts of speech used as nouns", "Hotels, cafes, restaurants, movie theaters", "metals, chemical elements", "scientific units", "young persons and baby animals"]

if flag == "der":
    flag_group = der_groups
elif flag == "das":
    flag_group = das_groups
elif flag == "die":
    flag_group = die_groups
else: sys.exit("Wrong flag group")


for noun in noun_list:
    if noun["group"] == "":
        print( f"\n\n\n {noun["artik"].title()} {noun["de"].title()} \t\t\t\t\t {noun["eng"]} " )

        gr_counter = 1 
        for group in flag_group:
            print( f"\t\t {gr_counter}. {group} ")
            gr_counter += 1
        group_flag = input("Put group nr or leave blank:\n Or if you want to save and quit 'q' ")
        if group_flag == "q":
            break 
        elif group_flag == "":
            noun["group"] = "none"            
        else:
            noun["group"] = flag_group[ int(group_flag) - 1]

with open(f"{flag}List.json", "w") as jfile:
    json.dump(noun_list, jfile)
