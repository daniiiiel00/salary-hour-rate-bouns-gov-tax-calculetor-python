# salary-hour-rate-bouns-gov-tax-calculetor-python
#Employee Salary Calculator
This is a simple Python script to calculate the salary of an employee based on their hourly rate, hours worked, and bonus. The program takes into account overtime pay, federal tax deductions, and displays a detailed summary of the employee's pay including gross salary, tax, bonus, and net pay.

#Features:
Calculates gross salary based on regular hours (up to 40) and overtime hours (above 40 hours).

Applies a federal tax rate based on the gross salary: 15% for salaries less than 5000 ETB, and 25% for salaries above 5000 ETB.

#Includes bonus in the net pay calculation.

#Displays detailed salary breakdown (gross salary, tax, bonus, net pay).

#Requirements:
Python 3.x

#Installation:
Clone the repository or download the Python file:


*git clone https://github.com/yourusername/salary-calculator.git
Navigate to the directory containing the Python file:


cd salary-calculator
Run the Python script:


python salary_calculator.py

#How It Works:
The program prompts the user for:

Employee's name

Hourly rate (ETB)

Hours worked in a week

Bonus amount (ETB)

If the employee works less than or equal to 40 hours, their salary is simply the hourly rate multiplied by hours worked.

If the employee works more than 40 hours, overtime pay is calculated at 1.5 times the hourly rate for hours beyond 40.

The program calculates federal tax based on a progressive tax rate:

15% if gross salary is less than 5000 ETB.

25% if gross salary is 5000 ETB or more.

The final net pay is calculated as:

Net Pay = Gross Salary + Bonus - Federal Tax

The output includes the following:

Employee Name

Gross Salary

Federal Tax Deducted

Bonus Amount

Net Pay

Example Output:
yaml
Copy
Edit
Enter Employee Name: John Doe
Enter Hourly Rate: ETB 200
Enter Hours Worked: 45
Enter Bonus Amount: ETB 1000

Employee Name: John Doe
Gross Salary: ETB9500.00
Federal Tax Deducted: ETB2375.00
Bonus Amount: ETB1000.00
Net Pay: ETB7125.00
Contributing:
Feel free to fork this project, submit issues, or make pull requests for improvements.

#License:
This project is open-source and available .
