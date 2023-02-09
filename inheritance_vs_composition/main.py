"""
Abstract Base Classes in Python
Inheritance and composition are two major concepts in object-oriented programming that model the relationship between
two classes. They drive the design of an application and determine how the application should evolve as new features are
 added
or requirements change.

Both of them enable code reuse, but they do it in different ways.

Inheritance models what is called an is a relationship. This means that when you have a Derived class that inherits
from a Base class, you created a relationship where Derived is a specialized version of Base.
Let’s say you have a base class Animal and you derive from it to create a Horse class. The inheritance relationship
states that a Horse is an Animal. This means that Horse inherits the interface and implementation of Animal,
and Horse objects can be used to replace Animal objects in the application.

What’s Composition?
Composition is a concept that models a has a relationship. It enables creating complex types by combining objects
of other types. This means that a class Composite can contain an object of another class Component.
This relationship means that a Composite has a Component.

Note: Classes that contain objects of other classes are usually referred to as composites, where classes that are used
to create more complex types are referred to as components.

"""
import hr
import payroll

if __name__ == "__main__":
    print('inheritance vs composition')

    salary_employee = hr.SalaryEmployee(1, 'John Smith', 1500)
    hourly_employee = hr.HourlyEmployee(2, 'Jane Doe', 40, 15)
    commission_employee = hr.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
    payroll_system = payroll.PayrollSystem()
    payroll_system.calculate_payroll([
        salary_employee,
        hourly_employee,
        commission_employee
    ])

    employee = hr.Employee(1, 'Invalid')
    payroll_system.calculate_payroll([employee])