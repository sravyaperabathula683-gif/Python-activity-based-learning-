# Case Study 1: University Scholarship Allocation
aggregate_min = 80
subject_min = 70
attendance_min = 75
income_max = 250000

applicants = [
    ["Asha", 88, [82, 85, 91], 90, 180000],
    ["Bharat", 79, [80, 76, 84], 92, 150000],
    ["Charan", 91, [88, 69, 95], 86, 120000],
    ["Divya", 91, [90, 92, 89], 86, 200000],
]

eligible = []
rejected = []

for applicant in applicants:
    name, aggregate, subjects, attendance, income = applicant
    reasons = []
    if aggregate < aggregate_min:
        reasons.append("aggregate below minimum")
    for mark in subjects:
        if mark < subject_min:
            reasons.append("subject mark below minimum")
            break
    if attendance < attendance_min:
        reasons.append("attendance below minimum")
    if income > income_max:
        reasons.append("income above limit")
    if not reasons:
        eligible.append(applicant)
    else:
        rejected.append([name, reasons])

eligible.sort(key=lambda item: (item[1], item[3]), reverse=True)
print("ELIGIBLE SCHOLARSHIP APPLICANTS")
for rank, applicant in enumerate(eligible, start=1):
    print(rank, applicant[0], "Aggregate:", applicant[1], "Attendance:", applicant[3])
print("\nNOT ELIGIBLE")
for item in rejected:
    print(item[0], "-", ", ".join(item[1]))
