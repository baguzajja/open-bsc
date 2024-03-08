import sqlite3
import telnetlib
import time
#should use python2 sending_sms_broadcast.py
Host="127.0.0.1"
Port="4242"

# launch ./set_imsi_extension for the first and use the same extension
numero_emetteur = "1234"

msg_a_envoyer = "Jangan Lupa Coblos 02 pada tanggal 14 Februari 2024"
localisation_base = '/var/lib/osmocom/hlr.sqlite3'
#if repetition = true with multiple repetition else with one sending only
#repetition = False



tn = telnetlib.Telnet(Host,Port)
conn = sqlite3.connect(localisation_base)
cursor = conn.cursor()

cursor.execute("""SELECT extension FROM subscriber""")
rows = cursor.fetchall()

for row in rows:
    cmd = "subscriber extension "+ str(row[0].encode('ascii')) + " sms sender extension " +  str(numero_emetteur) + " send " + str(msg_a_envoyer) + "\n"
    print(cmd)
    tn.write(str(cmd))
    time.sleep(1)



#while(repetition == True)
#    for row in rows:
#        cmd = "subscriber extension "+ row[0].encode('ascii') + " sms sender extension " +  numero_emetteur + " send " + msg_a_envoyer + "\n"
#        print cmd
#        tn.write(cmd)
#        time.sleep(1)


tn.write("exit")
tn.write("exit")
conn.close()
