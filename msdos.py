#!/usr/bin/env python3

import yaml
import pprint
import requests
import logging
import pushover
from logging.config import fileConfig
fileConfig('logging_config.ini')
logger = logging.getLogger()

pp = pprint.PrettyPrinter(indent=2)

logger.info( 'Monitoring System and Disk Operating System' )

configFile = open('config.yml')
configMap = yaml.safe_load(configFile)
configFile.close()

pushover = pushover.Client( configMap['pushover']['user'], api_token=configMap['pushover']['api_token'] )

# pp.pprint(configMap)

def doCheck( check, service, config ):

  if check == 'http':
    logger.debug("Executing check: " + check )
    logger.debug("Checking URL: " + config['url'])
    try:
      r = requests.get( config['url'] )
    except requests.exceptions.RequestException as e:
      msg = e
      logger.error(msg)
      pushover.send_message(msg, title=service + " " + check)
    else:
      if r.status_code != int(config['response']):
        msg = "Response code " + str(r.status_code) + " does not match expected " + str(config['response'])
        logger.error(msg)
        pushover.send_message(msg, title=service + " " + check)

for service in configMap['services']:
  for check in configMap['services'][service]['checks']:
    logger.debug(service + ": " + check)
    doCheck( check, service, configMap['services'][service]['checks'][check] )
