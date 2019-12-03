# if else
# list my_list= [1,2,3,4,5]
scores = [90, 80, 70, 55]
my_score = scores[0]
print(my_score)

scores[0] = 100

for score in scores:
    print(score, end=' ')
print()

for i in range(len(scores)):
    print(scores[i], end=' ')
print()

for (i, score) in enumerate(scores):
    if score == 70:
        break
    print(i, score)

i = 0
while i < len(scores):
    print(scores[i])
    i += 1

