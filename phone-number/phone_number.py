class Phone(object):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def clean_up(self):
        num_list = list(x for x in self.phone_number if x.isdigit())
        ctr_code = num_list[0]
        if ctr_code == '1':
            num_list.remove(ctr_code)
        self.phone_number = ''.join(num_list)
        return self.phone_number

number_1 = Phone('+ 1 965-(986) 896')
print(number_1.clean_up())
