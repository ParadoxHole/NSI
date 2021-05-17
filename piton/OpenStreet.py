import webbrowser
trame="$GPGGA,064036.289,4836.5375,N,00740.9373,E,1,04,3.2,200.2,M,,,,0000*0E"
typetrame = trame.split(",")
zoom = "16"

latitute_degrée = typetrame[2][0:2]
latitute_minute = typetrame[2][2:4]
latitute_second = str(float(typetrame[2][4:]) * 60)
latitute_direction = typetrame[5]
latitute = float(latitute_degrée) + float(latitute_minute)/60 + float(latitute_second)/3600 #+ latitute_direction

longitude_degrée = typetrame[4][0:2]
longitude_minute = typetrame[4][2:4]
longitude_second = str(float(typetrame[4][4:]) * 60)
longitude_direction = typetrame[5]
longitude = float(longitude_degrée) + float(longitude_minute)/60 + float(longitude_second)/3600 #+ latitude

webbrowser.open('https://www.openstreetmap.org/#map='+zoom+'/'+str(latitute)+'/'+str(longitude))
