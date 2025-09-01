test_dict={"Red" : 1, "Orange": 3, "Yellow" : 1, "Green": 3, "Blue" : 2}
print("The original Dictionary:"+ str (test_dict))
K=2
res=0
for key in test_dict:
    if test_dict[key] == K:
        res =res+1
print("Frequency of 2 is :" + str(res))