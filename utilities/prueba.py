import os
from base64 import b64decode

def main():
    key = os.environ.get('SERVICE_ACCOUNT_KEY')
    print(">>>>>>>>>> key: ", key)
    # with open('path.json', 'w') as json_file:
    valor = b64decode(key).decode()
    print(">>>>>>>>>> valor: ", valor)

if __name__ == '__main__':
    main()