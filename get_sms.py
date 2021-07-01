import os
import serial
from time import sleep


def get_sms():
    fd = serial.Serial('COM14', 115200,timeout = 1, xonxoff=True, dsrdtr = True, interCharTimeout = True)
    fd.write("AT+CMGF=1 \015")    
    fd.write('AT+CMGL="REC UNREAD" \015')
    ans=[[]]
    i=0
    line=''
    while line!=['\r\n', 'OK\r\n'] or i==1:
        fd.write('AT+CMGR='+str(i)+' \015')
        line=fd.readlines()
        ans.append(line)
        i=i+1
    ans.remove(ans[0])
    for i in range(ans.count(['\r\n', 'OK\r\n'])):
        ans.remove(['\r\n', 'OK\r\n'])
    for i in range(len(ans)):
        for q in range(ans[i].count('\r\n')):
            ans[i].remove('\r\n')
        for j in range(len(ans[i])):
            ans[i][j]=ans[i][j].strip('\r\n')
    fd.close()
    print ans
    return ans



def decode_PDU(text):
    result=unicode(text.decode('hex'), 'utf-16-be').encode('utf8')
    return result

