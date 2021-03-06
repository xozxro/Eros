
new [] matrixArr = [array, for, an, array]

## lets say you have this array full of different types of data
new [] mainArr = [123, string, 3532, numbers, 23.234, floats, etcetc, 323.523, 2.734, 902, matrixArr]

# we want to find the relevant data and put it into a new array
# this is very easy with type slicing

# we can list the results in a static string
static str = mainArr : int

# str set to : 123 3532

# then convert it to a list with type conversion
new [] strArr = str;

# strArr: [123, 3532]

# or we can type slice directly into an array
new [] strArr = mainArr : str

new [] floatArr = mainArr : float
new [] intArr = mainArr : int
new [] arrArr = mainArr : []

print floats...
print floatArr

print ints...
print intArr

print strings...
print strArr

print arrays...
print mainArr : []