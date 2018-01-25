class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   


   def displayEmployee(self):
      print (self.name, self.salary)

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp2.name="Khang"#change name
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %.d2"  %Employee.empCount)
