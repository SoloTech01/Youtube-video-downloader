from pytube import YouTube
import colorama
import sys, os, time


colorama.init()
G = colorama.Fore.GREEN
Y = colorama.Fore.YELLOW
lb = colorama.Fore.LIGHTBLUE_EX
r = colorama.Fore.RED
RESET = colorama.Fore.RESET


def sd(string):
    for c in string + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1 / 100)

def sd1(string):
     for c in string + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)
        
def yt_vid():
	print("\n")

	sd1(f"{lb}<<<<<<<<<<<<<<<<<Enter the youtube video link:>>>>>>>>>>>>>>>>>>>>>> ")
	try:
		url = input(Y)
		yt = YouTube(url)
		print("\n")
		sd1(f"{G}Downloading........")
		stream = yt.streams.filter(progressive=True,file_extension='mp4').first()
		stream.download(output_path="/storage/emulated/0/")
		print("\n")
		sd1("[✓] DOWNLOAD COMPLETE!")
		print("\n")
		sd1("[✓] VIDEO PATH: /storage/emulated/0/")
		print("\n")
		print(Y)
		sd1("THANKS FOR USING THIS PROGRAM,KINDLY FOLLOW ME ON GITHUB: SOLOTECH01")
		print("\n")
		print(G)
		sd1("<<<<<<<<<<<<<<<<<Do you want to continue (y/n):>>>>>>>>>>>>>>>>>")
		response = input(Y)
		if response.lower().strip() == "y":
			program_intro()
		elif response.lower().strip() == "n":
			print("\n")
			print(r)
			sd1("TERMINATING......")
			print(RESET)
			time.sleep(3)
			sys.exit()
		else:
			print("\n")
			print(r)
			sd1("INVALID OPTION!")
			print(RESET)
			sys.exit()
			
	except:
		print("\n")
		print(r)
		sd1("AN ERROR OCCURRED!")
		print(RESET)

def program_intro():
	os.system("clear")
	sd(f"""{G}
_   _ ____ _  _ ___ _  _ ___  ____       _  _ _ ___  ____ ____
 \_/  |  | |  |  |  |  | |__] |___     {Y}  |  | | |  \ |___ |  |
  |   |__| |__|  |  |__| |__] |___        \/  | |__/ |___ |__|

___  ____ _ _ _ _  _ _    ____ ____ ___  ____ ____
|  \ |  | | | {G}| |\ | |    |  | |__| |  \ |___ |__/
|__/ |__| |_|_| | \| |___ |__| |  | |__/ |___ |  \


""")

	sd1(f"{Y}        Download Youtube Videos directly to your phone's storage")
	print("\n")
	sd1(f"{G}[+] CREATED BY SOLOMON ADENUGA")
	print("\n")
	sd1("[✓] GITHUB: SOLOTECH01")
	print(RESET)
	yt_vid()

program_intro()