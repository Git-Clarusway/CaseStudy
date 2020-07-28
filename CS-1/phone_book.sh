#! /bin/bash
sudo echo 'Welcome ' $( who | cut -d' ' -f1 )
who | cut -d' ' -f1 >> AccesslsLog.txt
date >> AccesslsLog.txt
# python3 --version
sudo yum install python3 -y
export PATH1=$PATH
export PATH=$PATH:/usr/bin/python
sudo yum install git -y
export PATH=$PATH:/usr/bin/git
git clone https://github.com/Git-Clarusway/casestudy1.git
cd casestudy1
chmod +x phone_book.py
./phone_book.py             

