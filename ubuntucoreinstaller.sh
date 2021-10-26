#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
echo 'Install the robotics firmware on the ubuntu core'
echo "Installing classic environment"
sudo snap install classic --devmode -edge 
sudo classic
sudo apt-get update && sudo apt-get upgrade -y #Upgrade and update 
sudo apt-get install nano -y 
sudo apt-get install git -y 
# Config the uart port seeking the uart /dev/ttyS0 on the  /sys/class/tty/ 
sudo chmod 777 /dev/ttyAMA0 #permiss the AMA0 serial 
sudo chmod 777 /dev/ttyS0   #permiss the S0 serial 
sudo apt-get install python3-dev -y 
sudo apt-get install python3-pip -y 
sudo apt-get install python3-setuptools -y
groups ${USER}
sudo gpasswd --add ${USER} dialout
sudo apt-get install supervisor -y 


