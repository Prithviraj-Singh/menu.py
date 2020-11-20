import os
import subprocess as sp

x = input("Are you logged in as root???[y/n]")
if "n" in x:
    os.system("sudo su - root")
epel = sp.getoutput("rpm -qa | grep epel")
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
		PRESS 2: for Hadoop Configuration Automation Tool
		PRESS 3: for AWS Configuration Automation Tool
		PRESS 4: for Linux Automation Tool
		PRESS 5: for Logical Volume Management Automation
	""")
    os.system("tput setaf 1")
    print("\t\tPRESS 11: to exit")
    os.system("tput setaf 7")
    ch = input("What technology would you like to work on today... enter the technology's number:")

    if int(ch) == 1:
        os.system("date")
    elif int(ch) == 2:
        x = sp.getoutput("jps")
        if "Jps" in x:
            os.system("jps")
        else:
            os.system(
                "curl http://35.244.242.82/yum/java/el7/x86_64/jdk-8u171-linux-x64.rpm --output jdk-8u171-linux-x64.rpm")
            os.system("sudo rpm -i jdk-8u171-linux-x64.rpm --force")
        x = sp.getoutput("hadoop version")
        if "Hadoop" in x:
            os.system("hadoop version")
        else:
            os.system(
                "curl https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm --output hadoop-1.2.1-1.x86_64.rpm")
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
                x = sp.getoutput("jps")
                if "DataNode" in x:
                    os.system("hadoop-daemon.sh stop datanode")
                if "NameNode" in x:
                    os.system("hadoop-daemon.sh stop namenode")


            def hdfs(nod, fil):
                os.system("mkdir /{}".format(fil))
                x = open("/etc/hadoop/hdfs-site.xml", "r")
                y = x.readlines()
                y.insert(6, "<property>\n<name>dfs.{}.dir</name>\n<value>/{}</value>\n</property>".format(nod, fil))
                x = open("/etc/hadoop/hdfs-site.xml", "w")
                x.writelines(y)
                x.close()


            def core():
                a = open("/etc/hadoop/core-site.xml", "r")
                b = a.readlines()
                ip = input("what is the ip address of the master : ")
                b.insert(6,
                         "<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>".format(
                             ip))
                a = open("/etc/hadoop/core-site.xml", "w")
                a.writelines(b)
                a.close()


            def hdfs2(propert, value):
                x = open("/etc/hadoop/hdfs-site.xml", "r")
                y = x.readlines()
                y.insert(6, "<property>\n<name>dfs.{}</name>\n<value>{}</value>\n</property>\n".format(propert, value))
                x = open("/etc/hadoop/hdfs-site.xml", "w")
                x.writelines(y)
                x.close()


            had = input("Your answer : ")
            if int(had) == 1:
                stop()
                hdfs("name", "nn")
                core()
                x = input("Do you want to format the Master Node[y/n] :")
                if "y" in x:
                    os.system("hadoop namenode -format -Y")
                os.system("hadoop-daemon.sh start namenode")
            elif int(had) == 2:
                stop()
                hdfs("data", "dn")
                core()
                os.system("hadoop-daemon.sh start datanode")
            elif int(had) == 3:
                core()
            elif int(had) == 4:
                bs = input("What size of block would you like to make (size in bytes):")
                hdfs2("block.size", bs)
            elif int(had) == 5:
                re = input("How many replication would you like to make:")
                hdfs2("replication", re)
            elif int(had) == 6:
                v = 1
                os.system("clear")
            elif int(had) == 7:
                stop()
            elif int(had) == 8:
                x = input("Enter the name of any specific folder name on HDFS which you'd like to list in: /")
                os.system("hadoop fs -ls /{}".format(x))
            elif int(had) == 9:
                x = input("Enter the file's path on HDFS: /")
                os.system("hadoop fs -cat /{}".format(x))
            elif int(had) == 10:
                x = input("Enter the file's path which you'd like to upload:")
                y = input("Any specific folder where you'd like to upload your file")
                os.system("hadoop fs -put {} /{}".format(x, y))
            elif int(had) == 11:
                os.system("tput setaf 2")
                print("Exiting...")
                os.system("tput setaf 7")
                exit()
            else:
                print("Command not found")

    elif int(ch) == 3:

        def new_instance():  # function for creation of new instance

            a = 0
            while a == 0:
                print("""
                Steps to create new ec2- instance:
                *If you already have key-pair,Security-Group you can proceed to
                step 3* else start with step 1:\n
                Step 1: Create key-pair
                Step 2: Create Security group
                step 3: Create new Instance
                Press 4: Go Back
            ___________________________________________________________
                        """)
                choice = input("Enter your choice: ")
                if int(choice) == 1:
                    keyname = input("Enter unique key-pair name of your choice:")
                    cmd1 = "aws ec2 create-key-pair --key-name {0}".format(keyname)
                    check = sp.getstatusoutput(cmd1)
                    status1 = check[0]
                    out1 = check[1]
                    if status1 == 0:
                        print("Key-pair named {0} created successfully".format(keyname))
                        print("{0}".format(out1))
                        new_instance()
                    else:
                        print("Something went wrong {}".format(out1))
                        new_instance()
                if int(choice) == 2:
                    name = input("Enter security group name of your choice")
                    cmd2 = "aws ec2 create-security-group --group-name {0} --description \"security group\" ".format(
                        name)
                    check1 = sp.getstatusoutput(cmd2)
                    status2 = check1[0]
                    out2 = check1[1]
                    if status2 == 0:
                        print("Security group name {0} create successfully".format(name))
                        print("Security- Group id: {0}".format(out2))
                        new_instance()
                    else:
                        print("Error : {0} ".format(out2))
                        new_instance()
                elif int(choice) == 3:
                    keyname = input("Enter Key name: ")
                    sg = input("Enter Security group id : ")
                    image = input("Enter Image id: ")
                    instance_type = input("Enter Instance type E.g : t2.micro : ")
                    count = input("Enter the count of the Image : ")
                    subnet = input("Enter subnet id :")
                    cmd3 = "aws ec2 run-instances --image-id {0} --instance-type {1} --count {2} --subnet-id {3} --security-group-ids {4} --key-name {5}".format(
                        image, instance_type, count, subnet, sg, keyname)
                    check2 = sp.getstatusoutput(cmd3)
                    status3 = check2[0]
                    out3 = check2[1]
                    if status3 == 0:
                        print("Instance id {0} Launched Successfully".format(image))
                    else:
                        print("Error Occured: {0}".format(out3))

                elif int(choice) == 4:
                    break


        # Here the Create_Instance Function Ends....

        def start_stop():  # Function for starting and stoping the running instance
            b = 0
            while b == 0:
                print("""
                Press 1: Start Instance
                Press 2: Stop Instance
                Press 3: Go back
            ___________________________________________________________
                        """)
                ch1 = input("Enter your choice: ")
                if int(ch1) == 1:
                    cmd4 = "aws ec2 describe-instances"
                    display = sp.getstatusoutput(cmd4)
                    out4 = display[0]
                    show = display[1]
                    if out4 == 0:
                        print("{0}".format(show))
                        print(
                            "Following are the instances running in the region, scroll up and you will find instance id \n")
                        select = input("Enter Instance ID : ")
                        cmd5 = "aws ec2 start-instances --instance-ids {0}".format(select)
                        run = sp.getstatusoutput(cmd5)
                        status5 = run[0]
                        out5 = run[1]
                        print("{0}".format(out5))
                        if status5 == 0:
                            print("Instance id {0} started successfully".format(select))
                            start_stop()
                        else:
                            print("Something went wrong...!")
                            start_stop()
                    else:
                        print("Something went wrong")
                        start_stop()
                if int(ch1) == 2:
                    cmd6 = "aws ec2 describe-instances"
                    display1 = sp.getstatusoutput(cmd6)
                    out6 = display1[0]
                    show1 = display1[1]
                    print("{0}".format(out6))
                    if out6 == 0:
                        print("{0}".format(show1))
                        select1 = input("Enter Instance ID : ")
                        cmd7 = "aws ec2 stop-instances --instance-ids {0}".format(select1)
                        run1 = sp.getstatusoutput(cmd7)
                        status6 = run1[0]
                        out7 = run1[1]
                        print("{0}".format(out7))
                        if status6 == 0:
                            print("Instance id {0} stopped successfully".format(select1))
                            start_stop()
                        else:
                            print("Something went wrong...!")
                            start_stop()
                    else:
                        print("Something went wrong")
                        start_stop()
                if int(ch1) == 3:
                    break


        # Here the funtion start/stop() ends.....

        def ebsblock():  # Function to create EBS Volume
            c = 0
            while c == 0:
                print("""
                Menu:
                Press 1: To Ceate new EBS Volume
                Press 2: To Attach EBS Volume
                Press 3: To Detach EBS Volume
                Press 4: To Delete the EBS Volume
                Press 5: Go back
            ___________________________________________________________
                        """)
                ch3 = input("Enter your choice: ")
                if int(ch3) == 1:
                    select2 = input("Enter availability zone eg:(ap-south-1a/1b/1c): ")
                    size = input("Enter the size of EBS Block (in GB) : ")
                    cmd8 = "aws ec2 create-volume --availability-zone {0} --size {1} ".format(select2, size)
                    check3 = sp.getstatusoutput(cmd8)
                    status7 = check3[0]
                    out8 = check3[1]
                    if status7 == 0:
                        print("EBS Block of size {0} GB is created in the zone {1}".format(size, select2))
                        print("{}".format(out8))
                    else:
                        print("Something went wront...!")
                        ebsblock()

                if int(ch3) == 2:
                    cmd9 = "aws ec2 describe-instances"
                    display2 = sp.getstatusoutput(cmd9)
                    out9 = display2[0]
                    show2 = display2[1]
                    print("{0}".format(show2))
                    select4 = input("Enter the Instance ID where the EBS block is to be attached: ")
                    cmd10 = "aws ec2 describe-volumes"
                    check4 = sp.getstatusoutput(cmd10)
                    out10 = check4[1]
                    print("{}".format(out10))
                    volume = input("Enter Volume id you want to attach to instance: ")
                    device = input("Enter Device name:")
                    cmd11 = "aws ec2 attach-volume --instance-id {0} --volume-id {1} --device {2}".format(select4,
                                                                                                          volume,
                                                                                                          device)
                    check5 = sp.getstatusoutput(cmd11)
                    out11 = check5[1]
                    print("{0}".format(out11))
                    ebsblock()

                if int(ch3) == 3:
                    cmd12 = "aws ec2 describe-volumes"
                    display3 = sp.getstatusoutput(cmd12)
                    out12 = display3[1]
                    print("{0}".format(out12))
                    print(
                        "***For normal detach you can goto the instance and unmount the volume first, else you can do it from here forcefully..***")
                    select5 = input("Enter the volume id to be detached : ")
                    cmd13 = "aws ec2 detach-volume --volume-id {0} --force".format(select5)
                    check6 = sp.getstatusoutput(cmd13)
                    out13 = check6[1]
                    print("Detach Status: \n {}".format(out13))
                    ebsblock()

                if int(ch3) == 4:
                    cmd15 = "aws ec2 describe-volumes"
                    display4 = sp.getstatusoutput(cmd15)
                    out15 = display4[1]
                    print("{0}".format(out15))
                    select6 = input("Enter the volume id to be deleted : ")
                    cmd14 = "aws ec2 delete-volume --volume-id {0} ".format(select6)
                    check7 = sp.getstatusoutput(cmd14)
                    out14 = check7[1]
                    print("Delete Status: \n {}".format(out14))
                    ebsblock()

                if int(ch3) == 5:
                    break


        # End of EBS Volume....

        def s3_bucket():
            d = 0
            while d == 0:
                print("""
                Press 1: Creation of S3 Bucket
                Press 2: Upload file's into S3 Bucket
                Press 3: To empty S3 and delete S3 Bucket
                Press 4: Go Back
            ___________________________________________________________
                        """)
                ch4 = input("Enter your choice : ")

                if int(ch4) == 1:
                    select7 = input("Enter a unique name for S3 Bucket: ")
                    region = input("Enter region name eg(ap-south-1) : ")
                    location = input("Enter Location Constraint: eg(ap-south-1): ")
                    cmd16 = "aws s3api create-bucket --bucket {0} --region {1} --acl public-read --create-bucket-configuration LocationConstraint={2}".format(
                        select7, region, location)
                    check8 = sp.getstatusoutput(cmd16)
                    out16 = check8[1]

                    print(" S3 Bucket with name {0} created successfully in the region {1} : \n {2}".format(select7,
                                                                                                            region,
                                                                                                            out16))
                    s3_bucket()

                if int(ch4) == 2:
                    select7 = input("Enter the absolute location of file eg (C:/User/Desktop/filename): ")
                    cmd17 = "aws s3 ls"
                    check9 = sp.getstatusoutput(cmd17)
                    out17 = check9[1]
                    print("{0}".format(out17))
                    select8 = input("Enter Bucket name: ")
                    cmd18 = "aws s3 cp {0} s3://{1}/ --acl public-read".format(select7, select8)
                    check10 = sp.getstatusoutput(cmd18)
                    out18 = check10[1]
                    print("Status : \n {0} ".format(out18))
                    s3_bucket()

                if int(ch4) == 3:
                    cmd19 = "aws s3 ls"
                    check11 = sp.getstatusoutput(cmd19)
                    out19 = check11[1]
                    print("{}".format(out19))
                    print("Note: To delete, you to first empty the bucket")
                    select9 = input("Enter the bucket name to be emptied and deleted: ")
                    cmd20 = "aws s3 rm s3://{} --recursive".format(select9)
                    check12 = sp.getstatusoutput(cmd20)
                    out20 = check12[1]
                    print("{}".format(out20))
                    cmd21 = "aws s3 rb s3://{} --force".format(select9)
                    check13 = sp.getstatusoutput(cmd21)
                    out21 = check13[1]
                    print("{}".format(out21))
                    s3_bucket()

                if int(ch4) == 4:
                    break


        # End of S3_bucket function.....

        def cloudfront():
            e = 0
            while e == 0:  # Function for creation of CloudFront
                print("""
                Press1: Create CloudFront
                Press2: Delete CloudFront
                Press3: Go back
            ___________________________________________________________
                        """)
                ch6 = input("Enter your choice: ")
                if int(ch6) == 1:
                    print("Below is the List of S3 bucket you have created: \n")
                    cmd22 = "aws s3 ls"
                    select14 = input("Enter the S3 bucket link eg(bucket-name.s3.amazon.com): ")
                    cmd23 = "aws cloudfront create-distribution --origin-domain-name {}".format(select14)
                    check14 = sp.getstatusoutput(cmd23)
                    out22 = check14[1]
                    print("{}".format(out22))
                    cloudfront()
                if int(ch6) == 2:
                    print(
                        "****Note : Please first manually disable the cloudfront from GUI before deleting cloudfront distribution ****")
                    cmd23 = "aws cloudfront list-distributions"
                    check15 = sp.getstatusoutput(cmd23)
                    out23 = check15[1]
                    print("{}".format(out23))
                    select15 = input("Enter the CloudFront id location at the top : ")
                    cmd24 = "aws cloudfront get-distribution --id {}".format(select15)
                    check16 = sp.getstatusoutput(cmd24)
                    out24 = check16[1]
                    print("{}".out24)
                    select16 = input("Enter the ETag credentials located at the top : ")
                    cmd25 = "aws cloudfront delete-distribution --id {} --if-match {}".format(select15, select16)
                    check17 = sp.getstatusoutput(cmd25)
                    print("Distribution deleted successfully..!")
                    cloudfront()
                if int(ch6) == 3:
                    break


        awscli = sp.getstatusoutput("aws --version")

        status = awscli[0]

        if status != 0:
            print("AWS CLI is not installed in your system, Kindly install it with below options")
            r = 0
            while r == 0:

                print("""
            *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
                AWS CLI installation module: \n
                Press 1:Install AWS CLI software
                Press 2:Check Aws Version
                Press 3:To Exit
            ___________________________________________________________
                        """)
                ch7 = input("Enter your choice")
                if int(ch7) == 1:
                    os.system("clear")
                    h = 0
                    while h == 0:
                        print("""
                Press 1:Windows
                Press 2:Mac
                Press 3:Linux
                Press 4:Exit
            ___________________________________________________________
                                """)
                        cli = input("Enter Your choice: ")

                        if int(cli) == 1:
                            os.system("pip3 install awscli --upgrade --user")
                            print("If it is not working properly try to install by GUI.")

                        elif int(cli) == 2:
                            os.system("curl https://s3.amazonaws.com/aws-cli/awscli-bundle.zip -o awscli-bundle.zip")
                            os.system("unzip awscli-bundle.zip")
                            os.system("sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws")

                        elif int(cli) == 3:
                            os.system("curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o awscliv2.zip")
                            os.system("unzip awscliv2.zip")
                            os.system("sudo ./aws/install")
                            os.system("sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin")
                        elif int(cli) == 4:
                            break

                if int(ch7) == 2:
                    os.system("aws --version")

                if int(ch7) == 3:
                    break
            print("If you have'nt configured the AWS CLI, please configure it first before taking 	further choice's")
            f = 0
            while f == 0:
                os.system("clear")
                print("""
                Menu:
                Press 1: Configure AWS CLI with Account
                press 2: Create new Instance
                Press 3: Start/Stop Instance
                Press 4: Create EBS Volume
                Press 5: Create S3 Bucket
                Press 6: Create CloudFront
                Press 7: Exit
            ___________________________________________________________	
                        """)
                ch = input("Enter your choice: ")

                if int(ch) == 1:
                    print("Create an IAM User from AWS GUI and there you will get Access key and access password")
                    print("Link: https://aws.amazon.com")
                    cmd = "aws configure"
                    os.system(cmd)
                elif int(ch) == 2:
                    new_instance()
                elif int(ch) == 3:
                    start_stop()
                elif int(ch) == 4:
                    ebsblock()
                elif int(ch) == 5:
                    s3_bucket()
                elif int(ch) == 6:
                    cloudfront()
                elif int(ch) == 7:
                    break

        else:

            v = 0
            while v == 0:
                os.system("clear")
                print("Welcome user, How can i help you..?")
                print("""
            *_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*
                Menu:
                Press 1: Configure Awscli with Account(Initial step)
                press 2: Create Instance
                Press 3: Start/Stop Instance
                Press 4: EBS Volume
                Press 5: S3 services
                Press 6: Create CloudFront
                Press 7: Exit
            ___________________________________________________________
                        """)

                ch = input("Enter your choice: ")

                if int(ch) == 1:
                    print("Create an IAM User from AWS GUI and there you will get Access key and access password")
                    print("Link: https://aws.amazon.com")
                    cmd = "aws configure"
                    os.system(cmd)
                elif int(ch) == 2:
                    new_instance()
                elif int(ch) == 3:
                    start_stop()
                elif int(ch) == 4:
                    ebsblock()
                elif int(ch) == 5:
                    s3_bucket()
                elif int(ch) == 6:
                    cloudfront()
                elif int(ch) == 7:
                    break

    elif int(ch) == 4:
        import getpass as gp


        def yum(name):
            o = sp.getoutput(name)
            if "command not found" in o:
                os.system("echo `yum -q whatprovides {}` > c.txt".format(name))
                x = open("c.txt", "r")
                y = x.readlines(1)
                x = y[0]
                y = x.rsplit(' ')
                x = y[0]
                os.system("yum install {}".format(x))


        v = 0
        while v == 0:
            os.system("tput setaf 2")
            print("\t\tWelcome to Linux automation tool!!!")
            os.system("tput setaf 7")
            print("""



        	PRESS 1: to show Present Working Directory (Directory which the user is on)
        	PRESS 2: to list all the items in Present working directory
        	PRESS 3: to get a detailed list of items in Present Working Directory
        	PRESS 4: to change directory
        	PRESS 5: to make an empty file in Present Working Directory
        	PRESS 6: to create a directory in Present Working Directory
        	PRESS 7: to read a file
        	PRESS 8: to show date
        	PRESS 9: to show calender
        	PRESS 10: to show time (hh:mm:ss)
        	PRESS 12: to show all the processes running in the background
        	PRESS 13: to bring any background process to foregound
        	PRESS 14: to add user account
        	PRESS 15: to see which user you are using
        	PRESS 16: to open firefox
        	PRESS 17: to use calculator
        	PRESS 18: to use do remote login to a system
        	PRESS 19: to show IP adress
        	PRESS 20: to show packet exchange
        	PRESS 21: to show CPU details
        	PRESS 22: to show Port details
        	PRESS 23: to Shutdown the system
        	PRESS 24: to Reboot
        	PRESS 25: to switch user
        	PRESS 26: to send a file to a system in the same network
        	PRESS 27: to give detailes list of harddisk
        	PRESS 28: to exit to main menu
        	PRESS 29: to remove something
		PRESS 30: to install packages based on command name
        		""")
            os.system("tput setaf 1")
            print("\t\tPRESS 11: to exit")
            os.system("tput setaf 7")

            i = input("What would you like the program to do? :")
            if int(i) == 1:
                yum("pwd")
                os.system("pwd")
            elif int(i) == 2:
                yum("ls")
                os.system("ls")
            elif int(i) == 3:
                yum("ls")
                os.system("ls -l")
            elif int(i) == 4:
                yum("cd")
                op = input("Give the path of directory where you'd like to land:")
                os.system("cd {}".format(op))
            elif int(i) == 5:
                yum("touch")
                op = input("What name should th file have:")
                os.system("op")
            elif int(i) == 6:
                yum("mkdir")
                os.system("What name should the folder have:")
            elif int(i) == 7:
                yum("cat")
                op = input("Give the name of the file or path of the file:")
                os.system("cat {}".format(op))
            elif int(i) == 8:
                yum("date")
                os.system("date")
            elif int(i) == 9:
                yum("cal")
                os.system("cal")
            elif int(i) == 10:
                yum("date")
                os.system("date +%T")
            elif int(i) == 12:
                yum("jobs")
                os.system("jobs")
            elif int(i) == 13:
                yum("fg")
                op = input("What the process ID of the process you'd like to bring to the foreground:")
                os.system("fg {}".format(op))
            elif int(i) == 14:
                yum("useradd")
                op = input("What is the name of New User:")
                pas = gp.getpass()
                os.system("useradd {} -p {}".format(op, pas))
            elif int(i) == 15:
                yum("whoami")
                os.system("whoami")
            elif int(i) == 16:
                yum("firefox")
                os.system("firefox")
            elif int(i) == 17:
                yum("bc")
                os.sytem("bc")
            elif int(i) == 18:
                yum("ssh")
                op = input("What's the IP of the system you'd like to ssh to:")
                os.system("ssh {}".format(op))
            elif int(i) == 19:
                yum("ifconfig")
                os.system("ifconfig enp0s3")
            elif int(i) == 20:
                yum("tcpdump")
                op = input("Would you like to make a file of all th log?[y/n]:")
                if "y" in op:
                    os.system("tcpdump -i enp0s3 -n -w packets.txt")
                    os.system("tcpdump -r -n packets.txt -x > newpackets.txt")
                    os.system("cat newpackets.txt")
                else:
                    os.system("tcpdump -i -n enp0s3")
            elif int(i) == 21:
                yum("lscpu")
                os.system("lscpu")
            elif int(i) == 22:
                yum("netstat")
                os.system("netstat -tnlp")
            elif int(i) == 23:
                yum("init")
                os.system("init 0")
            elif int(i) == 24:
                yum("init")
                os.system("inti 6")
            elif int(i) == 25:
                op = input("Name of the user you'd like to switch to:")
                yum("su")
                os.system("su {}".format(su))
            elif int(i) == 26:
                yum("scp")
                op = input("Give the path to the file you'd like to send:")
                op1 = input("Give the IP of the system you'd like to send the file to:")
                op2 = input("Location where you'd like to store the file: /")
                os.system("scp {} {}:/{}".format(op, op1, op2))
            elif int(i) == 28:
                v = 1
                os.system("clear")
            elif int(i) == 29:
                op = input("Do you want to remove a file or a directory [f/d]")
                if "f" in op:
                    yum("rm")
                    op1 = input("Name or the path of the file you'd like to remove:")
                    os.system("rm {}".format(op1))
                else:
                    yum("rmdir")
                    op1 = input("Name or the path of the directory you'd like to remove:")
                    os.system("rmdir {}".format(op1))
            elif int(i) == 27:
                yum("fdisk")
                op = input("For what harddisk would you like to get the details leave empty for all")
                os.system("fdisk -l {}".format(op))
            elif int(i) == 11:
                exit()
            elif int(i) == 30:
                op = input("Type the command for which you'd like to install the package")
                yum(op)
            else:
                os.system("tput setaf 1")
                print("COMMAND NOT FOUND!!!")
                os.system("tput setaf 7")


    elif int(ch) == 11:
        os.system("tput setaf 2")
        print("Exiting...")
        os.system("tput setaf 7")
        exit()
   
    elif int(ch) == 5:
        def lvcreate(i):
            x = input("What should be the size of your logical volume(Numeric value): ")
            z = input("What is the unit of your given size: ")
            if ("m" in z or "M" in z):
                z = "M"
            elif ("k" in z or "K" in z):
                z = "K"
            else:
                z = "G"
            name = input("What should be the name of your lv :")
            os.system("lvcreate --size {}{} --name {} {}".format(x, z, name, i))
            ty = input(
                "In which format type whould you like to format your new Logical volume (recommended/default type 'ext4'): ")
            if ty == "xfs":
                os.system("mkfs.xfs /dev/{}/{}".format(i, name))
            elif (ty == "ext4" or ty == "" or ty == " "):
                print("Good choice!!!")
                os.system("mkfs.ext4 /dev/{}/{}".format(i, name))
            else:
                print("""Type not supported!!!...
        Formating in the default format""")
                os.system("mkfs.ext4 /dev/{}/{}".format(i, name))
            q = input("Give a suitable name or path of a directory for your Logical Volume: ")
            os.system("mkdir {}".format(q))
            os.system("mount /dev/{}/{} {}".format(i, name, q))
            print("Your Logical Volume {} is ready to be used in the directory {}".format(name, q))
    
    
        def create():
            print("which harddisk would you like to give lvm capablities")
            i = input("Enter a suitable name for your volume group: ")
            y = "vgcreate " + i
            while (True):
                z = input("Enter the name of the harddisk or press q to quit: ")
                if z == "q":
                    break
                else:
                    stat = sp.getoutput("pvcreate {}".format(z))
                    y += " {}".format(z)
                    print(stat)
            os.system(y)
            opt = input("Do you want to create a Logial Volume[y/n]: ")
            if "y" in opt:
                lvcreate(i)
    
    
        os.system("clear")
        while (True):
            os.system("tput setaf 5")
            print("""
                    Welcome to my LVM menu
                    ______________________
            """)
            os.system("tput setaf 12")
            print("""
            PRESS 1: for making a new storage device capable of LVM
            PRESS 2: for making a new Logical Volume from an existing Volume Group
            PRESS 3: for showing all storage devices
            PRESS 4: for showing existing Logical Volumes
            PRESS 5: for showing existing Physical Volumes
            PRESS 6: for showing existing Volume Group
            PRESS 7: for changing space of a prexisting Logical Volume
            PRESS 8: to exit to main-menu
            """)
            os.system("tput setaf 1")
            print("	Print 11 to Exit")
            os.system("tput setaf 7")
            o = input("What would you like the application to do: ")
            if int(o) == 1:
                create()
            elif int(o) == 2:
                q = input("From which volume group would you like to make the Logical-Volume: ")
                lvcreate(q)
            elif int(o) == 3:
                q = input("Write the name of any particular drive to show details (default  shows all): ")
                os.system("fdisk -l")
            elif int(o) == 4:
                q = input("Write the name of volume group you'd like to see LVs from (default shows all): ")
                os.system("lvdisplay {}".format(q))
            elif int(o) == 5:
                q = input("Write the name of any physical drive to show its details (default shows all): ")
                os.system("pvdisplay {}".format(q))
            elif int(o) == 6:
                q = input("Write the name of a particular VG to show its details (default show all): ")
                os.system("vgdisplay {}".format(q))
            elif int(o) == 7:
                q = input("What is the format type of your Logical Volume (default ext4): ")
                if q != "xfs":
                    q1 = input("What would you like to do to the space of your LV[add/sub]")
                    if "ad" in q1:
                        q1 = input("How much space would you like to add(enter the numeric value): ")
                        q2 = input("What is the unit of given size?[M/K/G] : ")
                        if ("m" in q2 or "M" in q2):
                            q2 = "M"
                        elif ("k" in q2 or "K" in q2):
                            q2 = "K"
                        else:
                            q2 = "G"
                        q = input("Write the complete name of the Logical volume where you'd like to make the changes: ")
                        os.system("lvextend --size +{}{} {}".format(q1, q2, q))
                        os.system("resize2fs ()".format(q))
    
                    elif "su" in q1:
                        q1 = input("Write the complete name of the Logical volume where you'd like to make the changes: ")
                        q = input("Where is the Logical Volume mounted? : ")
                        q3 = input(
                            "How much space would you like to remove from the Logical volume (numerical value only): ")
                        q3 = int(q3)
                        q2 = input("What is the unit of given space?[M/K/G] : ")
                        if ("m" in q2 or "M" in q2):
                            q2 = "M"
                            q3 = q3 * 1024
                        elif ("k" in q2 or "K" in q2):
                            q2 = "K"
                        else:
                            q2 = "G"
                            q3 = q3 * 1024 * 1024
                        x = sp.getoutput("lvdisplay {}".format(q1))
                        x = x.rsplit(" ")
                        size = float(x[158])
                        x = x[159]
                        if ("m" in x or "M" in x):
                            x = "M"
                            size = size * 1024
                        elif ("k" in x or "K" in x):
                            x = "K"
                        else:
                            x = "G"
                            size = size * 1024 * 1024
                        size = size - q3
                        size = int(size)
                        os.system("umount {}".format(q))
                        os.system("e2fsck -f {}".format(q1))
                        os.system("resize2fs {} {}K".format(q1, size))
                        os.system("lvreduce --size -{}K {}".format(q3, q1))
                        os.system("mount {} {}".format(q1, q))
                else:
                    q = input("Where is the device mounted? : ")
                    q1 = input("How many blocks would like to add to the storage? : ")
                    os.system("xfs_growfs -D {} {}".format(q1, q))
            elif int(o) == 8:
                break
            elif int(o) == 11:
                os.system("tput setaf 1")
                print("Exiting...")
                os.system("tput setaf 7")
                exit()
            else:
                os.system("tput setaf 1")
                print("INVALID OPTION!!!")
                os.system("tput setaf 7")

    else:
        os.system("tput setaf 1")
        print("COMMAND NOT RECOGNIZED!!!")
        os.system("tput setaf 7")
