# problem statement:
# Given a variable input- could be either a dict or a list of dict
# we need to print all keys as list and all values as another list.

l = [{
        'plan_code': 'b',
        'quantity': '1',
        'account': {
            'account_code': 'b',
            'username': 'jdoe',
            'email': 'jdoe@domain.com',
            'first_name': 'b',
            'last_name': 'b',
            'company_name': 'Company, LLC.',
            'billing_info': {
                'first_name': 'b',
                'last_name': 'b',
                'address1': '123 Test St',
                'city': 'San Francisco',
                'state': 'CA',
                'country': 'US',
                'zip': '94105',
                'credit_card': {
                    'number': '1',
                    'year': '2018',
                    'month': '12',
                    'verification_value': '123',
                },
            },
        },
    }]

def walk_dict(d, k, v):
  for key,value in d.iteritems():
    if isinstance(value, dict):
      k.append(key)
      walk_dict(d[key], k, v)
    else:
      k.append(key)
      v.append(value)

def walk_list(lst, k,v):
  for item in lst:
    if isinstance(item, dict):
      walk_dict(item, k, v)

key = []
value = []

if isinstance(l, list):
  walk_list(l, key, value)
elif isinstance(l, dict):
  walk_dict(l,key,value)
print("key={0},\n value={1}".format(key, value))
