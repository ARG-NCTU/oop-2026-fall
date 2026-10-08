class Member(object):
  tag = 1

  def __init__(self, name):
    self.name = name
    self.borrowed_books = 0
    self.id = Member.tag
    Member.tag += 1

  def get_status(self):
    print(self.name + ':' + str(self.borrowed_books))

class StudentMember(Member):
  def borrow_book(self):
    if self.borrowed_books < 3:
      self.borrowed_books += 1

class FacultyMember(Member):
  def borrow_book(self):
    if self.borrowed_books < 5:
      self.borrowed_books += 1


members_registry = {}
operations = [
    "student Alice",
    "faculty Bob",
    "student Charlie", 
    "borrow 1", "borrow 1", "borrow 1", "borrow 1", "status 1",
    "borrow 2", "borrow 2", "borrow 2", "borrow 2", "borrow 2", "borrow 2", "status 2", 
    "status 3"
]

for op in operations:
  parts = op.split()
  command = parts[0]
  
  if command == "student":
    name = parts[1]
    new_student = StudentMember(name)
    members_registry[new_student.id] = new_student
      
  elif command == "faculty":
    name = parts[1]
    new_faculty = FacultyMember(name)
    members_registry[new_faculty.id] = new_faculty
      
  elif command == "borrow":
    member_id = int(parts[1])
    members_registry[member_id].borrow_book()
      
  elif command == "status":
    member_id = int(parts[1])
    members_registry[member_id].get_status()