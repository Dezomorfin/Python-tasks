import time
d = ["monday", "tuesday", "wednesday", 
     "thursday", "friday", "saturday", "sunday"]

m = ["", "january", "february", "march", "april", 
         "may", "june", "july", "august", "september", 
         "october", "november", "december"]

t = time.localtime()
print("Today: \n%s %s %s %s %02d:%02d:%02d\n%02d.%02d.%02d." %
	 ( d[t[6]], t[2], m[t[1]], t[0], t[3], 
       t[4], t[5], t[2], t[1], t[0]))