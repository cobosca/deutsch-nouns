

# programma kas ielaadee texta failu ar jeeliem 2000 vaacu lietu vaardiem.
# pa rindinai nolasa un katrai rindai ( vardam ) izveido dictionary peec extractorFormat.txt formas.
# ievieto konkreeto dictionary lielajaa listaa kur staavees 2000 taadi dict.
# kad pabeigts , tad uztaisa json failu no taa galvenaa lista.


import json

noun_list = []

with open("2000dnouns.txt", "r") as textfile:
    for line in textfile:
        new_line = line.replace("\t", "#")
        new_line = new_line.replace("\n", "")
        line_elements = new_line.split("#")
        nrandengword = line_elements[0]
        nr, engword = nrandengword.split(" ")
        artik_deword = line_elements[1]
        try:
            artik, deword = artik_deword.split(" ");    
        except:
            artik = "No artikel"
            deword = artik_deword

        plural = line_elements[2]

        word_dict = dict(eng=engword, artik=artik, de=deword, plural=plural, group="")
        print(word_dict)
        noun_list.append( word_dict )

print(len(noun_list))
json_list = json.dumps( noun_list )

with open("nounList.json", "w") as jfile:
    jfile.write( json_list )
