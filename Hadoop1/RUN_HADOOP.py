import os

def RUN_HADOOP(ip,NODE):
	if NODE == 'namenode':
		os.system("ssh "+ip+"  hadoop namenode -format")
	os.system("ssh "+ip+" hadoop-daemon.sh start "+NODE)
