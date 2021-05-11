import re

# Matching Characters
# any five letter string starting with a and ending with s.
pattern = '^a...s$' # one can use any number of '.' to increase the length of pattern.
test_string = 'aasss'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")

# Program to extract numbers from a string
string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'
result = re.findall(pattern, string)
print(result)

# Program to remove all whitespaces
# multiline string
string = 'abc 12\
de 23 \n f45 6'
# matches all whitespace characters
pattern = '\s+'
# empty string
replace = ''
new_string = re.sub(pattern, replace, string)
print(new_string)

# Match	3.14529	-255.34	128 1.9e10 123,340.00
# Skip	720p
pattern = '^-?\d+(,\d+)*(\.\d+(e\d+)?)?$'
string=['3.14529', '-255.34', '128', '1.9e10', '123,340.00', '720p']
print [st for st in string if re.match(pattern, st)]

# regex for ip address.
pattern = '^((?:(?:2[0-5][0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}' \
         '(?:2[0-5][0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9]))$'
string='12.34.65.255'

#Extracting Data From Log Entries
#Skip	W/dalvikvm( 1553): threadid=1: uncaught exception		To be completed
# Skip	E/( 1553): FATAL EXCEPTION: main		To be completed
# Skip	E/( 1553): java.lang.StringIndexOutOfBoundsException		To be completed
# Capture	E/( 1553):   at widget.List.makeView(ListView.java:1727)	makeView ListView.java 1727	To be completed
# Capture	E/( 1553):   at widget.List.fillDown(ListView.java:652)	fillDown ListView.java 652	To be completed
# Capture	E/( 1553):   at widget.List.fillFrom(ListView.java:709)	fillFrom ListView.java 709
