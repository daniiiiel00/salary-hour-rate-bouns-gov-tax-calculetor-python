
def calculate_salary():
 
    employee_name = input("Enter Employee Name: ")
    hourly_rate = float(input("Enter Hourly Rate: ETB"))
    hours_worked = float(input("Enter Hours Worked: "))
    bonus = float(input("Enter Bonus Amount: ETB"))

 
    if hours_worked <= 40:
        gross_salary = hourly_rate * hours_worked
    else:
        regular_pay = hourly_rate * 40
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (hourly_rate * 1.5)
        gross_salary = regular_pay + overtime_pay

 
    federal_tax_rate = 0.15 if gross_salary < 5000 else 0.25
    

    federal_tax = gross_salary * federal_tax_rate
    

 
    total_deductions = federal_tax
    net_pay = gross_salary + bonus - total_deductions

  
    print(f"\nEmployee Name: {employee_name}")
    print(f"Gross Salary: ETB{gross_salary:.2f}")
    print(f"Federal Tax Deducted: ETB{federal_tax:.2f}")
    print(f"Bonus Amount: ETB{bonus:.2f}")
    print(f"Net Pay: ETB{net_pay:.2f}")

 
calculate_salary()
