import sys

from src.connector import CLI_Connector

# Drive Computer Remote Command Line Client
# CLI
#
# Part of the GSSM Autonomous Golf Cart
# Written by: Joseph Telaak, class of 2022

# Connector
connector = CLI_Connector(ip_addr=str(sys.argv[0]),establish_port=42069, command_port=69, log_port=420, response_port=777)

# Initialization
def init():
    print("Initializing Teleop Client")

    # Establish Server Connection
    if connector.establish_connection():
        connector.startListeners()
    
    else:
        sys.exit(1)

    print("Initialization Complete")

# Main loop
def run():
    message = "echo \"Hello!\""

    # While message is not ended
    while message != "end":
        # Send message
        connector.sendCommand(message)

        # Get message
        message = input(">")

    # Close
    connector.close()