
# main.py
import sys

from cli_module import main as cli_main
from gui_module import GUIApp


def main():
    # Check if command-line arguments are provided
    if len(sys.argv) > 1:
        # Run the CLI module
        cli_main()
    else:
        # Run the GUI module
        app = GUIApp()
        app.mainloop()


if __name__ == "__main__":
    main()
