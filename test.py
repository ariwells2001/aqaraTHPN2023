import mysql.connector

connection = mysql.connector.connect(host='ariwells.kr',user='iotuser',password="iot12345", database='myaqara')
mycursor = connection.cursor()
    
sample_size = 4
    
mycursor.execute("select state from states where entity_id = 'sensor.0x00158d000232040e_temperature' order by state_id desc limit {}".format(sample_size))
# mycursor.execute("select temperature, humidity,pressure,discomfort from discomfortTable order by id desc limit {}".format(sample_size))

lastT=list(mycursor)

mycursor.execute("select state from states where entity_id = 'sensor.0x00158d000232040e_humidity' order by state_id desc limit {}".format(sample_size))

lastH = list(mycursor)

mycursor.execute("select state from states where entity_id = 'sensor.0x00158d000232040e_pressure' order by state_id desc limit {}".format(sample_size))

lastP = list(mycursor)
# print(lastData)
print(lastH)
print(lastT)
print(lastP)
print(float(lastT[0][0])-float(lastT[3][0]))
connection.commit()