my_dictionary = {}
print(type(my_dictionary))
my_dictionary['gigE0'] = 'Link to ISP'
my_dictionary['gigE1'] = 'Link to Core1'
my_dictionary['gigE2'] = 'Link to Core2'
my_dictionary['gigE3'] = 'iBGP to RTR2'
print(my_dictionary['gigE0'])
my_list = [3, 2, 1]
my_dict2 = {}
my_dict2['thisisakey'] = 'thisisavalue'
my_dictionary['nested_list'] = my_list
my_dictionary['nested_dict'] = my_dict2
print(my_dictionary)
print(my_dictionary['nested_dict']['thisisakey'])
