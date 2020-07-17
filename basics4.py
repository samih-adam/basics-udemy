#The dir() function returns all properties and methods of the
# specified object, without the values. This function will return all the properties and methods,
# even built-in properties which are default for all object.

#The sum() function takes an iterable and returns the sum of items in it.
# Iterable item like string, list, dictionary etc. ...
# The sum() function only works with numerical values, trying to use it with non-numeric
# type will result in an error.

#The len() function in Python takes either an array or a string as its parameter
# and determines the number of elements in the given array, or number of characters in
# the given string. In short, it returns how long the passed array or string is.
# .lower() makes everything lowercase
# .count() counts everything inside the list syntax or whatever variable you connect it to

monday_temp = [9.1, 8.8, 7.5]
student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}

mysum = sum(student_grades)
length = len (student_grades)
mean = mysum / length

print (mean)