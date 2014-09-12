#jobs/cron.py
import logging

from django.core.management import call_command

import kronos

@kronos.register('0 18 * * *')
@kronos.register('0 0 * * *')
def run_daily_job():
    try:
        logger = logging.getLogger('jobs.management.commands')
        logger.info('Starting daily_job')
        call_command('download_quotes')
        call_command('create_daily_quotes')
        logger.info('Finished daily_job')
    except Exception, e:
        logger.error(e)