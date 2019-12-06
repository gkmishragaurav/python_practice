# In this simplistic example, the code assumes that the list of fields contains only text
# fields. The field name is contained in the list as a string. The strings in the list are also
# the labels used in the form that is returned. For every element in the list, a single field is
# added to the webform. The webform is then returned as a string containing the HTML
# code for the generated webform.
def generate_webform(field_list):
    generated_fields = "\n".join(
    map(
    lambda x: '{0}:<br><input type="text" name="{0}"><br>'.format(x),
    field_list
    ))
    return "<form>{fields}</form>".format(fields=generated_fields)

if __name__ == "__main__":
    fields = ["name", "age", "email", "telephone"]
    print(generate_webform(fields))