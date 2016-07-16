import os,TUI,SSH,IP_LIST,WRITE_IP,commands,RUN_HADOOP,SECURITY

PATH="/root/RUN_HADOOP/HADOOP1/"
n,_=commands.getstatusoutput("rpm -q nmap")

if n != 0:
	os.system("cd /root/RUN_HADOOP/HADOOP1/")
  	os.system("rpm -ivh nmap-ncat-6.40-7.el7.x86_64.rpm")
        os.system("rpm -ivh nmap-6.40-7.el7.x86_64.rpm")

ip_list,ip=IP_LIST.GET_IP()
ip_list.remove(str(ip))

namenode=TUI.TUI(ip_list,"NAMENODE")
jobtracker=TUI.TUI(ip_list,"JOBTRACKER")
datanode=TUI.NODE_NO(ip_list,"DATANODE")

NODE=datanode
NODE =NODE+[namenode]
NODE =NODE+[jobtracker]

s,_=commands.getstatusoutput("rpm -q sshpass")

if  s  != 0 :
	commands.getoutput("rpm -i sshpass-1.05-5.el7.x86_64.rpm")

#os.system("ssh-keygen -f  /root/.ssh/f.rsa  -t  rsa  -N ''")

for i in NODE:
	SECURITY.SEC(i)
	#os.system("sshpass -p redhat ssh-copy-id  -o 'StrictHostKeyChecking no' root@"+i)
	os.system("scp "+PATH+"hadoop-1.2.1-1.x86_64.rpm   "+PATH+"jdk-7u79-linux-x64.rpm root@"+i+":/root/")
	os.system("scp "+PATH+"SSH.py root@" +i+":/root/")
	os.system("scp "+PATH+"INSTALL.py root@" +i+":/root/")
	os.system("ssh root@"+i+" python INSTALL.py")
	
os.system("rpm -ivh "+PATH+"hadoop-1.2.1-1.x86_64.rpm")   
os.system("rpm -ivh "+PATH+"jdk-7u79-linux-x64.rpm")

WRITE_IP.CLIENT_ENTRY(namenode)
WRITE_IP.MAPRED_ENTRY(jobtracker)

SSH.COPY_XML(namenode,"core-site.xml")
SSH.COPY_XML(jobtracker,"mapred-site.xml")
SSH.COPY_XML(namenode,"hdfs-site.xml")
SSH.COPY_XML(str(ip),"core-site.xml")

for i in datanode:
	SSH.COPY_XML(i,"core-site.xml")
	SSH.COPY_XML(i,"mapred-site.xml")
	SSH.COPY_XML(i,"hdfs-site.xml")
RUN_HADOOP.RUN_HADOOP(namenode,"namenode")
RUN_HADOOP.RUN_HADOOP(jobtracker,"jobtracker")

for i in datanode:
	RUN_HADOOP.RUN_HADOOP(i,"datanode")
	RUN_HADOOP.RUN_HADOOP(i,"tasktracker")
