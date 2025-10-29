from pathlib import Path
from sys import argv

def main():
    try:
    
        with open(Path(argv[1]),'r') as log:
            print(log.readline())
    except IndexError:
        print('Please enter path to your directory')
    except FileNotFoundError:
        print('Please enter valid path to your directory')

if __name__ == "__main__":
    main()