import statistics
import json
def stats():
	temps_lab1 = ()		#sets up lists to analyze
	temps_class1 = ()
	temps_office = ()
	occu_lab1 = ()
	occu_class1 = ()
	occu_office = ()
	

	logfile = open("logfile.txt", "r")		#open logfile to read
	lines = logfile.readlines()			#reads logfile line by line


	for line in lines:
		room = json.loads(line)		#turns text line into dictionary
		if room.keys() == "lab1":		#if-elif loops get the proper keys to index into each line bc three different rooms
			temps_lab1.append(room["lab1"]["temperature"])  
			occu_lab1.append(room["lab1"]["occupancy"])
		elif room.keys() == "class1":
			temps_class1.append(room["class1"]["temperature"])
			occu_class1.append(room["class1"]["occupancy"])
		else:
			temps_office.append(room["office"]["temperature"])
			occu_office.append(room["office"]["occupancy"])
	

	officetemp_mean = mean(temps_office)		#calculates means
	print(officetemp_mean)
	class1temp_mean = mean(temps_class1)
	print(class1temp_mean)
	lab1temp_mean = mean(temps_lab1)
	print(lab1temp_mean)

	office_occu_mean = mean(occu_office)
	print(office_occu_mean)
	lab1_occu_mean = mean(occu_lab1)
	print(lab1_occu_mean)
	class1_occu_mean = mean(occu_class1)
	print(class1_occu_mean)

	officetemp_var = statistics.variance(temps_office) 		#calculates variances
	class1temp_var = statistics.variance(temps_class1)
	lab1temp_var = statistics.variance(temps_lab1)

	office_occu_var = statistics.variance(occu_office)
	lab1_occu_var = statistics.variance(occu_lab1)
	class1_occu_var = statistics.variance(occu_class1)


stats()
