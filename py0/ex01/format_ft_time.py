import time
from datetime import datetime

seconds = time.time()
now = datetime.now()

seconds_full = f"{seconds:,.4f}"
seconds_scientific = f"{seconds:.2e}"
unix_start = "January 1, 1970"

print(
    "Seconds since",
    unix_start, ":",
    seconds_full, "or",
    seconds_scientific, "in scientific notation")

print(now.strftime("%b %d %Y"))
