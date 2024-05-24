import re
print("請輸入查看開始日期(ex:05-09):")
start_date = input()

print("請輸入查看開始時間(ex:14:40):")
start_time = input()

print("選擇顯示相關log(1. mms, 2. supl, 3. ims, 4. volte, 5. signal, 6. roaming):")


func_num = int(input())
func_log=[]
match func_num:
        case 1:
            func_log = "mms"
        case 2:
            func_log = "supl"
        case 3:
            func_log = "ims"
        case 4:
            func_log = "volte"   
        case 5:
            func_log = "signal"   
        case 6:
            func_log = "roaming"     
        case _:
            func_log = "Input is wrong!"


# print("請輸入查看結束日期(ex:05-09):")
# end_date = input()
# print("請輸入查看結束時間(ex:14:40):")
# end_date = input()


f = open("logcat", "r",encoding='UTF-8')
lines = f.readlines()

file = open("data","w")
tmp = []


for line in lines:
    tmp = re.split(r' ', line)
    
    if(start_date==tmp[0]) and (start_time in tmp[1]):
            if(func_log=="mms") or (func_log=="supl"):
                ## Check network(LTE) (supl,mms)
                if("Broadcasting ServiceState" in line):
                    file.write(line)
                if("DATA_REGISTRATION_STATE" in line) and ("<" in line):
                    file.write(line)
                if("OPERATOR" in line) and ("<" in line):
                    file.write(line)
                #MMS
                if("destination port" in line) and ("2948" in tmp[10]) or ("processMessagePart:" in line):
                    file.write(line)
                    
                    
                    
            ## Check IMS (volte sms)
            elif(func_log=="ims" or func_log=="volte"):
                if("VOICE_REGISTRATION_STATE" in line) and ("<" in line):
                    file.write(line)
                #SMS
                if("Delivering SMS to:" in line):
                    file.write(line)
            
            
    if(func_log=="signal"):
        if("RIL_REQUEST_GET_CELL_INFO_LIST" in line) and ("<" in line):
            file.write(line)
            

                    
            
            
    
    
    
    
file.close()

 #print(tmp[0]) #date
 #print(tmp[1]) #time
 #print(tmp[2]) #pid
 #print(tmp[3]) #pid
 #print(tmp[6]) log property
 #print(tmp[7]) Classify
