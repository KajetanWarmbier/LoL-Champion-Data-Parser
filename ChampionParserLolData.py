import os
import json
import pandas as pd

directory = 'E:\lolComp\jsonParseChampions\champion'

character_list = []
character_data = []
characters_array =['type', 'format', 'version', 'data.id', 'data.key',
'data.name', 'data.title', 'data.image.full', 'data.imaga.sprite', 'data.image.group', 'data.image.x',
'data.image.y', 'data.image.w', 'data.image.h', 'data.skins', 'data.lore', 'data.blurb', 'data.allytips',
'data.enemytips', 'data.tags', 'data.partype', 'data.info.attack', 'data.info.defense', 'data.info.magic',
'data.info.difficulty', 'data.stats.hp', 'data.stats.hpperlevel', 'data.stats.mp', 'data.stats.mpperlevel',
'data.stats.movespeed', 'data.stats.armor', 'data.stats.armorperlevel', 'data.stats.spellblock', 'data.stats.spellblockperlevel',
'data.stats.attackrange', 'data.stats.hpregen', 'data.stats.hpregenperlevel', 'data.stats.mpregen', 'data.stats.mpregenperlevel', 'data.stats.crit', 
'data.stats.critperlevel','data.stats.attackdamage', 'data.stats.attackdamageperlevel', 'data.stats.attackspeedperlevel', 'data.stats.attackspeed',
'data.spells', 'data.passive.name', 'data.passive.description', 'data.passive.image.full', 'data.passive.image.sprite', 'data.passive.image.group',
'data.passive.image.x', 'data.passive.image.y', 'data.passive.image.w', 'data.passive.image.h', 'data.recommended']
characters_full = pd.DataFrame(columns=characters_array)

main_directory = "E:\\lolComp\jsonParseChampions\champion\\"

for filename in os.listdir(directory):
    if filename.endswith(".json"):
        character_list.append(main_directory + filename)
        continue
    else:
        continue

for character in character_list:
        with open(character) as data_file:
            character = json.load(data_file)
        character = pd.json_normalize(character, max_level=5)
        character_info = pd.DataFrame(character)
        character_info.columns = characters_array
        characters_full = characters_full.append(character_info)

characters_full.insert(0, 'ID', range(1, 1 + len(characters_full)))

characters_full.drop(['data.skins', 'data.lore', 'data.blurb', 'data.allytips', 'data.enemytips',
 'data.recommended', 'data.passive.description', 'data.passive.name', 'data.spells'], inplace=True, axis=1)

#print(characters_full)
#characters_full.to_csv('charactersinfofullv2.csv')