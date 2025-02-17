import sys
import argparse

import gui


def main():
    """ Program is primarily intended to be ran in GUI mode
        but can be started in CLI mode for debugging
    """
    unparsed_args = sys.argv[1:] if len(sys.argv) > 1 else None
    if unparsed_args:
        # Parses command line arguments if present
        parser = argparse.ArgumentParser(
            description="A GUI script with CLI debugging."
        )

        # Define command-line arguments
        parser.add_argument("-h", "--help", action="store_true", help="Show help info")
        parser.add_argument("-v", "--version", action="store_true", help="Show version info")
        parser.add_argument("-d", "--debug", action="store_true", help="Enter debugging mode")

        # Parse arguments
        args = parser.parse_args()

        help_text = "PokeBot Help:\n\t\
	    		PokeBot is primarily a GUI program.\nTo run in GUI mode,\
	    		launch with no arguments or enter 'g' now\n\t\t\
	    		eg. 'python3 ./PokeBot/main.py\n\
	    		Available CLI arguments:\n\t\
	    		'-h'/'--help'    - Show help fogo\n\t\
	    		'-v'/'--version' - Show version info\n\t\
	    		'-d-/'--debug'   - Enter debugging mode\n\
	    		To quit, enter 'q'\n-- "

        # Handle arguments
        if args.help:
            help_input = input(help_text).lower()
            if help_input == 'q':
                quit()
            elif help_input == 'g':
                gui.main()
            else:
                print(f"Invalid input: {help_input}\n Exiting help menu")
                quit()
        elif args.version:
            print("Version 1.0.0")
        elif args.debug:
            print("Reset config? (y/n)")
            debug_input = input("-- ").lower()
            if debug_input == 'y':
                # reset config
                pass
            else:
                print("No other options available currently\n\
	        			Exiting debug menu")
                quit()
        else:
            print("No valid options provided. Use -h for help.")

    else:
        gui.main()


if __name__ == "__main__":
    main()
