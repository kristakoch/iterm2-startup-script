#!/usr/bin/env python3.7

import iterm2
import json
import os
import sys

from time import sleep

async def main(connection):
    app = await iterm2.async_get_app(connection)

    window = app.current_terminal_window

    # Load the commands file
    script_dir = os.path.dirname(os.path.realpath(__file__))
    commands_file = os.path.join(script_dir, "commands.json")

    try:
        with open(commands_file, "r") as f:
            tabs = json.load(f)
    except Exception as e:
        
        # A nice, hacky exit
        error_message = f"# Failed to load commands from {commands_file}."
        session = window.current_tab.current_session
        await window.current_tab.current_session.async_send_text(error_message)
        sys.exit(1)  

    # Loop through tabs and execute each command group in a new tab 
    # or split pane if there are multiple commands
    if window is not None:
        first_tab = True

        for tab in tabs:

            # Create a new tab for every set except the first
            if first_tab:
                first_tab = False 
            else: 
                await window.async_create_tab()
            
            first_command = True
            
            for command_set in tab["commands"]:
                # Use the current session for the first command, then split for subsequent ones
                if first_command:
                    session = app.current_terminal_window.current_tab.current_session
                    first_command = False
                else:
                    session = await session.async_split_pane(True, False)
                
                # Change to the specified directory
                await session.async_send_text(f'cd {command_set["location"]} \n')

                # Run the command
                await session.async_send_text(f'{command_set["command"]}\n')

                # Optional wait after each command set if wait_time is specified
                if "wait_time" in command_set:
                    sleep(command_set["wait_time"])

        else:
            print("No current window")

iterm2.run_until_complete(main)