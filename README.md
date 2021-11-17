Built by zxro (c) 2021<br>
<br><br>
Eros is a simple syntax programming language built with simple Python code, <br>
allowing for more ease in modification and further expirementation by anyone.<br><br>

BASIC SYNTAX<br>
##################################################################################<br>
#### VARIABLES<br>
|<br>
| #########################################<br>
| ### STRINGS<br>
| <br>
| # DYNAMIC - dynamic strings are string variables that can be modified and type sliced after being set<br>
|<br>
  dynamic stringVar = this is a string 123 these are ints 456<br>
  print stringVar<br>
|<br>
|   # outputs 'this is a string 123 these are ints 456'<br>
|<br>
| # STATIC - static strings are string variables that hold retained data from another variable<br>
| # they can be used just like dynamic variables in all other aspects<br>
| <br>
| # they can be used to 'type slice' - extracting only a certain data type out of dynamic strings<br>
| # in the future this will be modifyable, making it easy for developers to define their own types in order<br>
| # to quickly handle and filter large amounts of data through a one line type slice.<br>
|<br>
  static intVar = stringVar : int<br>
  print intVar<br>
| <br>
|   # outputs 123 456<br>
|<br>
| #########################################<br>
| ### ARRAYS<br>
|<br>
| # arrays can be created by segmenting data by any specified token.<br>
| # place this token in between brackets when creating the array.<br>
| # leave blank to segregate by space<br>
|<br>
  int elem1 = 1<br>
  int elem2 = 2<br>
  dynamic elem3 = string<br>
  new [] arrVar = elem1 elem2 elem3<br>
  print arrVar<br>
|<br>
|  # outputs [1,2,'string']<br>
| <br>
| # and this will have the same result...<br>
  new [,] arrVar = elem1,elem2,elem3<br>
| <br>
| # TYPE CONVERSION<br>
| <br>
  static intVar = stringVar : int<br>
  new [] intVar;<br>
|<br>
| #########################################<br>
| ### NUMBERS<br>
| <br>
| # INT<br>
| <br>
  new int newInt = 3<br>
  print newInt<br>
|<br>
|   # outputs 3<br>
|<br>
| # FLOAT<br>
|<br>
  new float newFloat = 3.2<br>
  print newFloat <br>
|<br>
|  # outputs 3.2<br>
|<br>
| # TYPE CONVERSION<br>
|<br>
| # this will convert typeSliceVar into an integer variable within the programs data array. <br>
| # if typeSliceVar includes multiple numbers spaced apart, this will sum them up and return that value.<br>
|<br>
  static typeSliceVar = example : int<br>
  int typeSliceVar;<br>
|<br>
|<br>
##################################################################################<br>
#### PRINT<br>
| ### basic string and variable output<br>
|<br>
  print this is a string<br>
| <br>
|   # outputs 'this is a string'<br>
| <br>
  dynamic string = 'xyz'<br>
  print string<br>
|<br>
|   # outputs 'xyz'<br>
|<br>
| ### string connetation and type slicing<br>
|<br>
  dynamic string = this is a string with some 8324 numbers and some 3.23 floats<br>
  dynamic stringB = and this is another!<br>
  print string ++ string : int ++ stringB<br>
| <br>
|   # outputs 'this is a string with some 8324 numbers and some 3.23 floats 8324 and this is another!'<br>
| <br>



