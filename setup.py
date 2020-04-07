import os
import logging
import sys
import shutil
from datetime import datetime

def startCopy(source, destination):
  basename = os.path.basename(source)
  logging.info(f"Copying {basename} from {source} into {destination}")
  shutil.copyfile(source.replace('~',os.path.expanduser('~')),destination+basename)
  logging.info(f"Successfully copied {source} into {destination}...")

if __name__ == "__main__":
  targets = logging.StreamHandler(
    sys.stdout), logging.FileHandler('./log.log')
  logging.basicConfig(format='[%(asctime)s] %(message)s',
            level=logging.INFO, handlers=targets, datefmt='%Y-%m-%d %H:%M:%S')
  # logging.info('testing the logging system')
  try:
    with open('./.setting') as setting:
      for line in setting.read().strip().splitlines():
        print(line)
        source, destination = line.split(',')
        try:
          startCopy(source,destination)
        except Exception as e:
          logging.info(f"Cannot copy {source} into {destination}, {e}")
  except Exception as e:
    logging.info(e)
  finally:
    pass
