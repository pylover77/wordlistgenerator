import sys,itertools,string,time


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

if len(sys.argv)>=5:
    try:
        min_lenght=int(sys.argv[1])
        max_lenght=int(sys.argv[2])
        char=sys.argv[3]
        file=open(sys.argv[4], "w")
        for i in range(min_lenght, max_lenght + 1):
            for j in itertools.product(char, repeat=i):
                string=''.join(j)
                file.write(string + "\n")
                sys.stdout.write('\r[+] Creating Wordlist...')
                sys.stdout.flush()
        time.sleep(1.5)
        print (bcolors.GREEN + "\n[+] Wordlist done : " + sys.argv[4])
        print (bcolors.YELLOW + '\n[-] End time: ' + time.strftime('%H:%M:%S'))
        file.close()
    except KeyboardInterrupt:
        print (bcolors.RED + "\n~~keyboard interrupt .. ")
else:
    print (bcolors.RED + "\n[!]SYNTAX ERROR \nCORRECT SYNTAX: wd_generator.py min_lenght max_lenght chars name_file")