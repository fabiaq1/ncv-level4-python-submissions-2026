import matplotlib.pyplot as plt

name = ["Thandi", "Sipho", "Lerato"]
marks = [65.0, 95.3, 65.7]

passed = 0
failed = 0
distinction = 0

# Count passes, failures and distinctions
for m in marks:
    if m >= 80:
        distinction += 1
    elif m >= 50:
        passed += 1
    else:
        failed += 1

# Display results
print("Passes:", passed)
print("Failures:", failed)
print("Distinctions:", distinction)

# Draw pie chart
labels = ["Pass", "Fail", "Distinction"]
values = [passed, failed, distinction]

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Student Results")
plt.show()