# timestamped_print.py
import builtins
import time

# Save the original print function
original_print = builtins.print

def timestamped_print(*args, **kwargs):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # Call the original print function with the timestamp
    original_print(f"{current_time} -", *args, **kwargs)

def enable_timestamped_print():
    builtins.print = timestamped_print

def disable_timestamped_print():
    builtins.print = original_print
