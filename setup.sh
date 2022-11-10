#!/bin/bash

echo "Starting project setup"

# git clone https://github.com/DuckyCB/reverse-vending-machine_tic5

python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
