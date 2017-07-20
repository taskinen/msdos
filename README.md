# msdos
Monitoring System and Disk Operating System

## Executive summary
Use case: you want to monitor bunch of HTTP(s) URLs and get a [Pushover](https://pushover.net/) notification if they do not respond as you wish. This is the simplest possible way to do that.

## How to use
Check out the code, install requirements with pip (`pip install -r requirements.txt`), and save `config.yml.template` as `config.yml` customized with your configuration. Then run `python3 msdos.py` with crontab every minute.

## Known issues
* The notifications are ugly. They may be hard to read and contain unnecessary information such as exceptions and stack tracebacks from the libraries used.
* No history. This program does not save any kind of history data. There is no way to know how long a URL has been broken. Also the program will send a notification every time it is run and the URL is broken.
