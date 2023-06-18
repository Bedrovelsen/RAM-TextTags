#! /bin/bash

ls "$1" | xargs -I {} python r.py ./"$1"/{}