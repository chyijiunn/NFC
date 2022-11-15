import hashlib
hs = hashlib.md5(b'ffffffffffffff')#這邊放讀取的 ID 標籤，為一個物件
print(hs)#印出這個物件
print(hs.hexdigest())#物件的 MD5 value