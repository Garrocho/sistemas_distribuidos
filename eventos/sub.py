import paho.mqtt.client as mqtt

#hostname
broker="localhost"
#port
port=1883
#time to live
timelive=60
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/data")
def on_message(client, userdata, msg):
    print(msg.payload.decode())
    
client = mqtt.Client()
client.connect(broker,port,timelive)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
