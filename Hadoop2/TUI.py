import os
def TUI(IP_LIST,NODE):
	string_1="dialog --radiolist 'SELECT "+ NODE+" \n IPs ARE : ' 15 35 "+str(len(IP_LIST))+" "

	for i in range(len(IP_LIST)):
        	string_1 = string_1 + str(i+1) +" "+ IP_LIST[i]+" off "
	
	os.system(string_1+" 2>/tmp/ch.txt")
	f1=open('/tmp/ch.txt','r')
	ch=f1.read()
	nodeip=IP_LIST[int(ch)-1]
	IP_LIST.remove(nodeip)
	return nodeip
	
def NODE_NO(IP_LIST,NODE):
	os.system("dialog --inputbox 'SELECT NUMBER OF "+NODE+"' 15 35  ""2>/tmp/ch1.txt")
	f1=open('/tmp/ch1.txt','r')
	ch1=int(f1.read())
	nodeip=[]
	i=0
	while i < ch1:
		nodeip.append(IP_LIST[i])
		i=i+1
	return nodeip
	
