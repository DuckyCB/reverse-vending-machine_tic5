
def get_rvm():
  return 69

def generate_id(barcode, weight, date, user):
        rvm = get_rvm()
        return str(rvm) + 'ASDFGH'

class Bottle:
  def __init__(self, barcode, weight, date, user):
    self.rvm = get_rvm()
    self.id = generate_id(barcode, weight, date, user)
    self.barcode = barcode
    self.weight = weight
    self.date = date
    self.user = user
  
  def __str__(self):
    return f"""
        rvm: {self.rvm} - id: {self.id} 
        barcode: {self.barcode}, weight: {self.weight}, date: {self.date}
        user: {self.user}"""
