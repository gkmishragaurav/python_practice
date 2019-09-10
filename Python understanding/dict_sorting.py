fruits = [{'name': 'apple', 'price':25},
          {'name': 'graps', 'price': 2},
          {'name': 'mango', 'price': 20},
          {'name': 'peach', 'price': 12},
          {'name': 'mmm', 'price': 1},
          {'name': 'uert', 'price': 2.3},
          {'name': 'bt5r', 'price': 4.2},
          {'name': 'za', 'price': 3.1},
          {'name': 'zdfg', 'price': 3.1}
          ]
print fruits

fruits.sort(key=lambda fruit: (fruit['price'], fruit['name']))

print fruits