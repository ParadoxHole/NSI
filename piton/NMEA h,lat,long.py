trame="$GPGGA,064036.289,4836.5375,N,00740.9373,E,1,04,3.2,200.2,M,,,,0000*0E"
typetrame = trame.split(",")

heureTTC = typetrame[1][0:2]+"h : "+ typetrame[1][3:5]+"m : " + typetrame[1][5:]+"s "

print(heureTTC)

latitude = typetrame[2][0:2]+"° "+ typetrame[2][2:4]+"' " + typetrame[2][5:]+'" ' + typetrame[3]

print(latitude)

longitude = typetrame[4][0:2]+"° "+ typetrame[4][3:5]+"' " + typetrame[4][4:]+'" '+ typetrame[5]

print(longitude)