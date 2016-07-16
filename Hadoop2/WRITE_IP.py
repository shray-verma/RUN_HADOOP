import xml.etree.ElementTree as ET

PATH="/root/Desktop/RUN_HADOOP/HADOOP2/XML_FILES/"

def CLIENT_ENTRY(namenode):
	tree=ET.parse(PATH+"core-site.xml")
	root=tree.getroot()
	root[0][1].text="hdfs://"+namenode+":10001"
	tree.write(PATH+"core-site.xml")

def YARN_ENTRY1(resource_manager):
        tree=ET.parse(PATH+"yarn-site1.xml")
        root=tree.getroot()
        root[0][1].text=""+resource_manager+":8025"
        root[1][1].text=""+resource_manager+":8030"
        tree.write(PATH+"yarn-site1.xml")

def YARN_ENTRY2(resource_manager):
        tree=ET.parse(PATH+"yarn-site2.xml")
        root=tree.getroot()
        root[1][1].text=""+resource_manager+":8025"
        tree.write(PATH+"yarn-site2.xml")

def YARN_ENTRY3(resource_manager):
        tree=ET.parse(PATH+"yarn-site3.xml")
        root=tree.getroot()
	root[0][1].text=""+resource_manager+":8025"
        root[1][1].text=""+resource_manager+":8030"
	root[2][1].text=""+resource_manager+":8032"

