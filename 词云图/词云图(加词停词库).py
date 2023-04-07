
pathwen = r'D:\desktop\词云图\txt'
savepath = r'D:\desktop\词云图\生'
picnamea = r'D:\desktop\词云图\原始图片\t0.png'

# ---------改上面两行代码即可-------------下面的代码无需更改-------------------------

import matplotlib.pyplot as plt #数据可视化
import jieba #词语切割
import wordcloud #分词
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS #词云，颜色生成器，停止词
import numpy as np #科学计算
from PIL import Image #处理图片
import os



def stopwordslist(filepath):
    stopwords = [line.strip().split('\n')[0] for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


def movestopwords(sentence,stopwords):
    stopwords = stopwords #stopwordslist('stop_words.txt')  # 这里加载停用词的路径
    #print(stopwords[:10])
    outstr = []
    for word in sentence:           #句子中的每一个字，
        if len(word) >= 2:
            if word not in stopwords:   #这里和英文不一样，应为如果这样用，就是字母了
                if word != '\t'and'\n':
                    outstr.append(word)
                    #outstr += word
                    #outstr += " "    #确实不需要这句，word本身就有可能是空格
    return outstr

##print(movestopwords(['中国','美国','日本']))

def ciyun(ciyunname, picname, stopwords, resultfile):
    try:
        with open(ciyunname,'r',encoding='utf-8') as f:  #打开新的文本转码为utf-8
            textfile= f.read()  #读取文本内容
    except:
        with open(ciyunname,'r',encoding='gbk') as f:  #打开新的文本转码为utf-8
            textfile= f.read()  #读取文本内容
    wordlist = jieba.lcut(textfile)#切割词语
    space_list1 = movestopwords(wordlist,stopwords)
    #print(len(space_list1))
    #print(type( wordlist))
    #print(wordlist[:10])
    space_list = ' '.join(space_list1) #空格链接词语
    #print(space_list[:30])
    #print(type(space_list))
    #picname = 'pic.png'  #更改名字
    backgroud = np.array(Image.open(picname)) 
    
    wc = WordCloud(width=1400, height=2200, #图片大小
			background_color='white',
                        mode='RGB', 
			mask=backgroud,
                        max_words= 300, # 高频词语数量
			stopwords=STOPWORDS.add('.'),
			font_path='C:\Windows\Fonts\STZHONGS.ttf',
			max_font_size=250,  #最大字号
			relative_scaling=0.6, #设置字体大小与词频的关联程度为0.4
			random_state=50, 
			scale=2 
			).generate(space_list) 		
			
    image_color = ImageColorGenerator(backgroud)#设置生成词云的颜色，如去掉这两行则字体为默认颜色
    wc.recolor(color_func=image_color)

    plt.imshow(wc) #显示词云
    plt.axis('off') #关闭x,y轴
    #plt.show()#显示
    
    wc.to_file(resultfile) #保存词云图
##    print('已经生成：','result_'+ k +'.png')
    

if __name__ == '__main__':
    
    stopwords = stopwordslist(r'D:\desktop\词云图\stop_words.txt')
    jieba.load_userdict(r"D:\desktop\词云图\add_word.txt")
    picname = picnamea 
    
    pathwen = pathwen
    savepath = savepath
    
    filejias = os.listdir(pathwen)
    for filejia in filejias:
        newpath = pathwen+'\\'+ filejia
        files = os.listdir(newpath)
        print(filejia)
        for file in files:
            readfile = newpath+'\\'+file
            k = file[:-4]
            resultfile = savepath+'\\'+str(picnamea[-5])+k+'.png'
            ciyun(readfile, picname, stopwords, resultfile)
            print(file)
            
    print('执行结束')















