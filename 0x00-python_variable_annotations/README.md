# Python Variable Anotation

Variable annotations in Python are a way to provide type hints for variables. They were introduced in Python 3.6 as part of PEP 526. Variable annotations allow you to associate a type with a variable, giving tools like linters, static analyzers, and type checkers information about the expected type of a variable.


## How to use/run test modules
Clone and move test modules to the `0x00-python_variable_annotations` directory

    git clone https://github.com/JamesRaphaelJRC/alx-backend-python/0x00-python_variable_annotations.git
    cd 0x00-python_variable_annotations
    mv tests/* .

Run any of the test module in this format `./<test_module>.py`.
Example

    ./0-main.py



# Description for each module

### [0-add.py](https://github.com/JamesRaphaelJRC/alx-backend-python/blob/main/0x00-python_variable_annotations/0-add.py)
Defines a type-annotated function `add` that takes a float `a` and a float `b` as arguments and returns their sum as a float. 

### [1-concat.py](https://github.com/JamesRaphaelJRC/alx-backend-python/blob/main/0x00-python_variable_annotations/1-concat.py)
Defines a type-annotated function `concat` that takes a string `str1` and a string `str2` as arguments and returns a concatenated string

### [2-floor.py](ttps://github.com/JamesRaphaelJRC/alx-backend-python/blob/main/0x00-python_variable_annotations/2-floor.py)
Writes a type-annotated function floor which takes a float `n` as argument and returns the floor of the float.

### [3-to_str.py](ttps://github.com/JamesRaphaelJRC/alx-backend-python/blob/main/0x00-python_variable_annotations/3-to_str.py)
Takes a float `n` as argument and returns the string representation of the float.

### [4-define_variables.py](ttps://github.com/JamesRaphaelJRC/alx-backend-python/blob/main/0x00-python_variable_annotations/4-define_variables.py)
Defines and annotate the following variables with the specified values:

`a`, an integer with a value of 1
`pi`, a float with a value of 3.14
`i_understand_annotations`, a boolean with a value of True
`school`, a string with a value of “Holberton”

### [5-sum_list.py](ttps://github.com/JamesRaphaelJRC/alx-backend-python/blob/main/0x00-python_variable_annotations/5-sum_list.py)
Defines a type-annotated function `sum_list` which takes a list `input_list` of floats as argument and returns their sum as a float.

### [6-sum_mixed_list.py](ttps://github.com/JamesRaphaelJRC/alx-backend-python/blob/main/0x00-python_variable_annotations/6-sum_mixed_list.py)
Defines a type-annotated function `sum_mixed_list` which takes a list `mxd_lst` of integers and floats and returns their sum as a float.

### [7-to_kv.py](ttps://github.com/JamesRaphaelJRC/alx-backend-python/blob/main/0x00-python_variable_annotations/7-to_kv.py)
Defines a type-annotated function `to_kv that` takes a string `k` and an int OR float `v` as arguments and returns a tuple. The first element of the tuple is the string `k`. The second element is the square of the int/float `v` and should be annotated as a float.

### [8-make_multiplier.py](ttps://github.com/JamesRaphaelJRC/alx-backend-python/blob/main/0x00-python_variable_annotations/8-make_multiplier.py)
Defines a type-annotated function `make_multiplier` that takes a float `multiplier` as argument and returns a function that multiplies a float by `multiplier`.

### [9-element_length.py](ttps://github.com/JamesRaphaelJRC/alx-backend-python/blob/main/0x00-python_variable_annotations/9-element_length.py)
Annotates the below function’s parameters and return values with the appropriate types

    def element_length(lst):
    return [(i, len(i)) for i in lst]