Numberoftest = 0
score = 0
total = 0
average = 0.0
scorecount = 0 

numberOfTests = int(input("please enter the number of test you want to average:"))

#make this stuff repeat until scoreCount = numberofTests
score = int(input("Please enter a score: "))
scorecount = scorecount + 1
total = total + score


average  = total/scorecount
print("the average is ",average)
