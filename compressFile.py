import zlib
import binascii
import pickle
import cv2
import asyncio
import numpy
import os
import json

cap = cv2.VideoCapture(0)
isOpen, frame = cap.read()
print((','.join(str(item) for innerlist in numpy.ndarray.tolist(frame) for item in innerlist)))

# compressed_data = pickle.dumps(dd)
unhexsring = binascii.hexlify(bytes(','.join(str(item) for innerlist in numpy.ndarray.tolist(frame) for item in innerlist)))

compressed_data = zlib.compress(unhexsring)

print(compressed_data)

decompressed = zlib.decompress(compressed_data)
lastframe = binascii.unhexlify(decompressed).decode(encoding='UTF-8')
file = open("copy.txt", "w") 
file.write(lastframe.replace('...', '').replace(']', '')) 
file.close() 
print(lastframe)
