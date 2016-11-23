#!/usr/bin/env bash

ping -c 5 127.0.0.1
exit

# import into triple store
echo -e "\n----------"
echo "1. Import into triple store"
python auto_import.py "$1" pro

echo -e "\n----------"
echo "DONE!"