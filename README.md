# iterm2-startup-script

Startup script for iterm2. 

Initialize a script using these instructions: https://iterm2.com/python-api/tutorial/index.html

Add a commands.json file to the same directory as the script with a location, command, and optional wait time for each one. If multiple commands are added  under the `commands` key, they will be run in new vertically split panes.

Example:
```json
[
    {
        "commands": [
            {
                "location": "~/code/src/github.com/kristakoch/first-server",
                "command": "task run -f",
            },
            {
                "location": "~/code/src/github.com/kristakoch/ui",
                "command": "task local -f",
                "wait_time": 10
            }
        ]
    },
    {
        "commands": [
            {
                "location": "~/code/src/github.com/kristakoch/second-server",
                "command": "task run -f"
            }
        ]
    }
]
```