# -*- coding: utf-8 -*- 
import operator
class ChartClas(object):
    KEY_WORDS = {
        'location': ['西苑', '西二旗', '知春路', '牡丹园', '人民大学', '回龙观', '霍营', '望京', '立水桥', '西直门', '三元桥', '劲松', '惠新', '四惠', '鼓楼', '天通'],
        'line': ['一号', '1号', '八通', '四号', '4号', '大兴', '六号', '6号', '九号', '9号', '十三号', '13号', '房山', '亦庄', '二号', '2号', '五号', '5号', '八号', '8号', '十号', '10号', '十五号', '15号', '昌平']
    }
    TEMP = {}

    def __init__(self):
        pass

    def generateDict(self):
        result = {}
        for key  in self.KEY_WORDS:
            result[key] = []
            for word in self.KEY_WORDS[key]:
                word = word.decode('utf-8')
                temp = {
                    'name': word,
                    'count': 0
                }
                result[key].append(temp)
        return result


    def sortBy(self, dictObj):
    	pass


    def analysis(self, data):
        dicObj = self.generateDict();
        for item in data:
            title = item["title"]
            for key in dictObj:
                for item in dictObj[key]:
                    if item.name in title:
                        item.count += 1
        return dictObj

char = ChartClas()
char.analysis(range(10))


