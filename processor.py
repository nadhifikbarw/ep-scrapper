import os.path as ospath
from DataProcessor import Processor
import processor_settings as SETTING

if __name__ == '__main__':
    # Resolve absolute path
    tweets_dir = ospath.abspath(SETTING.TWEETS_DIR)
    if ospath.isdir(tweets_dir) is False:
        raise Exception('Tweets directory is not found, given: ' + tweets_dir + ' not found')

    # Create Processor
    processor = Processor(tweets_dir, ospath.abspath('./out.csv'))

    # Run processor
    processor.handle()
