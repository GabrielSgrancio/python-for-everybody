inp = input("Enter score: ")
score = float(inp)
if score > 0.9 or score < 0.0 :
    print("Bad score")

if score >= 0.9:
    grade = "A" 
elif score >=0.8:
    grade = "B"
elif score >=0.7:
    grade = "C"
elif score >=0.6:
    grade = "D" 
elif score <0.6:
    grade = "F"

print(grade)
