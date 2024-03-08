#!/bin/sh
cp services/osmo-nitb2.service /lib/systemd/system
cp services/osmo-bts-trx2.service /lib/systemd/system
cp services/osmo-trx-lms2.service /lib/systemd/system
cp services/osmo-pcu2.service /lib/systemd/system
cp services/osmo-sgsn2.service /lib/systemd/system
cp services/osmo-ggsn2.service /lib/systemd/system
cp services/osmo-sip-connector2.service /lib/systemd/system

systemctl daemon-reload
