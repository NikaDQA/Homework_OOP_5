from collections.abc import Generator


class Candidate:
  def __init__(self, first_name, last_name, email, tech_stack,
               main_skill, main_skill_grade):
      self.first_name = first_name
      self.last_name = last_name
      self.email = email
      self.tech_stack = tech_stack
      self.main_skill = main_skill
      self.main_skill_grade = main_skill_grade



  @property
  def full_name(self):
      return f'{self.first_name} {self.last_name}'

  @classmethod
  def generate_candidates(cls, file_path):
      candidates = []
      with open(file_path, 'r') as file:
          next(file)
          for line in file:
              data = line.strip().split(',')
              first_name, last_name = data[0].split()
              email = data[1]
              tech_stack = data[2].split('|')
              main_skill = data[3]
              main_skill_grade = data[4]
              candidate = cls(first_name, last_name, email, tech_stack, main_skill, main_skill_grade)
              candidates.append(candidate)
      return candidates


url = 'candidates.csv'
candidates = Candidate.generate_candidates(url)
for candidate in candidates:
    print(candidate.full_name)
    print(candidate.email)
    print(candidate.tech_stack)
    print(candidate.main_skill)
    print(candidate.main_skill_grade)
    print()