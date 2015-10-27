tmp = 1e0
while 1e0 + tmp != 1e0:
    eps = tmp
    tmp /= 2e0
print(eps)

import sys
print(sys.float_info.epsilon)
print(1 + eps)    
