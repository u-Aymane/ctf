bUsername_trial = b"PRITCHARD"
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"

import hashlib

s = ''
keys = [4, 5, 3, 6, 2, 7, 1, 8]
for i in keys:
	s += hashlib.sha256(bUsername_trial).hexdigest()[i]


print(key_part_static1_trial + s)