#!/bin/bash

# ffmpeg comp tool

upload() {
        touch link.txt
        ./transfer wet "$1" | grep Download > link.txt
}

ZIPNAME=$(date +%s)

if [[ $2 == "-f" ]]; then
        spotdl "$1" --output-format flac
elif [[ $2 == "-m" ]]; then #mp3
        spotdl "$1"
fi

if [[ $2 == "-f" && $3 == "-t" ]]; then
        MUSIC=$(ls | grep .flac)
elif [[ $2 == "-m" && $3 == "-t" ]]; then
        MUSIC=$(ls | grep .mp3)
fi

if [[ $3 == "-a" || $3 == "-p" ]];then
        if [[ $2 == "-f" ]]; then
                zip -r $ZIPNAME.zip *.flac
                MUSIC=$ZIPNAME.zip
        elif [[ $2 == "-m" ]]; then
                zip -r $ZIPNAME.zip *.mp3
                MUSIC=$ZIPNAME.zip
        fi
fi

echo $MUSIC

if [[ $3 != "" ]]; then
        upload "$MUSIC" "Playlist / Album"
else
        upload "$MUSIC" $MUSIC
fi

sed -i "s/Link/$MUSIC at/g" link.txt

if [[ ! -n $(ls | grep .zip) &&  ! -n $(ls | grep .flac) &&  ! -n $(ls | grep .mp3) ]]; then
        echo "Something went wrong. Check your entries and try again." > link.txt
fi

rm -rf *.flac
rm -rf *.mp3
rm -rf *.zip