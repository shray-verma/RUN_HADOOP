import os,commands

def INSTALL():
	h=os.system("rpm -q hadoop")
	j=os.system("rpm -q jdk")
	if  h !=  0 :
		os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --replacefiles")
	if  j !=  0 :
		os.system("rpm -ivh jdk-7u79-linux-x64.rpm")
def COPY_XML(ip,filename):
	os.system("scp /root/Desktop/RUN_HADOOP/HADOOP1/XML_FILES/"+filename+ "  root@"+ip+":/etc/hadoop/")
