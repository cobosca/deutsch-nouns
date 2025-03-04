import json


with open("nounList.json", "r") as jfile:
    noun_list = json.load(jfile)

# print(noun_list)
# print(len(noun_list)) 


# ok. so, viss straadaa. Lists ir saglabajies ka json un to var arii extractot.
# tagad vajadzeetu uztaisiit programmu kas sadala lietvardus pa dzimteem 3 dazados list, bet tada pasa formata.
# programma ies cauri katram elementam lielajaa 2000 noun listaa , kur katrs elements ir dict.
# Un Checkos kaada ir dict["artik"] veertiiba. Ja Der tad viena listaa , ja Die tad citaa, ja Das tad citaa.

der_list = []
das_list = []
die_list = []

handikap_list = []

for noun in noun_list:
    if noun["artik"] == "Der":
        der_list.append(noun)
    elif noun["artik"] == "Das":
        das_list.append(noun)
    elif noun["artik"] == "Die":
        die_list.append(noun)
    else:
        handikap_list.append(noun)

print(len(der_list))
print(len(das_list))
print(len(die_list))


with open("derList.json", "w") as jfile:
    json.dump(der_list, jfile)

with open("dasList.json", "w") as jfile:
    json.dump(das_list, jfile)

with open("dieList.json", "w") as jfile:
    json.dump(die_list, jfile)
