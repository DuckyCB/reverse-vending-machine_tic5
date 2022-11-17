# TODO: Get correct id for the actual RVM
def get_rvm():
    return 69

# TODO: Generate id using data
def generate_id():
    # rvm = get_rvm()
    i = 0
    while True:
        i += 1
        yield i
    # return 1
    # return str(rvm) + 'ASDFGH'


class Bottle:
    def __init__(self, barcode, weight, date, user):
        self.rvm = get_rvm()
        self.id = -1
        self.barcode = barcode
        self.weight = weight
        self.date = date
        self.user = user

    def __str__(self):
        return f"""---------------
rvm: {self.rvm} - id: {self.id} 
barcode: {self.barcode}, weight: {self.weight}, date: {self.date}
user: {self.user}"""
