import json
#!/usr/bin/python
 # -*- coding: utf-8 -*-
with open('large-file.json', encoding='utf-8') as openfile:
    miJSON= json.load(openfile)
print(miJSON)
# for i in range (5):
#      print(miJSON[i])

crearEvents=[]
for i in range (len(miJSON)):
    if (miJSON[i]['type']=='CreateEvent'):
        crearEvents.append(miJSON[i])

for q in range (5):
    print("#################")
    print("## Evento #", q+1,"##")
    print("#################")
    print("ID:", crearEvents[q]['id'])
    print("Tipo:", crearEvents[q]['type'])
    print("Actor:")
    print("--------")
    print("---------ID:",crearEvents[q]['actor']['id'])

with open("eventos.json","w") as outfile:
    json.dump(crearEvents,outfile)
