foodprefer = {
    'Allister': 'sushi',
    'Whitney': 'beer'
}
print(foodprefer['Whitney'])
print(foodprefer['Allister'])

class Person:
    def __init__(self):
        self.working = {
            'Monday': True,
            'Tuesday': True,
            'Wednesday': False,
            'Thursday': True,
            'Friday': True
        }
Allister = Person()
print(Allister.working['Monday'])
print(Allister.working['Tuesday'])
print(Allister.working['Wednesday'])
