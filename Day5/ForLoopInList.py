scores = [
    78, 56, 89, 90, 45, 67, 72, 88, 92, 60,
    34, 76, 81, 55, 99, 48, 66, 83, 91, 53,
    40, 70, 85, 62, 79, 100, 58, 64, 87, 95,
    43, 68, 74, 82, 36, 50, 61, 97, 71, 80,
    59, 46, 93, 84, 65, 38, 75, 52, 69, 57
]
sum_module = sum(scores) # to verify
print(sum_module) # to verify

# program sum() function
sum = 0
for score in scores:
    sum += score
print(sum)


topper_module = max(scores) # to verify
print(topper_module)
# program max() function
topper = 0
for score in scores:
    if score > topper:
        topper = score

print(topper)