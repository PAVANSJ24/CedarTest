import numpy as np
import json

data = np.load("event25.npz", allow_pickle=True)
lists = np.ndarray.tolist(data)
json = json.dumps(lists)

print(json)

# print(data.files)
# row = data.files
# np.set_printoptions(threshold=np.inf)
# print(data['root_file'])
# sys.stdout=open("test.txt","w")
# for i in row:
#     print("--------------------------")
#     print(data[i])
# sys.stdout.close()

# import numpy as np
# import h5py
# filename = 'multimuonfile.h5'
# f = h5py.File(filename, 'r')
# np.savetxt('h5file.txt', f['dataset'][...])
# f.close()
