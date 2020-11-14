# pip install cryptography
from cryptography.fernet import Fernet 
import time
import click

print(r"""
+---------------------------+
| UNIP | APS - Criptografia |
| Yuri Almeida  - F224EA7   |
| Julio Perozzi - F12IDA4   |
+---------------------------+
                """)
#Encriptação
if click.confirm('Voce deseja encriptar a mensagem?', default=True):
        msg_argv = input("Digite sua mensagem: ")
        key = Fernet.generate_key()  # geração da chave_secreta!
        print(type(key))
        print(b'sua chave secreta:',key)  # imprime chave_secreta!
        time.sleep(2) #aguarda 2s
        print("Aguarde estamos encriptando...")
        time.sleep(2) #aguarda 2s
        encrypt_msg = Fernet(key) #valor da chave_secreta é atribuído a uma variável->encrypt_msg
        encrypted_msg = encrypt_msg.encrypt(msg_argv.encode()) # encripta mensagem do usuario!
        print("sua string: ",encrypted_msg) #imprime string//texto_encriptado!

#Decriptação
if click.confirm('Voce deseja decriptar sua string?', default=True):
        msg_argv2 = input("Sua string: ") # entrada da string//texto_encriptado!
        time.sleep(1.25) #aguarda 1.25s
        secret = input("Sua chave secreta: ") # entrada da chave secreta!
        print(type(secret))
        print(secret) 
        print("[!]decriptando a sua mensagem secreta..[!]")
        time.sleep(2) #aguarda 2s
        print("[+]mensagem decriptada com sucesso[+]")
        time.sleep(2.25) #aguarda 2.25s
        decrypt_msg = Fernet(secret) #valor chave_secrete é atribuído a uma variável->decrypt_msg
        texto_decodado = decrypt_msg.decrypt(bytes(msg_argv2, 'utf-8')) #decriptação com chave_secreta!
        print(texto_decodado) #imprime texto_simples!
