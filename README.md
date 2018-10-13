**Index**   

- [DESCRIPTION](#description)
- [INSTALATION](#instalation)
- [REFERENCES](#references)


# DESCRIPTION

Automate a permanent video conference through hangouts in a linux system (tested with Pine Rock64). It automatically starts and stop the conference and turn the TV on and off. Work in progress.
# INSTALATION

```
pip3 install -r requirements.txt
sudo apt-get install libcec-dev build-essential python-dev # cec related
sudo apt-get install scrot # PyAutoGUI related
```

# REFERENCES
https://pypi.org/project/PyAutoGUI/
https://github.com/trainman419/python-cec
