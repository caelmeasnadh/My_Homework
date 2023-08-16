class Phone:
    phone_number = ''
    _incoming_call = 0

    def set_phone_number(self, number):
        self.phone_number = number

    def _get_number_of_calls(self):
        return self._incoming_call

    def increase_number_of_calls(self):
        self._incoming_call += 1

phone_1 = Phone()
phone_2 = Phone()
phone_3 = Phone()
phone_1.set_phone_number('099999999')
phone_2.set_phone_number('098888888')
phone_3.set_phone_number('097777777')

print('Number of calls :', phone_1._get_number_of_calls())
[phone_1.increase_number_of_calls() in range(15)]
print('Number of calls :', phone_1._get_number_of_calls())
phone_2.increase_number_of_calls()
phone_2.increase_number_of_calls()
phone_2.increase_number_of_calls()
phone_3.increase_number_of_calls()
phone_3.increase_number_of_calls()
print('Number of calls phone_1 :', phone_1._get_number_of_calls())
print('Number of calls phone_2 :', phone_2._get_number_of_calls())
print('Number of calls phone_3:', phone_3._get_number_of_calls())


phones = [phone_1, phone_2, phone_3]
sum_off_calls = 0
for phone in phones:
    sum_off_calls += phone._get_number_of_calls()
print('Number of calls : ', sum_off_calls)
with open("C:/Users/datex/Documents/OOP_Lesson_1.txt.", 'r+') as f:
    f.write(f'Number of calls : {(str(sum_off_calls))}')