from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'], port=9042)

session = cluster.connect('employee')

# read data simple
# print("reading data...")

# rows = session.execute("SELECT * FROM employee_details")

# for emp in rows:
#     print(emp.name, "from", emp.city, "earns $", emp.salary)

# ------------------------------------------------------------
# read performant
# prepared_statement = session.prepare(
#     "SELECT * FROM employee_details WHERE emp_id=?")

# employees_to_lookup = [1, 2]

# for employee_id in employees_to_lookup:
#     employee = session.execute(prepared_statement, [employee_id]).one()
#     print(employee)

# ------------------------------------------------------------
# write sync
# session.execute(
#     "INSERT INTO employee_details(emp_id, name, city, salary) VALUES(3, 'Trevor', 'Cochin', 80)"
# )
# print("Inserted successfully")

# ------------------------------------------------------------
# write async
session.execute_async(
    "INSERT INTO employee_details(emp_id, name, city, salary) VALUES(4, 'Sam', 'Seattle', 125)"
)
print("Inserted successfully")
