import requests
from lxml import etree
import re
from selenium import webdriver
from copy import deepcopy

class Music163:
    def __init__(self):
        self.start_url = "http://music.163.com/discover/playlist"
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
    def parse_url(self,url):
        print(url)
        resp = requests.get(url,headers=self.headers)
        return resp.content.decode()

    def get_category_list(self):#获取大分类和小分类
        resp = self.parse_url(self.start_url)
        html = etree.HTML(resp)
        dl_list = html.xpath("//div[@class='bd']/dl")
        category_list = []
        for dl in dl_list:
            b_cate = dl.xpath("./dt/text()")[0] if len(dl.xpath("./dt/text()"))>0 else None
            a_list = dl.xpath("./dd/a")
            for a in a_list:
                item = {}
                item["b_cate"]= b_cate
                item["s_cate"] = a.xpath("./text()")[0] if len(a.xpath("./text()"))>0 else None
                item["s_href"] = "http://music.163.com"+a.xpath("./@href")[0] if len(a.xpath("./@href"))>0 else None
                category_list.append(item)
        return category_list

    def get_playlist_list(self,item,total_playlist_list):#获取小分类中的playlist列表
        playlist_list = []
        if item["s_href"] is not None:
            scate_resp = self.parse_url(item["s_href"])
            scate_html = etree.HTML(scate_resp)
            li_list = scate_html.xpath("//ul[@id='m-pl-container']/li")
            for li in li_list:
                item["playlist_title"] = li.xpath("./p[@class='dec']/a/@title")[0] if len(li.xpath("./p[@class='dec']/a/@title"))>0 else None
                print(item["playlist_title"])
                item["playlist_href"] = "http://music.163.com"+li.xpath("./p[@class='dec']/a/@href")[0] if len(li.xpath("./p[@class='dec']/a/@href"))>0 else None
                item["author_name"] = li.xpath("./p[last()]/a/@title")[0] if len(li.xpath("./p[last()]/a/@title"))>0 else None
                item["author_href"] = "http://music.163.com"+li.xpath("./p[last()]/a/@href")[0] if len(li.xpath("./p[last()]/a/@href"))>0 else None
                playlist_list.append(deepcopy(item))
            total_playlist_list.extend(playlist_list)
            next_url = scate_html.xpath("//a[text()='下一页']/@href")[0] if len(scate_html.xpath("//a[text()='下一页']/@href"))>0 else None
            if next_url is not None and next_url!='javascript:void(0)':
                item["s_href"] = "http://music.163.com"+next_url
                #递归，调用自己，获取下一页的播放列表，直到下一页没有的时候不再递归
                return self.get_playlist_list(item,total_playlist_list)
        return total_playlist_list

    def get_playlist_info(self,playlist): #获取单个播放别表的信息
        if playlist["playlist_href"] is not None:
            playlist_resp = self.parse_url(playlist["playlist_href"])
            playlist["covers"] = re.findall("\"images\": .*?\[\"(.*?)\"\],",playlist_resp)
            playlist["covers"] =  playlist["covers"][0] if len(playlist["covers"])>0 else None
            playlist["create_time"] = re.findall("\"pubDate\": \"(.*?)\"",playlist_resp)
            playlist["create_time"] = playlist["create_time"][0] if len(playlist["create_time"])>0 else None
            playlist_html = etree.HTML(playlist_resp)
            playlist["favorited_times"] = playlist_html.xpath("//a[@data-res-action='fav']/@data-count")[0] if len(playlist_html.xpath("//a[@data-res-action='fav']/@data-count"))>0 else None
            playlist["shared_times"] = playlist_html.xpath("//a[@data-res-action='share']/@data-count")[0] if len(playlist_html.xpath("//a[@data-res-action='share']/@data-count"))>0 else None
            playlist["desc"] = playlist_html.xpath("//p[@id='album-desc-dot']/text()")
            playlist["played_times"] = playlist_html.xpath("//strong[@id='play-count']/text()")[0] if len(playlist_html.xpath("//strong[@id='play-count']/text()"))>0 else None
            playlist["tracks"] = self.get_playlist_tracks(playlist["playlist_href"])
            return playlist

    def get_playlist_tracks(self,href): #获取每个歌单的歌曲信息
        driver = webdriver.Chrome()
        driver.get(href)
        driver.switch_to.frame("g_iframe")
        tr_list = driver.find_elements_by_xpath("//tbody/tr")
        playlist_tracks = []
        for tr in tr_list:
            track = {}
            track["name"] = tr.find_element_by_xpath("./td[2]//b").get_attribute("title")
            track["duration"] = tr.find_element_by_xpath("./td[3]/span").text
            track["singer"] = tr.find_element_by_xpath("./td[4]/div").get_attribute("title")
            track["album_name"] = tr.find_element_by_xpath("./td[5]//a").get_attribute("title")
            playlist_tracks.append(track)
        driver.quit()
        return playlist_tracks



    def run(self):
        categroy_list = self.get_category_list() #获取分类
        for cate in categroy_list:
            total_playlist_list = self.get_playlist_list(cate,[]) #获取每个分类下的所有播放列表
            print("-"*100)
            print(total_playlist_list)
            print("-"*100)
            for playlist in total_playlist_list:
                print(playlist,"*"*100)
                playlist = self.get_playlist_info(playlist)  #获取每个播放列表下的所有歌曲信息
                print(playlist)

if __name__ == '__main__':
    music_163 = Music163()
    music_163.run()