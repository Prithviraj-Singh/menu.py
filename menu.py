import os
import subprocess

epel = subprocess.getoutput("rpm -qa | grep epel")
if epel != "epel-release-8-8.el8.noarch":
    print(epel)
    os.system("dnf -p install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")

os.system("clear")
while True:
	os.system("tput setaf 2")
	print("\t\t\tWELCOME TO THE MENU")
	os.system("tput setaf 7")
	print("\t\t\t____________________")
    
    
	print("""
		PRESS 1: to run date
		PRESS 2: for hadoop
	""")
	os.system("tput setaf 1")
	print("\t\tPRESS 11: to exit")
	os.system("tput setaf 7")
	ch = input("What technology would you like to work on today... enter the technology's number:")
    
	if int(ch) == 1:
		os.system("date")
	elif int(ch) == 2:
		x = subprocess.getoutput("jps")
		if "Jps" in x:
			os.system("jps")
		else:
			os.system("curl http://35.244.242.82/yum/java/el7/x86_64/jdk-8u171-linux-x64.rpm --output jdk-8u171-linux-x64.rpm")
			os.system("sudo rpm -i jdk-8u171-linux-x64.rpm --force")
		x = subprocess.getoutput("hadoop version")
		if "Hadoop" in x:
			os.system("hadoop version")
		else:
			os.system("curl https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm --output hadoop-1.2.1-1.x86_64.rpm")
		os.system("yum remove -y hadoop")
		os.system("sudo rpm -i hadoop-1.2.1-1.x86_64.rpm --force")
		os.system("clear")

		v = 0
		while v == 0: 
			print("""
			WELCOME TO HADOOP CONFIGURATION PAGE
			____________________________________


		PRESS 1: to configure Name Node
		PRESS 2: to configure Data Node
		PRESS 3: to configure Client Node
		PRESS 4: to change the size of blocks
		PRESS 5: to change the number of replications made
		PRESS 6: to exit to main-menu
		PRESS 7: to stop NameNode or DataNode services
		PRESS 8: to list all the files pressent in the main directory of HDFS
		PRESS 9: to read a file from HDFS
		PRESS 10: to upload a file to HDFS
			""")
			os.system("tput setaf 1")
			print("\t\tPRESS 11: to exit")
			os.system("tput setaf 7")

			def stop():
				x = subprocess.getoutput("jps")
				if "DataNode" in x:
					os.system("hadoop-daemon.sh stop datanode")
				if "NameNode" in x:
					os.system("hadoop-daemon.sh stop namenode")
			def hdfs(nod,fil):
				os.system("mkdir /{}".format(fil))
				x = open("/etc/hadoop/hdfs-site.xml","r")
				y = x.readlines()
				y.insert(6,"<property>\n<name>dfs.{}.dir</name>\n<value>/{}</value>\n</property>".format(nod,fil))
				x = open("/etc/hadoop/hdfs-site.xml","w")
				x.writelines(y)
				x.close()

			def core():
				a = open("/etc/hadoop/core-site.xml","r")
				b = a.readlines()
				ip = input("what is the ip address of the master : ")
				b.insert(6,"<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>".format(ip))
				a = open("/etc/hadoop/core-site.xml","w")
				a.writelines(b)
				a.close()

			def hdfs2(propert,value):
				x = open("/etc/hadoop/hdfs-site.xml","r")
				y = x.readlines()
				y.insert(6,"<property>\n<name>dfs.{}</name>\n<value>{}</value>\n</property>\n".format(propert,value))
				x = open("/etc/hadoop/hdfs-site.xml","w")
				x.writelines(y)
				x.close()
				
			had = input("Your answer : ")
			if int(had) == 1:
				stop()
				hdfs("name","nn")
				core()
				x = input("Do you want to format the Master Node[y/n] :")
				if "y" in x:
					os.system("hadoop namenode -format -Y")
				os.system("hadoop-daemon.sh start namenode")
			elif int(had) == 2:
				stop()
				hdfs("data","dn")
				core()
				os.system("hadoop-daemon.sh start datanode")
			elif int(had) == 3:
				core()
			elif int(had) == 4:
				bs = input("What size of block would you like to make (size in bytes):")
				hdfs2("block.size",bs)
			elif int(had) == 5:
				re = input("How many replication would you like to make:")
				hdfs2("replication",re)
			elif int(had) == 6:
				v = 1
				os.system("clear")
			elif int(had) == 7:
				stop()
			elif int(had) == 8:
				os.system("hadoop fs -ls")
			elif int(had) == 9:
				x = input("Enter the file's path on HDFS:")
				os.system("hadoop fs -cat /{}".format(x))
			elif int(had) == 10:
				x = input("Enter the file's path which you'd like to upload:")
				y = input("Enter the location in HDFS where you'd like to upload the file")
				os.system("hadoop fs -put {} /{}".format(x,y))
			elif int(had) == 11:
				os.system("tput setaf 2")
				print("Exiting...")
				os.system("tput setaf 7")
				exit()
			else:
				print("Command not found")
	elif int(ch) == 11:
		os.system("tput setaf 2")
		print("Exiting...")
		os.system("tput setaf 7")
		exit()
	else:
		os.system("tput setaf 1")
		print("COMMAND NOT RECOGNIZED!!!")
		os.system("tput setaf 7")
