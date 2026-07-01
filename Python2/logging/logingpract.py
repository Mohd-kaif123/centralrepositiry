import logging

'''
logging.basicConfig(
    filename='system.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info('root:Application Started')
'''
'''
logging.basicConfig(
    filename='system.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info('Root: Application started')
logging.info('Root: Loading Data')
logging.info('Root: Program Finished')
logging.warning('root: Disk usage is High')
logging.error('root: Application Crashed')
'''
'''
logging.basicConfig(
    filename='system.log',
    level=logging.DEBUG,
    format='%(levelname)s:%(message)s:%(name)s'
)
name =input("Enter Name:")
logging.info(f"User {name} Logged IN ")
'''
'''
logging.basicConfig(
    filename='system.log',
    level=logging.DEBUG,
   format='%(asctime)s - %(levelname)s - %(message)s'
)
def backup():
    logging.info("Backup  started")
    logging.info("Backup completed")
backup()
'''
'''
logging.basicConfig(
    filename='system.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s'
)
disk = 85
if (( disk>=80 )):
    logging.warning('Disk usage is High')
else:
    logging.info('Disk Usage is Normal')
'''
'''
logging.basicConfig(
    filename='system.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s'
)
service = "nginx"
status = "running"
if status == "running" :
    logging.info(f"{service} is running")
else:
    logging.warning(f"{service} is stopped")
'''
'''
import sys
logging.basicConfig(
    filename='system.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s'
)
name = sys.argv[1]
logging.info(f"User {name} is logged in")
'''