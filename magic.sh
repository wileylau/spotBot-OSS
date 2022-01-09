#!/bin/bash

# ffmpeg comp tool

mv "$1" in.flac
ffmpeg -i in.flac -compression_level 12 "$1"
rm -rf in.flac

touch link.txt
./transfer wet "$1" | grep Download > link.txt
sed -i "s/Link/$1 at/g" link.txt
rm -rf *.flac