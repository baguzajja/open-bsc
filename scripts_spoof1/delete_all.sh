#! /bin/bash
# bash delete_all.sh
#cd /home/pi/Desktop/karli/ 
sqlite3 -line /var/lib/osmocom/hlr.sqlite3 'delete from subscriber;'
