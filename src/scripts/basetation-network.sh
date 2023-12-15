sudo apt install net-tools -y
sudo apt install ifupdown
sudo service network-manager stop
# BaseStation Adapter 1
echo "auto enx503eaa20a87d
iface enx503eaa20a87d inet static
address 199.0.1.2
netmask 255.255.0.0
broadcast 199.199.0.0" | sudo tee --append /etc/network/interfaces
# BaseStation Adapter 2
echo "auto enx503eaa231489
iface enx503eaa231489 inet static
address 199.0.1.2
netmask 255.255.0.0
broadcast 199.199.0.0" | sudo tee --append /etc/network/interfaces
# BaseStation Adapter 3
echo "auto enx503eaa2397ea
iface enx503eaa2397ea inet static
address 199.0.1.2
netmask 255.255.0.0
broadcast 199.199.0.0" | sudo tee --append /etc/network/interfaces
# BaseStation Adapter 4
echo "auto enx503eaa23975f
iface enx503eaa23975f inet static
address 199.0.1.2
netmask 255.255.0.0
broadcast 199.199.0.0" | sudo tee --append /etc/network/interfaces
# BaseStation Adapter 5
echo "auto enx503eaa231486
iface enx503eaa231486 inet static
address 199.0.1.2
netmask 255.255.0.0
broadcast 199.199.0.0" | sudo tee --append /etc/network/interfaces
sudo service network-manager start
sudo ifup -a
