import re
from openpyxl import Workbook

#packet_number connot repeat, so delete repeat data


f = open("X5A_0326_new.txt", "r",encoding='UTF-8')


lines = f.readlines()
tmp = []
hand_shake_type = []
info = []
start_pkg_num = []
start_pkg_time = []
end_pkg_num = []
end_pkg_time = []


for line in lines:
    #print(line) #Print all information
    tmp = re.split(r'\[', line)

    if(len(tmp)==2):
        info = tmp[0].split()
        hand_shake_type = tmp[1].split()
        if len(info)==10:
            
            if "8883" in info and "SYN]" in hand_shake_type[0]:
                start_pkg_num.append(info[7])
                start_pkg_time.append(info[1])
                
            elif "8883" in info and ("FIN," in hand_shake_type[0] or "RST," in hand_shake_type[0]):
                end_pkg_num.append(info[9])
                end_pkg_time.append(info[1])
                

start_dict = dict(zip(start_pkg_num, start_pkg_time))
print("Start:"+str(start_dict))

print("=======================================")

end_dict = dict(zip(end_pkg_num, end_pkg_time))
print("End:"+str(end_dict))


wb_start = Workbook()
ws_start  = wb_start .active
for start_pkg_num, start_time in start_dict.items():
    ws_start.append([start_pkg_num, start_time])
wb_start.save("output_0329_start.xlsx")


wb_end = Workbook()
ws_end = wb_end.active
for end_pkg_num, end_pkg_time in end_dict.items():
    ws_end.append([end_pkg_num, end_pkg_time])
wb_end.save("output_0329_end.xlsx")


















    

    

        
    









    











