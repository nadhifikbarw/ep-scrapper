import os.path as ospath


from DataProcessor import Processor
import processor_settings as SETTING

if __name__ == '__main__':
    # Resolve absolute path
    tagged_file = ospath.abspath(SETTING.TAGGED_FILE)
    if ospath.isfile(tagged_file) is False:
        raise Exception('Tweets directory is not found, given: ' + tagged_file + ' not found')

    # Create Processor
    processor = Processor(tagged_file, ospath.abspath('./out.csv'))

    # Run processor
    processor.handle()
