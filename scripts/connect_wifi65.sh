#!/bin/bash
echo "Connecting to 65 Callodine WiFi - GothamCity"
nmcli dev status
nmcli dev wifi list
nmcli dev wifi connect GothamCity password 65Cal_WiFi
