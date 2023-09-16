# import rsa ,time
# publicKey, privateKey = rsa.newkeys(512) 
# message = "hello geeks"
# encMessage = rsa.encrypt(message.encode(),publicKey)
# print("original string: ", message)
# print("encrypted string: ", encMessage)
# decMessage = rsa.decrypt(encMessage, privateKey).decode()
# print("decrypted string: ", decMessage)
# print(time.perf_counter())

# import time 
# from cryptography.fernet import Fernet
# message = "hello geeks"
# key = Fernet.generate_key()
# fernet = Fernet(key)
# encMessage = fernet.encrypt(message.encode())
# print("original string: ", message)
# print("encrypted string: ", encMessage)
# decMessage = fernet.decrypt(encMessage).decode()
# print("decrypted string: ", decMessage)
# print(time.perf_counter())
