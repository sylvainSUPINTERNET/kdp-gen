from dotenv import load_dotenv

load_dotenv()

from src.services.EbookGenerator import print_book

if __name__ == '__main__':
    print_book()
    print("book printed with success")