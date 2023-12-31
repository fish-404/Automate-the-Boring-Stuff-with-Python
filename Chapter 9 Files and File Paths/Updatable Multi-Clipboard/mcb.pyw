#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: 
#   py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#   py.exe mcb.pyw delete <keyword> - Delete keyword 
#   py.exe mcb.pyw <keyword>      - Loads keyword to clipboard.
#   py.exe mcb.pyw list           - Loads all keywords to clipboard.
#   py.exe mcb.pyw delete         - Delete all keywords

import shelve, pyperclip, sys 

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3:
    # Save clipboard content.
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    # Delete keyword.
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

