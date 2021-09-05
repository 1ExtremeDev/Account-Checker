import threading
from core.checkers.Checker import Start as Checker
from core.customthread import ExtremeDev
from core.funcs import System, Load, Others
from core.config import *
import random
import os
import time
import sys
import keyboard
from threading import Thread
from core.config_handler import Text
stocking = {
    "files": {
        "lines": [],
        "proxies": [],
        'bad-combos': [],
        'bad-proxies': []
    },
    'values': {}
}


module_n = {
    "_byname": {
        "Checker": Checker
    }
}

for each in ['good', 'bad', 'custom', 'checked', 'cpm', 'cpm1', 'retries', 'errors']: stocking['values'][each] = 0
    
class Menu:
    def loading():
        for each in stocking['values']:
            stocking['values'][each] = 0
        System.clear()
        System.print_info()
        System.println('\n\n Welcome, where do you want to go?\n\n')
        for (number, name)in {'1': 'Checker', '2': 'Settings', '3': 'Quit'}.items():
            System.println(' [{}] [{}]\n'.format(number, name))
        sys.stdout.write(' > ')
        sys.stdout.flush()
        goto = 0
        while True: 
            try:  
                if keyboard.is_pressed('1'): 
                    goto = 1
                    break
                elif keyboard.is_pressed('2'):
                    goto = 2
                    break
                elif keyboard.is_pressed('3'):
                    goto = 3
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
            Menu.Start()
        elif goto == 2:
            Menu.Settings()
        elif goto == 3:
            System.quit()
    def Start():
        System.clear()
        System.print_info()
        System.println('\n')
        combos = Load.combos()
        if type(combos) is list:
            stocking['files']['lines'] = combos[0]
            stocking['files']['bad-combos'] = combos[1]
            System.println('\n Loaded {} valid line(s) and {} bad line(s).'.format(str(len(stocking['files']['lines'])), str(len(stocking['files']['bad-combos']))))
            time.sleep(1)
        else:
            System.println('\n Re-trying..')
            time.sleep(2)
            Menu.loading()
        System.clear()
        System.print_info()
        System.println('\n')
        proxies = Load.proxies()
        if type(proxies) is list:
            stocking['files']['proxies'] = proxies[0]
            stocking['files']['bad-proxies'] = proxies[1]
            System.println('\n Loaded {} valid proxy(s) and {} bad line(s).'.format(str(len(stocking['files']['proxies'])), str(len(stocking['files']['bad-proxies']))))
        else:
            System.println('\n Re-trying..')
            time.sleep(2)
            Menu.loading()
        time.sleep(2)
        System.clear()
        System.print_info()
        System.clear()
        System.print_info()
        threads = Others.get_threads()
        input('\n Press ENTER to start.')
        Screen.show()
        while True:
            if threading.active_count() < threads:
                if len(stocking['files']['lines']) != 0:
                    ExtremeDev.Threading(goto=module, argumente=('Checker',)).start()
                else:
                    break
        Screen.show()
        System.println('\n')
        Information.print_half('Checked everything.')
        Information.print_half('Press ENTER to return to the menu.')
        input()
        Menu.loading()


    def Settings():
        Text.menu()
        Menu.loading()


class Screen:
    def show():
        stocking['values']['cpm2'] = stocking['values']['cpm1'] * 60
        stocking['values']['cpm1'] = 0
        System.clear()

        System.print_info()
        System.title('Regrix | Valid: {}/{} | Custom: {}'.format(str(stocking['values']['good']), str(len(stocking['files']['lines'])), str(stocking['values']['custom'])))
        System.println('\n\n\n')
        if keyboard.is_pressed('q'):
            print('TODO') 
        Information.print_half('Total Threads: [{}]'.format(str(threading.active_count())))
        Information.print_half('Total Line(s): [{}]'.format(str(len(stocking['files']['lines']))))
        if len(stocking['files']['proxies']) == 0:
            Information.print_half('Proxyless Mode: [ON]')
        else:
            Information.print_half('Total Proxy(s): [{}]'.format(str(len(stocking['files']['proxies']))))
        Information.print_half('Valid Account(s): [{}]'.format(str(stocking['values']['good'])))
        Information.print_half('Invalid Account(s): [{}]'.format(str(stocking['values']['bad'])))
        Information.print_half('Custom Account(s): [{}]'.format(str(stocking['values']['custom'])))
        Information.print_half('Retry(s): [{}]'.format(str(stocking['values']['retries'])))
        Information.print_half('Check(s) per minute: [{}]'.format(str(stocking['values']['cpm2'])))
        Information.print_half('Error(s): [{}]'.format(str(stocking['values']['errors'])))
        Information.print_half(' Press q to save.')
        time.sleep(1)
        if len(stocking['files']['lines']) == 0:
            ...
        else:
            threading.Thread(target=Screen.show).start()

def module(name):
    if not len(stocking['files']['proxies']): proxy=None
    else: 
        if len(stocking['files']['proxies']) != 0:
            proxy = random.choice(stocking['files']['proxies'])
        else:
            proxy = None
    account = random.choice(stocking['files']['lines'])
    stocking['files']['lines'].remove(account)
    username, password = account.split(':')[0], account.split(':')[1]
    thread = ExtremeDev.Threading(goto=Checker.check, argumente=(username, password, proxy,))
    thread.start()
    results = thread.join()
    for each in results: mode = results[each]
    if mode == 0: stocking['values']['good']+=1; stocking['values']['checked']+=1; stocking['values']['cpm1']+=1
    elif mode == 1: stocking['values']['bad']+=1; stocking['values']['checked']+=1; stocking['values']['cpm1']+=1
    elif mode == 2: stocking['values']['custom']+=1; stocking['values']['checked']+=1; stocking['values']['cpm1']+=1
    elif mode == 3: stocking['values']['retries']+=1; stocking['files']['lines'].append(each)
    elif mode == 4: stocking['values']['errors']+=1; stocking['files']['lines'].append(each)


Menu.loading()
