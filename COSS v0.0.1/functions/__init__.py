colors = {
    'Green':'\033[1;32m',
    'Purple':'\033[1;35m',
    'Yellow':'\033[1;33m',
    'Blue':'\033[1;34m',
    'Red':'\033[1;31m',
    'Cyan':'\033[36m',
    'Close':'\033[m'
}

def write_on_txt(text:str,path:str,date:bool=True):
    from datetime import datetime
    with open(path,'a') as txt:
        if not date:
            txt.write(f'\n{text}')
        else:
            txt.write(f'\n{datetime.now()}: {text}')
