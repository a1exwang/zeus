:check_network
echo "Checking network"
ping 192.168.203.1 || goto check_network
echo "Network up"

net use X: \\192.168.203.1\nas\paradise

start C:\Users\ice_b\Desktop\thunder_backend\Thunder\Program\Thunder.exe
cd C:\Users\ice_b\Desktop\thunder_backend\
start python api.py