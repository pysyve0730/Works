import re
from openpyxl import Workbook

#packet_number connot repeat, so delete repeat data


f = open("X5A_0401_A010_new.txt", "r",encoding='UTF-8')


lines = f.readlines()
tmp = []
hand_shake_type = []
info = []
start_pkg_num = []
start_pkg_time = []
end_pkg_num = []
end_pkg_time = []


source_pkg_num = 6
source_pkg_time = 1
dist_pkg_num = 8
dist_pkg_time = 1

for line in lines:
    #print(line) #Print all information
    tmp = re.split(r'\[', line)

    if(len(tmp)==2):
        info = tmp[0].split()
        hand_shake_type = tmp[1].split()
        print(info)
        if len(info)==9:
            
            if "8883" in info and "SYN]" in hand_shake_type[0]:
                start_pkg_num.append(info[source_pkg_num])
                start_pkg_time.append(info[source_pkg_time])

            elif "8883" in info and ("FIN," in hand_shake_type[0] or "RST," in hand_shake_type[0]):
                end_pkg_num.append(info[dist_pkg_num])
                end_pkg_time.append(info[dist_pkg_time])

start_dict = dict(zip(start_pkg_num, start_pkg_time))
print("Start has "+str(len(start_dict))+" rows:"+str(start_dict))

print("=======================================")

end_dict = dict(zip(end_pkg_num, end_pkg_time))
print("End has "+str(len(end_dict))+" rows:"+str(end_dict))


wb_start = Workbook()
ws_start  = wb_start.active
for start_pkg_num, start_time in start_dict.items():
    ws_start.append([start_pkg_num, start_time])
wb_start.save("output_0401_start.xlsx")


wb_end = Workbook()
ws_end = wb_end.active
for end_pkg_num, end_pkg_time in end_dict.items():
    ws_end.append([end_pkg_num, end_pkg_time])
wb_end.save("output_0401_end.xlsx")
