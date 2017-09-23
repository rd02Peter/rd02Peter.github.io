#!/bin/sh
ROMID="28-000000000000"

cat /sys/bus/w1/devices/$ROMID/w1_slave | \
  perl -e 'while(<stdin>){ if(/t=([-0-9]+)/){print $1/1000,"\n";} }'
