my_string = '1h 45m,360s,25m,30m 120s,2h 60s'
total_m = 0
new_my_string = my_string.split(',')
for time in new_my_string:
    for new_time in time.split(' '):
        if "h" in new_time:
            new_time = new_time.replace("h", "")
            new_time = int(new_time)
            total_m = total_m + new_time * 60  
        elif "m" in new_time:
                new_time = new_time.replace("m", "")
                new_time = int(new_time)
                total_m = total_m + new_time
        elif "s" in new_time:
                new_time = new_time.replace("s", "")
                new_time = int(new_time)
                total_m = total_m + new_time // 60

print(total_m)                     
