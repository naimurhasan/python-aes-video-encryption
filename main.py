from encryptor import Encryptor

if __name__ == '__main__':
    key = b'\xa2\x8a\x84\xd4\xe6\xb4\x7f\x13\xbc\x01\x04\x83\xf5N\x0bg'
    enc = Encryptor(key)
    enc.encrypt_file('plain_video.mp4')
    # enc.decrypt_file('plain_video.mp4.enc')