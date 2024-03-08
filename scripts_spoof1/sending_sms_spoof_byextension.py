#should use python2_sms_spoof_byextension.py
import sqlite3
import telnetlib
import time

Host="127.0.0.1"
Port="4242"
numero_emetteur = "0341220590"  #launch ./set_imsi_extension for the first and use the same extension
numero_destinataire = "0341220590"
msg_a_envoyer = "ALERT Corona virus"

#if repetition = true with multiple repetition else with one sending only
#repetition = False



tn = telnetlib.Telnet(Host,Port)


#subscriber imsi 012340123456789 sms sender imsi 987654321043210 send test123 
cmd = "subscriber extension "+ numero_destinataire + " sms sender extension " +  numero_emetteur + " send " + msg_a_envoyer + "\n"
print cmd
tn.write(cmd)
time.sleep(1)

#while(repetition == True)
#    for row in rows:
#        cmd = "subscriber extension "+ row[0].encode('ascii') + " sms sender extension " +  numero_emetteur + " send " + msg_a_envoyer + "\n"
#        print cmd
#        tn.write(cmd)
#        time.sleep(1)


tn.write("exit")
tn.write("exit")
