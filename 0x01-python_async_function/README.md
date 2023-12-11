# PYTHON ASYNC FUNCTIONS
In Python, asynchronous programming is achieved using the asyncio module. Asynchronous functions are defined using the async def syntax. 

Asynchronous functions are typically used to perform non-blocking I/O operations, allowing other tasks to run while waiting for I/O to complete. They are commonly used in conjunction with the asyncio event loop.

Example:

    import asyncio

    async def hello_world():
        print("Hello")
        await asyncio.sleep(1)  # Simulate asynchronous I/O operation
        print("World")

    # Run the asynchronous function
    asyncio.run(hello_world())


## Tasks solved in this directory:

### [0-basic_async_syntax.py](https://github.com/JamesRaphaelJRC/alx-backend-python/blob/main/0x01-python_async_function/0-basic_async_syntax.py)
Defines an asynchronous coroutine named `wait_random`  that takes in an integer argument (max_delay, with a default value of 10), waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it (The time delayed).


### [1-concurrent_coroutines.py](https://github.com/JamesRaphaelJRC/alx-backend-python/blob/main/0x01-python_async_function/1-concurrent_coroutines.py)
Imports wait_random from the previous python file above and defines an async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay and spawn wait_random n times with the specified max_delay.

wait_n returns the list of all the delays (float values). The list of the delays should be in ascending order without using sort() because of concurrency.
