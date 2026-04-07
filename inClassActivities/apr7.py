# Student and Roster classes
class Student:
  def __init__(self, first, last, gpa):
    self.first = first
    self.last = last
    self.gpa = gpa
  def get_last(self):
    return self.last
  def get_gpa(self):
    return self.gpa

class Roster:
  def __init__(self):
    self.roster = []
  def add_student(self, student):
    self.roster.append(student)
  def course_size(self):
    return len(self.roster)
  def get_deans_list(self):
    # return last name of all students on dean's list
    for student in self.roster:
      if (student.get_gpa >= 3.5):
        return
