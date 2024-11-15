def process_salaries(employee_records):
  
    # Dictionary to store total and average salary per department
    dept_data = {}

    for employee in employee_records:
        dept = employee.get('department', 'Unknown') 
        salary = employee.get('salary', 0)

        if dept not in dept_data:
            dept_data[dept] = {'total_salary': 0, 'employee_count': 0}

        dept_data[dept]['total_salary'] += salary
        dept_data[dept]['employee_count'] += 1

    # Calculate average salary for each department
    result = {}
    for dept, data in dept_data.items():
        total_salary = data['total_salary']
        emp_count = data['employee_count']
        avg_salary = total_salary / emp_count if emp_count > 0 else 0
        result[dept] = {'total_salary': total_salary, 'average_salary': avg_salary}

    return result

# Example for understanding
employees = [
    {'name': 'Alice', 'department': 'HR', 'salary': 5000},
    {'name': 'Bob', 'department': 'IT', 'salary': 7000},
    {'name': 'Charlie', 'department': 'HR', 'salary': 5500},
    {'name': 'David', 'department': 'IT', 'salary': 8000},
    {'name': 'Eve', 'department': 'Finance', 'salary': 4500}
]
print(process_salaries(employees))
