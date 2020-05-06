# get input
score = float(input("Enter Score: "))

# print grade according to condition in the question
if (score < 0) or (score > 1):
    print('error!!')
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else:
    print('F')
