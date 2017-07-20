# msdos
Monitoring System and Disk Operating System

## Executive summary
Use case: you want to monitor bunch of HTTP(s) URLs and get a [Pushover](https://pushover.net/) notification if they do not respond as you wish. This is the simplest possible way to do that.

## How to use
Check out the code, install requirements with pip (`pip install -r requirements.txt`), and save `config.yml.template` as `config.yml` customized with your configuration. Then run `python3 msdos.py` with crontab every minute.
