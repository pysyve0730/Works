import re
from openpyxl import Workbook

# 初始化字典來儲存數據
start_dict = {}
end_dict = {}

# 定義封包數字和時間的位置
source_pkg_num = 6
source_pkg_time = 1
dist_pkg_num = 8
dist_pkg_time = 1

# 使用 with open 確保檔案會自動關閉
with open("X5A_0401_A010_new.txt", "r", encoding='UTF-8') as f:
    for line in f:
        tmp = re.split(r'\[', line.strip())  # 移除換行符號

        if len(tmp) == 2:
            info = tmp[0].split()
            hand_shake_type = tmp[1].split()

            if len(info) >= 9:  # 確保 info 長度足夠
                packet_number = info[source_pkg_num] if "SYN]" in hand_shake_type[0] else info[dist_pkg_num]
                packet_time = info[source_pkg_time] if "SYN]" in hand_shake_type[0] else info[dist_pkg_time]

                if "8883" in info:
                    if "SYN]" in hand_shake_type[0]:  # 判斷是 SYN 封包
                        start_dict.setdefault(packet_number, packet_time)
                    elif "FIN," in hand_shake_type[0] or "RST," in hand_shake_type[0]:  # 判斷是 FIN 或 RST
                        end_dict.setdefault(packet_number, packet_time)

# 輸出結果
print(f"Start has {len(start_dict)} rows: {start_dict}")
print("=======================================")
print(f"End has {len(end_dict)} rows: {end_dict}")

# 儲存到 Excel，不包含標題列
def save_to_excel(data, filename):
    wb = Workbook()
    ws = wb.active
    for packet_num, packet_time in data.items():
        ws.append([packet_num, packet_time])  # 不寫標題列
    wb.save(filename)

save_to_excel(start_dict, "output_0401_start_revise.xlsx")
save_to_excel(end_dict, "output_0401_end_revise.xlsx")
