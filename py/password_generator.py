# Imports
import random
import string

# Content
print("".join(random.choices(string.ascii_letters + string.digits, k=6)))
