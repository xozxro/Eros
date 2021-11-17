Built by zxro (c) 2021

Eros is a simple syntax programming language built with simple Python code, 
allowing for more ease in modification and further expirementation by anyone.

BASIC SYNTAX
##################################################################################
#### VARIABLES
|
| #########################################
| ### STRINGS
| 
| # DYNAMIC - dynamic strings are string variables that can be modified and type sliced after being set
|
  dynamic stringVar = this is a string 123 these are ints 456
  print stringVar
|
|   # outputs 'this is a string 123 these are ints 456'
|
| # STATIC - static strings are string variables that hold retained data from another variable
| 
| # they can be used to 'type slice' dynamic variables - extracting only a certain data type out of dynamic strings
| # in the future this will be modifyable, making it easy for developers to define their own types in order
| # to quickly handle and filter large amounts of data through a one line type slice.
|
  static intVar = stringVar : int
  print intVar
| 
|   # outputs 123 456
|
| #########################################
| ### ARRAYS
|
| # arrays can be created by segmenting data by any specified token.
| # place this token in between brackets when creating the array.
| # leave blank to segregate by space
|
  int elem1 = 1
  int elem2 = 2
  dynamic elem3 = string
  new [] arrVar = elem1 elem2 elem3
  print arrVar
|
|  # outputs [1,2,'string']
| 
| # and this will have the same result...
  new [,] arrVar = elem1,elem2,elem3
| 
| # TYPE CONVERSION
| 
  static intVar = stringVar : int
  new [] intVar;
|
| #########################################
| ### NUMBERS
| 
| # INT
| 
  new int newInt = 3
  print newInt
|
|   # outputs 3
|
| # FLOAT
|
  new float newFloat = 3.2
  print newFloat 
|
|  # outputs 3.2
|

| # TYPE CONVERSION
|
| # this will convert typeSliceVar into an integer variable within the programs data array. 
| # if typeSliceVar includes multiple numbers spaced apart, this will sum them up and return that value.
|
  static typeSliceVar = example : int
  int typeSliceVar;
|
|
##################################################################################
#### PRINT
| ### basic string and variable output
|
  print this is a string
| 
|   # outputs 'this is a string'
| 
  dynamic string = 'xyz'
  print string
|
|   # outputs 'xyz'
|
| ### string connetation and type slicing
|
  dynamic string = this is a string with some 8324 numbers and some 3.23 floats
  dynamic stringB = and this is another!
  print string ++ string : int +_ stringB
| 
|   # outputs 'this is a string with some 8324 numbers and some 3.23 floats 8324 and this is another!'
| 



