import os,commands

d,_=commands.getstatusoutput("rpm -q dialog")

if d != 0:
	commands.getoutput("rpm -ivh dialog-1.2-4.20130523.el7.i686.rpm")

os.system("dialog --radiolist 'SELECT HADOOP VERSION' 10 30 2 1 'HADOOP-1' off 2 'HADOOP-2' off 2>/tmp/ch2.txt")
version=int(open("/tmp/ch2.txt").read())
os.system("dialog --radiolist 'SELECT PROCEDURE' 10 30 2 1 'AUTOMATIC' off 2 'MANUAL' off 2>/tmp/ch3.txt")
install=int(open("/tmp/ch3.txt").read())
if install == 1:
	if version == 1:
        	os.system("python ./HADOOP1/AUTO1.py")
	else:
        	os.system("python ./HADOOP2/AUTO2.py")

else:
	if version == 1:
		os.system("python ./HADOOP1/MAN1.py")
	else:
		os.system("python ./HADOOP2/MAN2.py")
