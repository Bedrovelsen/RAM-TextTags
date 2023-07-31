#! /bin/bash

(ls "$1" | xargs -I {} echo "python r.py ./"$1"/{} | grep -v Loaded | tee -a "$1".json")