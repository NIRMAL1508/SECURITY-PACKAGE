from cryptography.fernet import Fernet

def audio_encryption(path):
    key=Fernet.generate_key()
    f1=open("enc_key.key",'wb')
    f1.write(key)
    fernet = Fernet(key)
    with open(path,'rb') as file:
        originalaudio=file.read()

    encrypted = fernet.encrypt(originalaudio)

    with open("voice_encryption.wav",'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def audio_decryption(path,key_path):
    f1=open(key_path,'rb')
    key=f1.read()
    fernet = Fernet(key)
    with open(path,'rb') as file1:
        encrypted_audio=file1.read()

    decrypted = fernet.decrypt(encrypted_audio)

    with open("voice_decryption.wav",'wb') as decrypted_file:
        decrypted_file.write(decrypted)



# path = input("\n\nEnter the path to the audio file to be Encrypted: ")
# audio_encryption(path)
# print("\nAudio File is Encrypted")
# audio_decryption("voice_encryption.wav")
# print("\n\nAudio File is decrypted")



