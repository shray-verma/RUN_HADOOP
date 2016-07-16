import os,TUI,SSH,IP_LIST,WRITE_IP,commands,RUN_HADOOP,SECURITY
PATH="/root/Desktop/RUN_HADOOP/HADOOP2/"

n,_=commands.getstatusoutput("rpm -q nmap")

if n != 0:
	commands.getoutput("rpm -ivh "+PATH+"nmap-ncat-6.40-7.el7.x86_64.rpm")
	commands.getoutput("rpm -ivh "+PATH+"nmap-6.40-7.el7.x86_64.rpm")

ip_list,ip=IP_LIST.GET_IP()
ip_list.remove(str(ip))

namenode=ip_list[0]
resource_manager=ip_list[1]
datanode=[]
datanode.append(ip_list[2])
datanode.append(ip_list[3])

NODE=datanode
NODE=NODE+[namenode]
NODE=NODE+[resource_manager]
NODE=NODE+[str(ip)]

s,_=commands.getstatusoutput("rpm -q sshpass")

if  s  != 0 :
	commands.getoutput("rpm -i "+PATH+"sshpass-1.05-5.el7.x86_64.rpm")

#os.system("ssh-keygen -f  /root/.ssh/f.rsa  -t  rsa  -N ''")

for i in NODE:
	SECURITY.SEC(i)
	#os.system("sshpass -p redhat ssh-copy-id  -o 'StrictHostKeyChecking no' root@"+i)
	os.system("scp "+PATH+"hadoop-2.6.4.tar.gz  "+PATH+"jdk-7u79-linux-x64.rpm root@"+i+":/root/")
	os.system("scp "+PATH+"SSH.py root@" +i+":/root/")
	os.system("scp "+PATH+"INSTALL.py root@" +i+":/root/")
	os.system("scp "+PATH+"BASH_FILE/.bashrc root@"+i+":/root/.bashrc")
	os.system("ssh root@"+i+" python /root/INSTALL.py")

WRITE_IP.CLIENT_ENTRY(namenode)
WRITE_IP.YARN_ENTRY1(resource_manager)
WRITE_IP.YARN_ENTRY2(resource_manager)
WRITE_IP.YARN_ENTRY3(resource_manager)

SSH.COPY_XML(namenode,"core-site.xml")
SSH.COPY_XML(namenode,"hdfs-site.xml")
SSH.COPY_XML(resource_manager,"core-site.xml")
SSH.COPY_XML(resource_manager,"yarn-site1.xml",1)
SSH.COPY_XML(str(ip),"core-site.xml")
SSH.COPY_XML(str(ip),"mapred-site.xml")
SSH.COPY_XML(str(ip),"yarn-site3.xml",1)

for i in datanode:
	SSH.COPY_XML(i,"core-site.xml")
	SSH.COPY_XML(i,"hdfs-site.xml")
	SSH.COPY_XML(i,"yarn-site2.xml",1)
RUN_HADOOP.RUN_HADOOP(namenode,"namenode")
RUN_HADOOP.RUN_HADOOP(resource_manager,"resourcemanager")
for i in datanode:
	RUN_HADOOP.RUN_HADOOP(i,"datanode")
	RUN_HADOOP.RUN_HADOOP(i,"nodemanager")
