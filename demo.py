# coding:utf-8

from os import path
import chnSegment
import plotWordcloud


if __name__=='__main__':

    # 读取文件
    d = path.dirname(__file__)
    with open(path.join(d, 'doc//十九大报告全文.txt'), 'r', encoding='utf-8') as f:
        text = f.read()

    #with open(path.join(d, 'doc//alice.txt'), 'r', encoding='utf-8') as f:
        #text = f.read()

    # text = open(path.join(d,'doc//alice.txt')).read()

    # 若是中文文本，则先进行分词操作
    text=chnSegment.word_segment(text)
    
    # 生成词云
    plotWordcloud.generate_wordcloud(text)
