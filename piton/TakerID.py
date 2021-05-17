trame="$GPGGA,064036.289,4836.5375,N,00740.9373,E,1,04,3.2,200.2,M,,,,0000*0E"
typetrame = trame.split(",")
talkerId = typetrame[0][1:3]
if talkerId == "GP":
    print("your talker id is : GPS")
elif talkerId == "BD" or talkerId == "GB":
    print("your talker id is : Beidou")
elif talkerId == "GA":
    print("your talker id is : Galileo")
elif talkerId == "GL":
    print("your talker id is : GLONASS")


print(talkerId)
