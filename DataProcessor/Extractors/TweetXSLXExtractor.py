from pandas import read_excel


from ..Models import Tweet


class TweetXSLXExtractor:
    @staticmethod
    def handle(filepath):
        result = []
        for index, data in read_excel(filepath, sheet_name='tagged', usecols='A:B').dropna().iterrows():
            result.append(Tweet(ft=data.tweet, tag=data.tag))
        return result
