import collections
import json
import xml.etree.ElementTree as ET

def read_json(file_name = "newsafr.json", max_len_word = 6, top_words = 10):
    with open(file_name, encoding="utf-8") as news_file:
        news = json.load(news_file)
        description_words = []
        for item in news['rss']['channel']['items']:
            description =[word for word in item['description'].split(' ') if len(word) > max_len_word]
            description_words.extend(description)
            counter_word = collections.Counter(description_words)

        print(counter_word.most_common(top_words))

def read_xml (file_name = "newsafr.xml", max_len_word = 6, top_words = 10):
    parser = ET.XMLParser(encoding='utf-8')
    xml_data = ET.parse(file_name, parser)
    xml_root = xml_data.getroot()

    description_words = []
    news = xml_root.findall("channel/item/description")
    for item in news:
        description = [word for word in item.text.split(' ') if len(word) > max_len_word]
        description_words.extend(description)
    counter_word = collections.Counter(description_words)
    print(counter_word.most_common(top_words))

        # print(counter_word.most_common(top_words))



if __name__ == '__main__':
    read_xml()
