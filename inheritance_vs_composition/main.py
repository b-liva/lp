"""
Implementation Inheritance vs Interface Inheritance
When you derive one class from another, the derived class inherits both:

The base class interface: The derived class inherits all the methods, properties, and attributes of the base class.

The base class implementation: The derived class inherits the code that implements the class interface.

Most of the time, you’ll want to inherit the implementation of a class, but you will want to implement multiple
interfaces, so your objects can be used in different situations.

In Python, you don’t have to explicitly declare an interface. Any object that implements the desired interface can be
 used in place of another object. This is known as duck typing. Duck typing is usually explained as “if it behaves
 like a duck, then it’s a duck.”

 Since you don’t have to derive from a specific class for your objects to be reusable by the program, you may be
  asking why you should use inheritance instead of just implementing the desired interface. The following rules
   may help you:

Use inheritance to reuse an implementation: Your derived classes should leverage most of their base class
implementation. They must also model an is a relationship. A Customer class might also have an id and a name,
but a Customer is not an Employee, so you should not use inheritance.

Implement an interface to be reused: When you want your class to be reused by a specific part of your application,
 you implement the required interface in your class, but you don’t need to provide a base class,
 or inherit from another class.
"""
import hr
import payroll
import disgruntled

if __name__ == "__main__":
    print('inheritance vs composition')

    salary_employee = hr.SalaryEmployee(1, 'John Smith', 1500)
    hourly_employee = hr.HourlyEmployee(2, 'Jane Doe', 40, 15)
    commission_employee = hr.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
    disgruntled_employee = disgruntled.DisgruntledEmployee(20000, 'Anonymous')
    payroll_system = payroll.PayrollSystem()
    payroll_system.calculate_payroll([
        salary_employee,
        hourly_employee,
        commission_employee,
        disgruntled_employee
    ])
