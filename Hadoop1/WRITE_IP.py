import xml.etree.ElementTree as ET

PATH="/root/Desktop/RUN_HADOOP/HADOOP2/XML_FILES/"

def CLIENT_ENTRY(namenode):
	tree=ET.parse(PATH+"core-site.xml")
	root=tree.getroot()
	root[0][1].text="hdfs://"+namenode+":10001"
	tree.write(PATH+"core-site.xml")

def MAPRED_ENTRY(jobtracker):
	tree=ET.parse(PATH+"mapred-site.xml")
	root=tree.getroot()
	root[0][1].text="hdfs://"+jobtracker+":9002"
	tree.write(PATH+"mapred-site.xml")
