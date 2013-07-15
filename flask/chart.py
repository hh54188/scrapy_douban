
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

    def generateObj(self, words):
        result = {}
        for word in words:
            word = word.decode('utf-8')
            self.TEMP[word] = 0

    def sortBy(self, data):
        for word in data:
            return data[word]

    def start(self, data):
        self.generateObj(self.KEY_WORDS["location"])
        for item in data:
            title = item["title"]
            for word in self.TEMP:
                if word in title:
                    self.TEMP[word] += 1

        # self.TEMP = sorted(self.TEMP.iteritems(), key = operator.itemgetter(1))
        print self.TEMP
        # for key in self.TEMP:
        #     print key
        #     print str(self.TEMP[key])

        return self.TEMP


