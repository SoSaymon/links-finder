import re
import webbrowser
import argparse
import os


def find_links(file):
    # Regular expression pattern to find links
    pattern = re.compile(r'http[s]?://\S+[^\s.,;)"]')

    with open(file, 'r') as f:
        content = f.read()

    # Find all links in the file
    links = re.findall(pattern, content)

    # Remove any punctuation from the end of the links
    cleaned_links = [link.rstrip(".,;)'") for link in links]

    return cleaned_links


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='file to scan for links')
    args = parser.parse_args()

    file = args.file
    if not file:
        file = input("Enter the file path: ")

    links = find_links(file)

    while True:
        clear_console()
        print("Found links:")
        for i, link in enumerate(links):
            print(f"{i + 1}. {link}")

        choice = input("Enter the number of the link you want to open (or 0 to exit): ")

        try:
            choice = int(choice)
            if choice == 0:
                break
            elif choice > 0:
                webbrowser.open(links[choice - 1])
        except (ValueError, IndexError):
            print("Invalid choice.")


if __name__ == '__main__':
    main()
