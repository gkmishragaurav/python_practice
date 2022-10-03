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
    },
  {
    "items":
      {
        "item":
          [
            {
              "id": "0001",
              "type": "donut",
              "name": "Cake",
              "ppu": 0.55,
              "batters":
                {
                  "batter":
                    [
                      {"id": "1001", "type": "Regular"},
                      {"id": "1002", "type": "Chocolate"},
                      {"id": "1003", "type": "Blueberry"},
                      {"id": "1004", "type": "Devil's Food"}
                    ]
                },
              "topping":
                [
                  {"id": "5001", "type": "None"},
                  {"id": "5002", "type": "Glazed"},
                  {"id": "5005", "type": "Sugar"},
                  {"id": "5007", "type": "Powdered Sugar"},
                  {"id": "5006", "type": "Chocolate with Sprinkles"},
                  {"id": "5003", "type": "Chocolate"},
                  {"id": "5004", "type": "Maple"}
                ]
            }
          ]
      }
  }
]

def walk_dict(d, k, v):
  for key,value in d.iteritems():
    if isinstance(value, dict):
      k.append(key)
      walk_dict(d[key], k, v)
    elif isinstance(value, list):
      k.append(key)
      walk_list(value, k, v)
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
