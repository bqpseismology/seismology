#!/bin/bash

if [ ! -d "$1" ]; then
    mkdir $1
fi

cp -r seismology/ setup.py MANIFEST dist/ build/ $1/
