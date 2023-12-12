# PYTHON ASYNC COMPREHENSION
`PEP 492` and `PEP 525` introduce support for native coroutines and asynchronous generators using async / await syntax. This PEP proposes to add asynchronous versions of list, set, dict comprehensions and generator expressions.

Hence, the tasks defined in this directory implements these comprehensions and generator expression on python asynchronous functions


## HOW TO USE
Clone this repository to your local machine.

    git clone https://github.com/JamesRaphaelJRC/alx-backend-python/0x02-python_async_comprehension.git

    cd 0x02-python_async_comprehension

Move your desired test module to the current working directory
Example:

    mv tests/0-main.py .


## DESCRIPTION OF TASKS COVERED IN THIS DIRECTORY

### [0-async_generator.py](https://github.com/JamesRaphaelJRC/alx-backend-python/blob/main/0x02-python_async_comprehension/0-async_generator.py)
Defines a coroutine called `async_generator` that takes no arguments.

The coroutine loops 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10.

### [1-async_comprehension.py](https://github.com/JamesRaphaelJRC/alx-backend-python/blob/main/0x02-python_async_comprehension/1-async_comprehension.py)
Imports `async_generator` from the previous task and then defines a coroutine called `async_comprehension` that takes no arguments.

The coroutine collects 10 random numbers using an async comprehensing over `async_generator`, then return the 10 random numbers.

### [2-measure_time.py](https://github.com/JamesRaphaelJRC/alx-backend-python/blob/main/0x02-python_async_comprehension/2-measure_runtime.py)
Imports `async_comprehension` from the previous file and defines a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather.`

`measure_runtime` measures the total runtime and return it.
