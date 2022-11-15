import hashlib
hs = hashlib.md5(b'ffffffffffffff')#這邊放讀取的 ID 標籤
print(hs)
print(hs.hexdigest())