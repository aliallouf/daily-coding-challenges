twelveEquivalent_AM = {"00": "12", "01": "01", "02": "02", "03": "03", "04": "0", "05": "0", "06": "06"
                       ,"07": "07", "08": "08", "09": "09", "10": "10", "11": "11"}
twelveEquivalent_PM = {"12": "12", "13": "01", "14": "02", "15": "03", "16": "04", "17": "05", "18": "06",
                       "19": "07", "20": "08", "21": "09", "22": "10", "23": "11"}
time_String = input()

if time_String.endswith('PM'):
    new_String = time_String.replace("PM", '')
    time_List = new_String.split(":")
    for i, j in twelveEquivalent_PM.items():
        if time_List[0] == j:
            time_List[0] = i
            
if time_String.endswith('AM'):
    new_String = time_String.replace("AM", '')
    time_List = new_String.split(":")
    for i, j in twelveEquivalent_AM.items():
        if time_List[0] == j:
            time_List[0] = i            
            
print(":".join(time_List).strip())            