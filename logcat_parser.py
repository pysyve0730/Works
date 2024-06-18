import re

print("選擇顯示相關log(1. LTE network, 2. mms, 3. ims, 4. sms, 5. signal, 6. roaming, 7. volte, 8. crash):")
func_num = int(input())

func_log=[]
match func_num:
        case 1:
            func_log = "LTE network"
        case 2:
            func_log = "mms"
        case 3:
            func_log = "ims"
        case 4:
            func_log = "sms"   
        case 5:
            func_log = "signal"   
        case 6:
            func_log = "roaming"
        case 7:
            func_log = "volte"
        case 8:
            func_log = "crash"
        case _:
            func_log = "Input is wrong!"
            
            
            
print("請輸入查看開始日期(ex:05-09):")
start_date = input()

print("請輸入查看開始時間(ex:14:40):")
start_time = input()


print("請輸入查看結束日期(ex:05-09):")
end_date = input()
print("請輸入查看結束時間(ex:14:40):")
end_time = input()




f = open("logcat_all.txt", "r",encoding='UTF-8')
lines = f.readlines()

file = open("data","w")
tmp = []

def lte_network(line):
    ## Check network(LTE) (supl,mms)
    if("Broadcasting ServiceState" in line):
            file.write(line)
    if("DATA_REGISTRATION_STATE" in line) and ("<" in line):
            file.write(line)
    if("OPERATOR" in line) and ("<" in line):
            file.write(line)
    if("ConnectivityService" in line):
            file.write(line)
    #X5A ping
    if("pingNetwork" in line):
            file.write(line)

def ims(line):
    ## Check IMS (volte sms)
    if("Broadcasting ServiceState" in line):
            file.write(line)
    if("VOICE_REGISTRATION_STATE" in line) and ("<" in line):
            file.write(line)

def roaming(line):
     if(".regState" in line) and ("<" in line):
            file.write(line)
     if("Broadcasting ServiceState" in line):
            file.write(line)
def signal(line):
     if("RIL_REQUEST_GET_CELL_INFO_LIST" in line) and ("<" in line):
            file.write(line)
            
def crash(line): 
    if("crash" in line):
            file.write(line)
    if("tombstoned" in line):
            file.write(line)
    if("Fatal signal" in line):
            file.write(line)
    if("fatal exception" in line):
            file.write(line)

def capture_log(date,time,tmp):

    if(date==tmp[0]) and (time in tmp[1]):
            #LTE
            ## Check LTE (mms)
            if(func_log=="LTE network"):
                lte_network(line)
            #MMS
            if(func_log=="mms"):
                if("destination port" in line) and ("2948" in tmp[10]) or ("processMessagePart:" in line):
                    file.write(line)     
                    #dispatchWapPdu()
                    #WAP_PUSH_DELIVER   
                    
            #IMS
            ## Check IMS (volte sms)
            if(func_log=="ims"):
                ims(line)

            #SMS
            if(func_log=="sms"):
                if("Delivering SMS to:" in line):
                    file.write(line)
            #Volte call
            if(func_log=="volte"):
                if("Telecom" in line):
                    file.write(line)
                if("PhoneServiceManager" in line):
                    file.write(line)
                if("Dialer" in line):
                    file.write(line)
                  
                    
            
 
    if(func_log=="signal"):
       signal(line)
    if(func_log=="roaming"):
        roaming(line)
       
    if(func_log=="crash"):
       crash(line) 



for line in lines:
    tmp = re.split(r' ', line)
    capture_log(start_date,start_time,tmp)
    capture_log(end_date,end_time,tmp)
    
    

    
    
file.close()
