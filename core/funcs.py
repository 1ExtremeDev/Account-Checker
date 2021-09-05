"""

AUTHOR: ExtremeDev
INSTAGRAM: @extremedevalt
Date: 17/03/2020

"""

for each in ('os', 'platform', 'ctypes', 'sys', 'time'): exec('import {}'.format(str(each)))
if platform.platform().startswith('Windows'):
    import tkinter
    from tkinter import filedialog, messagebox

class System:
    def quit(code=None) -> ...:
        sys.stdout.write('\n')
        if code is None: os._exit(0)
        else: os._exit(code)

    def clear() -> ...:
        if platform.platform().startswith('Windows'):
            os.system('cls') # Windows
        else:
            os.system('clear') # Linux        

    def title(title_name: str=None) -> ...:
        if title_name is None:
            title_name = '{}'.format('')
        if platform.platform().startswith('Windows'):
            ctypes.windll.kernel32.SetConsoleTitleW(str(title_name))
        else:
            print('\33]0;{}\a'.format(str(title_name)), end='')
            sys.stdout.flush()

    def println(*args) -> ...:
        cl = ''
        for each in args:
            cl+=each
        sys.stdout.write(cl)
        del cl
    def print_info():
        from .config import Information
        Information.print_half(Information.title())
        Information.print_half(' Version {} by {}'.format(Information.version(), Information.author()))
        Information.print_half(' Announcement: "{}"'.format(Information.information()))
            
            
class Load():
    def _file():
        if platform.platform().startswith('Windows'):
            root = tkinter.Tk()
            root.withdraw()
            filename = filedialog.askopenfile(parent=root, mode='rb', title='Choose a file',
                                        filetype=(("txt", "*.txt"), ("All files", "*.txt")))
            if filename is None:
                System.println(' Please enter a valid file.', '\n')
            else:
                if os.path.exists(filename.name):
                    return filename.name
                else:
                    System.println(' Please enter a valid location for your file.', '\n')
            time.sleep(2)
            return False
        else:
            System.println(' Please drag and drop your file location.', '\n')
            try:
                received_inp = input(' > ')
                if received_inp.startswith("'") and received_inp.endswith("'"):
                    try:
                        if os.path.exists(received_inp.split("'")[1]):
                            return received_inp.split("'")[1]
                        else:
                            ...
                    except:
                        if os.path.exists(received_inp):
                            return received_inp
                        else:
                            ...
                else:
                    if os.path.exists(received_inp):
                        return received_inp
                    else:
                        ...
            except:
                ...
            time.sleep(2)
            return False
    def combos():
        input(' Press enter to load your combos.')
        System.println('\n')
        filename = Load._file()
        if filename:
            try:
                file_opend = open(str(filename), 'r', encoding='utf-8').readlines()
                valids, bad = [], []
                for each in file_opend:
                    if each.__contains__(':'):
                        valids.append(each.replace('\n', ''))
                    else:
                        bad.append(each.replace('\n', ''))
                return [valids, bad]
            except Exception as error:
                ...
        else:
            return bool(0)
        System.println(' Cannot open {} file, error ocurred, re-try! ({})'.format(str(filename) if type(filename) is not bool else 'unknown', str(error)), '\n')
        time.sleep(2)
        return bool(1)
    def proxies(proxytype: str=None):
        if proxytype is None:
            proxytype = 'http'
        x = input(' Press enter to load your proxies. (type x to use proxyless mode.)\n > ')
        if x == 'x':
            return [[], []]
        System.println('\n')
        filename = Load._file()
        if filename:
            try:
                file_opend = open(str(filename), 'r', encoding='utf-8').readlines()
                proxies = []
                bad = []
                for each in file_opend:
                    each = each.replace('\n', '')
                    if len(each.split(':')) not in (2,3,4,5):
                        bad.append(each)
                    else:
                        if not len(each.split(':')) % 2: 
                            each = proxytype + ':' + each
                        if not each.split(':')[0] in ('http', 'https', 'socks4', 'socks5'):
                            bad.append(each)
                        else:
                            if len(each.split(':')) == 3:
                                proxies.append(
                                    {
                                        f'http': '{}://{}:{}'.format(proxytype, each.split(':')[1], each.split(':')[2]),
                                        f'https': '{}://{}:{}'.format(proxytype, each.split(':')[1], each.split(':')[2])
                                    }
                                )
                            else:
                                proxies.append(
                                    {
                                        f'http': '{}://{}:{}@{}:{}'.format(proxytype, each.split(':')[3], each.split(':')[4], each.split(':')[1], each.split(':')[2]),
                                        f'https': '{}://{}:{}@{}:{}'.format(proxytype, each.split(':')[3], each.split(':')[4], each.split(':')[1], each.split(':')[2]),
                                    }
                                )
                return [proxies, bad]
            except:
                return False

class Others:
    def get_threads():
        System.clear()
        System.print_info()
        System.println('\n How many threads do you want to use?\n > ')
        try:
            threads = int(input())
        except:
            print(' Please enter a valid input.\n Setting to default 250.')
            time.sleep(2)
            return 250
        return threads
    def get_refresh():
        ...