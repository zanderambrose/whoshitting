#!/bin/bash

# Run the Python script in the background
python main.py &

# Keep the container running
tail -f /dev/null