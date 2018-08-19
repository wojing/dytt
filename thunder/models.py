from django.db import models


# Create your models here.
class DyttItem(models.Model):
    title = models.CharField(max_length=100)
    film_name = models.CharField(max_length=100)
    publish_time = models.CharField(max_length=50)
    full_name = models.CharField(max_length=150)
    trans_name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=30)
    decade = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    film_type = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    subtitles = models.CharField(max_length=50)
    IMDB_score = models.CharField(max_length=30)
    douban_score = models.CharField(max_length=30)
    director = models.CharField(max_length=100)
    format = models.CharField(max_length=30)
    resolution = models.CharField(max_length=30)
    size = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    actor = models.CharField(max_length=300)
    magnet_link = models.CharField(max_length=100)
    thunder_link = models.CharField(max_length=100)
    image_link = models.CharField(max_length=100)
    introduction = models.CharField(max_length=500)


'''
dict(IMDB_score='.7/10 from 4,335 users', actor='马丁·弗瑞曼 Martin Freeman', country='英国', decade='2017',
     director='杰瑞米·德桑 Jeremy Dyson / 安迪·尼曼 Andy Nyman', douban_score='7.5/10 from 216 users', duration='98分钟',
     film_type='恐怖', format='x264 + aac', full_name='Ghost Stories',
     image_link='https://www.z4a.net/images/2018/07/18/35b5ded1257fb24b0.jpg',
     introduction='舞台剧《鬼故事》将被搬上大银幕，新片主演马丁·弗瑞曼、乔治·麦凯、安迪·尼曼等。尼曼继续出演他在剧中的角色古德曼教授。古德曼是一位心理治疗师，从不相信鬼怪之说；然而三个病人的“见鬼实录”让他对原有信念产生了怀疑。作为最受欢迎的惊悚戏剧之一，该剧曾在全球多地进行巡演。 ',
     language='英语', magnet_link='ftp://ygdy8:ygdy8@yg72.dydytt.net:8247/阳光电影www.ygdy8.com.鬼故事.BD.720p.中英双字幕.mkv',
     publish_time='2017-10-05(伦敦电影节)/2018-04-06(英国)', resolution='1280 x 720', size='1CD', subtitles='中英双字幕',
     title='2018年恐怖《鬼故事/鬼谈怪说》BD中英双字幕', trans_name='鬼故事/鬼谈怪说')
'''
