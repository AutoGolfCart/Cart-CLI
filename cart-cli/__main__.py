import sys

# Drive Computer Remote Command Line Client
# Main
#
# Part of the GSSM Autonomous Golf Cart
# Written by: Joseph Telaak, class of 2022

if __name__ == "__main__":
    # Version Check
    python_major = sys.version_info[0]
    python_version = str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2])

    # Check for Python 3
    if python_major != 3:
        print(f"The GSSM Auto Golf Cart Drive Computer Command Line Client Requires Python 3. You are using {python_version}")
        sys.exit(1)

    # Imports
    import src.cli as cli
    import src.util as util

    # Banner and Info Block
    print(util.to_color(util.title, "cyan"))
    print(util.info_block)

    # Check args
    if len(sys.argv) == 1:
        print(util.to_color("Please Specify the IP Address of the Drive Computer", "red"))
        sys.exit(1)
    
    # Run Program
    cli.init()
    cli.run()