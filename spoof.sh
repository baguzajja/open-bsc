#!/bin/bash

gnome-terminal -- bash -c 'sudo python3 main_uhd_spoof.py -u --gprs -i wlp3s0 --sip; exec bash'

gnome-terminal -- bash -c 'sudo osmo-trx-uhd -C /usr/src/osmo-nitb-scripts/configs/osmo-trx-uhd.cfg; exec bash'
	
echo "Aplikasi Running"

