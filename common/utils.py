from datetime import datetime
import random

def generate_random():
    return '{0:%Y%m%d%H%M%S%f}'.format(datetime.now()) + ''.join([str(random.randint(1, 10)) for i in range(5)])


