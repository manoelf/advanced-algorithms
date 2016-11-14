#http://codeforces.com/problemset/problem/722/A


time_format = int(raw_input())
time = raw_input().split(":")

hour = time[0]
minutes = time[1]


if (time_format == 12):
    if (int(hour) > 12):
        if (hour[1] == "0"):
            hour = "10"
        else:   
            hour = "0" + hour[1]
    if (hour == "00"):
        hour = "01"
else:
    if (int(hour) > 23):    
        hour = "0" + hour[1]


if (int(minutes) > 59):
    minutes = "0" + minutes[1]


print hour + ":" + minutes

    
	





