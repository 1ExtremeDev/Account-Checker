"""

AUTHOR: ExtremeDev
INSTAGRAM: @extremedevalt
Date: 15/03/2020

"""

import json
import os
from typing import Set
import keyboard
import sys
import time

from .funcs import *
from .config import *

basic = {
    "autologin": {
        "autologin": False,
        "username": "None",
        "password": "None"
    },
    "tool": {
        "timeout": 1000,
        "refresh": 1000
    }
}

class Config:
    def config_check():
        if os.path.exists('../settings/config.extremedev'):
            config_n = open('../settings/config.extremedev', 'r+', encoding='utf-8')
            config = json.load(config_n)
            config_n.close()
            if 'autologin' in config and 'tool' in config:
                if config['autologin']['username'] is not None and config['autologin']['autologin'] is not None and config['autologin']['password']is not None :
                    if config['tool']['timeout'] is not None  and config['tool']['refresh'] is not None:
                        return config
            else:
                
                return config

        else:
            try:
                os.makedirs('../settings')
            except:
                ...
            try:
                config = open('../settings/config.extremedev', 'a+', encoding='utf-8')
                json.dump(basic, config, indent=4)
                config.close()
                return 'created'
            except:
                print(' Cannot access settings/config.extremedev file. Please contact any admin.')
            return ...
    def GetInfo(arg: str=None):
        if arg is None:
            return Config.config_check()
        else:
            x = Config.config_check()
            if x != ...:
                names = {
                    'autologin': x['autologin']['autologin'],
                    'username': x['autologin']['username'],
                    'password': x['autologin']['password'],
                    'timeout': x['tool']['timeout'],
                    'refresh': x['tool']['refresh']
                }
                if arg not in names:
                    return ... 
                else:
                    return names[arg]
            else:
                return ...
    def jsondump(newvalue):
        try:
            config = open('../settings/config.extremedev', 'w+', encoding='utf-8')
            json.dump(newvalue, config, indent=4)
            config.close()
            return True
        except:
            return False
    def Remove():
        try:
            os.remove('../settings/config.extremedev')
        except:
            return ...
        return ...
class Settings:
    class tool:
        def Timeout(arg=None):
            _config = Config.config_check()
            if type(_config) is dict:
                if type(arg) is int:
                    _config['tool']['timeout'] = arg
                else:
                    return ...
            else:
                return ...
            return Config.jsondump(_config) 
        def refresh(arg=None):
            _config = Config.config_check()
            if type(arg) is int:
                _config['tool']['refresh'] = arg
            else:
                return ...
            return Config.jsondump(_config) 
    class autologin:
        def AutoLogin():
            _config = Config.config_check()
            if _config['autologin']['autologin'] is False:
                _config['autologin']['autologin'] = True
            else:
                _config['autologin']['autologin'] = False
            return Config.jsondump(_config) 
        def Username(arg=None):
            _config = Config.config_check()
            if type(arg) is str:
                _config['autologin']['username'] = arg
            else:
                return ...
            return Config.jsondump(_config) 
        def Password(arg=None):
            _config = Config.config_check()
            if type(arg) is str:
                _config['autologin']['password'] = arg
            else:
                return ... 
            return Config.jsondump(_config) 
    
class Text:
    def menu():
        System.clear()
        System.print_info()
        System.println(' Press the key whose connected with your change name.\n\n [A] AutoLogin\n [U] Username\n [P] Password\n [T] Timeout\n [R] Refresh Rate\n [M] Return to menu')
        System.println('\n > ')
        goto = 0
        while True: 
            try:  
                if keyboard.is_pressed('a'): 
                    goto = 1
                    break
                elif keyboard.is_pressed('u'):
                    goto = 2
                    break
                elif keyboard.is_pressed('p'):
                    goto = 3
                    break
                elif keyboard.is_pressed('t'):
                    goto = 4
                    break
                elif keyboard.is_pressed('r'):
                    goto = 5
                    break
                elif keyboard.is_pressed('m'):
                    goto = 6
                    break
            except Exception as error:
                print('Please message the owner of this application, error: {}'.format(str(error)))
                time.sleep(2)
                sys.exit()  
        sys.stdout.write("\b")
        sys.stdout.flush()
        sys.stdout.write(str(goto))
        sys.stdout.flush()
        if goto == 1:
            Settings.autologin.AutoLogin()
            Text.menu()
        elif goto == 6:
            ...
        else:
            System.println('\n\n Enter the new value: ')
            if goto in (4,5):
                try:
                    new_value = input()
                    new_value = int(new_value.replace(new_value[0], ''))
                except Exception as error:
                    print(error)
                    print('\n Please enter a valid value.')
                    time.sleep(2)
                    System.quit(1)
                if goto == 4:
                    Settings.tool.Timeout(new_value)
                elif goto == 5:
                    Settings.tool.refresh(new_value)
                Text.menu()
            else:
                if goto in (2,3):
                    System.println('\n\n Enter the new value: ')
                    new_value = input()
                    new_value = new_value.replace(new_value[0], '')
                    if goto == 2:
                        Settings.autologin.Username(new_value)
                    elif goto == 3:
                        Settings.autologin.Password(new_value)
                    Text.menu()
                else:
                    System.println('\n Invalid input..')
                    time.sleep(2)
                    Text.menu()
                