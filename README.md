<h1>EROS EXPIREMENTAL PROGRAMMING LANGUAGE</H1>
  <b><h4>  <br>
  <br>

  UPDATE: The readme is a little rough on this one - updating it within the next 24 hrs. Stay tuned.
  <br>  <br>

Eros is a simple syntax programming language built with relatively basic Python code, <br>
allowing for more ease in modification and further expirementation by anyone.<br>
  <br>
  

The language currently uses a static file for ease in testing, but this will obviously be<br> changed to 
  open any file executed through it. To run, simply put your code in test.es and run main.py.<br>
  <br> main.py creates an intepreter space using interpreter.py, which goes through the code and uses<br>
    functions.py to carry out the users commands. The design is currently simple but will evolve soon<br>
    as much more user expandability is added.<br><br>
  Built by zxro (c) 2021<br>
  <a href='https://twitter.com/xozxro'>twitter.com/xozxro</a><br>
<br>
  </b></h4>

<h2>BASIC SYNTAX<br></h2>
<h3>VARIABLES<br></h3>
<br>
 #########################################<br>
 ### <b>STRINGS</b><br>
 <br>
 # DYNAMIC - dynamic strings are string variables that can be modified and type sliced after being set<br>
<br>
  dynamic stringVar = this is a string 123 these are ints 456<br>
  print stringVar<br>
<br>
   # outputs 'this is a string 123 these are ints 456'<br>
<br>
 # STATIC - static strings are string variables that hold retained data from another variable<br>
 # they can be used just like dynamic variables in all other aspects<br>
 <br>
 # they can be used to 'type slice' - extracting only a certain data type out of dynamic strings<br>
 # in the future this will be modifyable, making it easy for developers to define their own types in order<br>
 # to quickly handle and filter large amounts of data through a one line type slice.<br>
<br>
  static intVar = stringVar : int<br>
  print intVar<br>
 <br>
   # outputs 123 456<br>
<br>
 #########################################<br>
 ### <b>ARRAYS</b><br>
<br>
 # arrays can be created via segmenting data by any specified token.<br>
 # place this token in between brackets when creating the array.<br>
 # leave blank to segregate by space or place your data in brackets.<br>
 # eg. new [] arr = [x,y,z]<br>
<br>
  int elem1 = 1<br>
  int elem2 = 2<br>
  dynamic elem3 = string<br>
  new [] arrVar = elem1 elem2 elem3<br>
  print arrVar<br>
<br>
  # outputs [1,2,'string']<br>
 <br>
 # and these will have the same result...<br><br>
  new [,] arrVar = elem1,elem2,elem3<br>
  new [-] arrVar = elem1- elem2-elem3<br>
  new [] arrVar = [elem1, elem2,elem3]<br>
 <br>
 # <b>TYPE CONVERSION</b><br>
 <br>
  static intVar = stringVar : int<br>
  new [] intVar;<br>
<br>
 #########################################<br>
 ### <b>NUMBERS</b><br>
 <br>
 # <b>INT</b>
 <br><br>
  new int newInt = 3<br>
  print newInt<br>
<br>
   # outputs 3<br>
<br>
 # <b>FLOAT</b><br>
<br>
  new float newFloat = 3.2<br>
  print newFloat <br>
<br>
  # outputs 3.2<br>
<br>
 # <b>TYPE CONVERSION</b><br>
 # this will convert typeSliceVar into an integer variable within the programs data array. <br>
 # if typeSliceVar includes multiple numbers spaced apart, this will sum them up and return that value.
<br><br>
  static typeSliceVar = example : int<br>
  int typeSliceVar;<br><br>
 #########################################<br>
 ### <b>BOOLEANS</b>
<br><br>
  new bool isBool = True
<br><br>
 ### <h3><b>PRINT</b></h3><br>
 ### basic string and variable output
<br><br>
  print this is a string<br>
 <br>
   # outputs 'this is a string'
 <br><br>
  dynamic string = 'xyz'<br>
  print string<br>
<br>
   # outputs 'xyz'<br>
<br>
 ### string connetation and type slicing<br>
<br>
  dynamic string = this is a string with some 8324 numbers and some 3.23 floats<br>
  dynamic stringB = and this is another!<br>
  print string ++ string : int ++ stringB<br>
 <br>
   # outputs 'this is a string with some 8324 numbers and some 3.23 floats 8324 and this is another!'<br>
 <br>



