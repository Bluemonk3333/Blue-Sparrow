import zipfile
import sys
import random
import pyfiglet
import string
import time

#write help fun
def help_fun():
     print('\n\nSyntax Usages:\t python file_name.py zip_file_name.zip\n\n')
     time.sleep(5)

#write banner fun
def banner_fun():
     banner_text = 'zip fpc'
     print_banner = pyfiglet.figlet_format(banner_text, font='slant', width=200)
     print(print_banner)

#write password list code fun
def password_list_create_fun(_passwords_length):
     numbers = string.digits
     password_store_list = []
     for _ in range(10000):
          passwords = ''.join(random.choice(numbers) for _ in range(_passwords_length))
          password_store_list.append(passwords)
     return password_store_list

#check given file is zip file is otr not
def check_zip_file(_zip_file_name):
     if zipfile.is_zipfile(_zip_file_name):
          return True
     else:
          return False

#write zip file password crack fun
def zip_file_password_crack_fun(_password_list):
     for password in _password_list:
          try:
               with zipfile.ZipFile(_zip_file_name, 'r') as zf:
                    zf.extractall(pwd=bytes(password,'utf-8'))
                    #print colorfull
                    print(f'Found zip file password is:\t{password}')
                    break
          except:
               print(f'password is:\t{password}')
               continue

#main function
if __name__ == '__main__':
     """_summary_
     Tool Name:     Zipfile Password creacker
     Author:   joker
     Date:     10/02/2024
     version:  0.0.2
     """     
     _zip_file_name = sys.argv[1]
     check_value = check_zip_file(_zip_file_name)
     if check_value == True:
          print('zip file is valid')
          time.sleep(3)
          banner_fun()
          help_fun()
          recv_passwords = password_list_create_fun(4)
          zip_file_password_crack_fun(recv_passwords)
     else:
          print('zip file is invalid')

     