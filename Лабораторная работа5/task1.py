from pprint import pprint
import random

n = random.randint(0,15)

nn = {'dec': n, 'bin': bin(n), 'oct': oct(n), 'hex': hex(n)}

pprint(nn)