import os

def SEC(ip):
	os.system("ssh root@"+ip+" setenforce 0")
	os.system("ssh root@"+ip+" iptables -F")
	os.system("ssh root@"+ip+" systemctl stop firewalld")
