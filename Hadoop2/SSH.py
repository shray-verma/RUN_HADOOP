import os,commands

def EXPORT_PATH():
	os.system("tar -xvzf hadoop-2.6.4.tar.gz")
	os.system("mv hadoop-2.6.4 /hadoop2")
	j=os.system("rpm -q jdk")
	if  j !=  0 :
		os.system("rpm -ivh jdk-7u79-linux-x64.rpm")
	os.system("exec bash &")

def COPY_XML(ip,filename,yarn=None):
	if yarn!=None:
		os.system("scp /root/Desktop/RUN_HADOOP/HADOOP2/XML_FILES/"+filename+ "  root@"+ip+":/hadoop2/etc/hadoop/yarn-site.xml")
		return
	if filename == "mapred-site.xml":
		 os.system("scp /root/Desktop/RUN_HADOOP/HADOOP2/XML_FILES/"+filename+ "  root@"+ip+":/hadoop2/etc/hadoop/mapred-site.xml")
	os.system("scp /root/Desktop/RUN_HADOOP/HADOOP2/XML_FILES/"+filename+ "  root@"+ip+":/hadoop2/etc/hadoop/"+filename)
