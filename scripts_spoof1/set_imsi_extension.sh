#! /bin/bash
#bash set_imsi_extension "imsi number" "extension number"
#cd /home/pi/Desktop/karli/ 


sqlite3 -line /var/lib/osmocom/hlr.sqlite3 "update Subscriber set extension='$2' where imsi='$1';"

echo ""
echo ""
echo "setting imsi : " $1 " as extension : " $2
echo "Please test with *#100# on your phone"
