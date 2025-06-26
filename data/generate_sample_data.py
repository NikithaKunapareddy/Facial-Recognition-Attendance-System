import pickle
import numpy as np

# Example names and faces (random data for demonstration)
names = ['Nikitha', 'Likhith', 'Udaya']
faces = np.random.randint(0, 255, (3, 7500), dtype=np.uint8)  # 3 faces, 50x50x3 flattened

with open('data/names.pkl', 'wb') as f:
    pickle.dump(names, f)
with open('data/faces_data.pkl', 'wb') as f:
    pickle.dump(faces, f)