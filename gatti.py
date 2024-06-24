import requests
import argparse
import os

def download(url, filename, chunk_size=1024*10):
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=chunk_size):
                file.write(chunk)
        return True
    else:
        return False

def run():

    parser = argparse.ArgumentParser(description='Download di gatti da robohash')
    parser.add_argument('-g','--gatto', type=str, help='Nome del gatto')
    parser.add_argument('-i','--infile', type=str, help='Filename con nomi di gatti')

    args = parser.parse_args() 
    if args.gatto:    
        url = 'https://robohash.org/set_set4/'+args.gatto
        download(url,f'{args.gatto}.png')

    if args.infile:
        # if os.path.exists(args.infile) and os.path.isfile(args.infile):
        if os.path.isfile(args.infile): # isfile controlla anche se il file esiste
            file = open(args.infile)
            nomi = file.readlines()
            file.close()

            for nome in nomi:
                print(f'download del gatto {nome}')
                nome = nome.strip()
                url = 'https://robohash.org/set_set4/'+nome
                download(url,f'{nome}.png')                


        # TODO eseguire un download per ogni nome


if __name__ == '__main__':
    run()