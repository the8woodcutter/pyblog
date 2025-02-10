#!/bin/sh
cp ./config.example.py > ./config.py
echo "NOTICE:"
ls -lh | grep "config.py"
echo "    ^ EDIT THIS FILE WITH YOUR OWN VARIABLES >> ./config.py << EDIT THIS!"
echo