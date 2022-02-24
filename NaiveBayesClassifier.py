import math
import random
import sys

age0 = []
gender0 = []
height0 = []
weight0 = []
bodyfat0 = []
diastolic0 = []
systolic0 = []
gripforce0 = []
sitbend0 = []
situp0 = []
broadjump0 = []
performance0 = []
age1 = []
gender1 = []
height1 = []
weight1 = []
bodyfat1 = []
diastolic1 = []
systolic1 = []
gripforce1 = []
sitbend1 = []
situp1 = []
broadjump1 = []
performance1 = []
correct = 0
count= 0

with open(sys.argv[1], "r") as file:
    for l in file:
        currentline = l.split(",")

        performance = float(currentline [11])

        if performance == 0:
            age0.append(float(currentline [0]))
            gender0.append(str(currentline [1]))
            height0.append(float(currentline [2]))
            weight0.append(float(currentline [3]))
            bodyfat0.append(float(currentline [4]))
            diastolic0.append(float(currentline [5]))
            systolic0.append(float(currentline [6]))
            gripforce0.append(float(currentline [7]))
            sitbend0.append(float(currentline [8]))
            situp0.append(float(currentline [9]))
            broadjump0.append(float(currentline [10]))
            performance0.append(int(currentline [11]))
        elif performance == 1:
            age1.append(float(currentline [0]))
            gender1.append(str(currentline [1]))
            height1.append(float(currentline [2]))
            weight1.append(float(currentline [3]))
            bodyfat1.append(float(currentline [4]))
            diastolic1.append(float(currentline [5]))
            systolic1.append(float(currentline [6]))
            gripforce1.append(float(currentline [7]))
            sitbend1.append(float(currentline [8]))
            situp1.append(float(currentline [9]))
            broadjump1.append(float(currentline [10]))
            performance1.append(int(currentline [11]))

#print(gender1)

def mean(values):
    return sum(values)/float(len(values))

def stdev(values):
	avg = mean(values)
	variance = sum([(v-avg)**2 for v in values]) / float(len(values)-1)
	return math.sqrt(variance)

age0mean = mean(age0)
age1mean = mean(age1)

height0mean = mean(height0)
height1mean = mean(height1)

weight0mean = mean(weight0)
weight1mean = mean(weight1)

bodyfat0mean = mean(bodyfat0)
bodyfat1mean = mean(bodyfat1)

diastolic0mean = mean(diastolic0)
diastolic1mean = mean(diastolic1)

systolic0mean = mean(systolic0)
systolic1mean = mean(systolic1)

gripforce0mean = mean(gripforce0)
gripforce1mean = mean(gripforce1)

sitbend0mean = mean(sitbend0)
sitbend1mean = mean(sitbend1)

situp0mean = mean(situp0)
situp1mean = mean(situp1)

broadjump0mean = mean(broadjump0)
broadjump1mean = mean(broadjump1)

age0stdev = stdev(age0)
age1stdev = stdev(age1)

height0stdev = stdev(height0)
height1stdev = stdev(height1)

weight0stdev = stdev(weight0)
weight1stdev = stdev(weight1)

bodyfat0stdev = stdev(bodyfat0)
bodyfat1stdev = stdev(bodyfat1)

diastolic0stdev = stdev(diastolic0)
diastolic1stdev = stdev(diastolic1)

systolic0stdev = stdev(systolic0)
systolic1stdev = stdev(systolic1)

gripforce0stdev = stdev(gripforce0)
gripforce1stdev = stdev(gripforce1)

sitbend0stdev = stdev(sitbend0)
sitbend1stdev = stdev(sitbend1)

situp0stdev = stdev(situp0)
situp1stdev = stdev(situp1)

broadjump0stdev = stdev(broadjump0)
broadjump1stdev = stdev(broadjump1)

def tofloat(gender0, gender1):
	for line in gender0, gender1:
		line = float(line.strip())
    
def gaussian(i, mean, stdev):
	expo = math.exp(-((i-mean)**2 / (2 * stdev**2 )))
	return (1 / (math.sqrt(2 * math.pi) * stdev)) * expo

with open(sys.argv[2], "r") as file:
    for l in file:
        line = l.split(",")

        probage0 = gaussian(float(line[0]), age0mean, age0stdev)
        probage1 = gaussian(float(line[0]), age1mean, age1stdev)

        probheight0 = gaussian(float(line[2]), height0mean, height0stdev)
        probheight1 = gaussian(float(line[2]), height1mean, height1stdev) 

        probweight0 = gaussian(float(line[3]), weight0mean, weight0stdev)
        probweight1 = gaussian(float(line[3]), weight1mean, weight1stdev)

        probbodyfat0 = gaussian(float(line[4]), bodyfat0mean, bodyfat0stdev)
        probbodyfat1 = gaussian(float(line[4]), bodyfat1mean, bodyfat1stdev) 

        probdiastolic0 = gaussian(float(line[5]), diastolic0mean, diastolic0stdev)
        probdiastolic1 = gaussian(float(line[5]), diastolic1mean, diastolic1stdev)

        probsystolic0 = gaussian(float(line[6]), systolic0mean, systolic0stdev) 
        probsystolic1 = gaussian(float(line[6]), systolic1mean, systolic1stdev)  

        probgripforce0 = gaussian(float(line[7]), gripforce0mean, gripforce0stdev) 
        probgripforce1 = gaussian(float(line[7]), gripforce1mean, gripforce1stdev) 

        probsitbend0 = gaussian(float(line[8]), sitbend0mean, sitbend0stdev)  
        probsitbend1 = gaussian(float(line[8]), sitbend1mean, sitbend1stdev)

        probsitup0 = gaussian(float(line[9]), situp0mean, situp0stdev)  
        probsitup1 = gaussian(float(line[9]), situp1mean, situp1stdev) 

        probbroadjump0 = gaussian(float(line[10]), broadjump0mean, broadjump0stdev)
        probbroadjump1 = gaussian(float(line[10]), broadjump1mean, broadjump1stdev)

        prob0 = probage0 * probheight0 * probweight0 * probbodyfat0 * probdiastolic0 * probsystolic0 * probgripforce0 * probsitbend0 * probsitup0 * probbroadjump0
        prob1 = probage1 * probheight1 * probweight1 * probbodyfat1 * probdiastolic1 * probsystolic1 * probgripforce1 * probsitbend1 * probsitup1 * probbroadjump1

        if prob0 > prob1:
            print(0)
            guess = 0
        elif prob1 > prob0:
            print(1)
            guess = 1
        
        #if guess == float(line[11]):
        #    correct += 1
        #count += 1

#print(correct/count)
            
        

#age, gender, height_cm, weight_kg, body_fat_%, diastolic, systolic, grip_force, sit_and_bend_forward_cm, sit_up_count, broad_jump_cm.