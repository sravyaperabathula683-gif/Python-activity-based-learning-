# Case Study 10: Campus Event Financial Planning
venue = 12000
equipment = 5000
transport = 3000
catering_per_person = 180
certificate_per_person = 20
sponsorship = 10000
registration_fee = 300
planned_participants = 100

values = [venue, equipment, transport, catering_per_person, certificate_per_person,
          sponsorship, registration_fee, planned_participants]
if min(values) < 0:
    print("Invalid event data")
else:
    fixed_cost = venue + equipment + transport
    variable_per_person = catering_per_person + certificate_per_person
    contribution = registration_fee - variable_per_person
    net_fixed = max(0, fixed_cost - sponsorship)
    if contribution <= 0:
        print("Break-even is not possible at this registration fee")
    else:
        minimum_people = (net_fixed + contribution - 1) // contribution
        planned_cost = fixed_cost + planned_participants * variable_per_person
        registration_income = planned_participants * registration_fee
        total_income = registration_income + sponsorship
        balance = total_income - planned_cost
        print("Fixed cost: Rs.", fixed_cost)
        print("Variable cost per participant: Rs.", variable_per_person)
        print("Sponsorship: Rs.", sponsorship)
        print("Minimum break-even registrations:", minimum_people)
        print("Planned participants:", planned_participants)
        print("Estimated total cost: Rs.", planned_cost)
        print("Total income: Rs.", total_income)
        print("Surplus: Rs.", balance)
        if balance < 0:
            print("Shortfall: Rs.", abs(balance))
        else:
            print("Event budget covered")
