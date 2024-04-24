class Person:
  def __init__(self, name, money, hours, meals):
    self.name = name
    self.money = money
    self.mood = self.sleep(hours)
    self.healthRate = self.eat(meals)

  def sleep(self, hours):
    if hours == 7:
      return "happy"
    elif hours < 7:
      return "tired"
    elif hours > 7:
      return "Lazy"
    
  def eat(meals):
    if meals == 3:
      return "100%"
    elif meals == 2:
      return "75%"
    elif meals == 1:
      return "50%"
    
  def buy(self, items):
    if self.money > 10:
      self.money -= items*10
    else:
      print("you dont have enough money")

class Employee (Person):
  def __init__(self,  name, money, hours, meals, id , car, email, salary, distanceToWork):
    self.id = id
    self.car = car
    self.email = email
    self.salary = salary
    self.distanceToWork = distanceToWork
    Person.__init__(self, name, money, hours, meals)

  def work(self, hours):
    if hours == 8:
      return "happy"
    elif hours > 8:
      return "tired"
    elif hours < 8:
      return "Lazy"

  def drive(self):
    print(f"{self.name} drive")

  def refuel(self):
    print(f"{self.name} refuel")

  def send_mail(self):
    print(f"{self.name} send_mail")


class Office:
  def __init__(self, name, employees):
    self.name = name
    self.employees = employees
  
  def get_all_employees(self):
    return self.employees

  def get_employee(self, empId):
    for employee in self.employees:
      if employee == empId:
        return employee

  def hire(self, Employee):
    print(f"hire that {Employee.name}")

  def fire(self,empId):
    for employee in self.employees:
      if employee == empId:
        print(f"fire that {employee}")

  def calculate_lateness(self):
    pass

  def deduct(self, empId, deduction):
    for employee in self.employees:
      if employee == empId:
        employee.salary -= deduction

  def reward(self, empId, reward):
    for employee in self.employees:
      if employee == empId:
        employee.salary += reward
  


class Car:
  def __init__(self, name, fuelRate, velocity):
    self.name = name
    self.fuelRate = fuelRate
    self.velocity = velocity

  def run(self):
    pass

  def stop(self):
    pass