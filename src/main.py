# main.py
from structur import structure
import argparse

def menu():
    parser = argparse.ArgumentParser(prog="Github-activity", description="Lihat aktivitas Push GitHub")
    parser.add_argument("username", help="Username GitHub")
    args = parser.parse_args()
    
    structure(args.username)

if __name__ == "__main__":
    menu()
