clear
echo " ____  _               ____ "
echo "|  _ \(_)_ __   __ _  / ___|  ___ __ _ _ __ "
echo "| |_) | | \`_ \ / _\` | \___ \ / __/ _\` | '_ \ "
echo "|  __/| | | | | (_| |  ___) | (_| (_| | | | |"
echo "|_|   |_|_| |_|\__, | |____/ \___\__,_|_| |_|"
echo "               |___/"
echo "enter the first 3 octets."
echo "The scan will run from network 1 to network 254."
echo
read -p "Enther the subnet:  " SUBNET

for IP in $(seq 1 254); do
	ping -c 1 -w 1 $SUBNET.$IP | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done