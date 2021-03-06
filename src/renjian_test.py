#!/usr/bin/python2.6
# coding=UTF8

'''Unit tests for the twitter.py library'''

__author__ = 'Arthur Wang'

import os
import simplejson
import time
import calendar
import unittest

import renjian

class StatusTest(unittest.TestCase):

  SAMPLE_JSON = '''{"all_zt_num": 3, "created_at": "2009-12-24 14:33:01 +0800", "favorited": false, "favoriters": ["asfman", "pippo"], "id": 349507, "in_reply_to_screen_name": "kinki", "in_reply_to_status_id": 349505, "in_reply_to_user_id": 1479, "level": 1, "link_desc": "my fucking blog", "link_title": "Arthraim.cn - programing", "original_url": "http://arthraim.cn/", "relative_date": "1\u5c0f\u65f6\u524d", "root_screen_name": "Arthraim", "root_status_id": 349381, "source": "\u7f51\u7ad9", "status_type": "LINK", "stick": true, "text": "@kinki [:O]", "thumbnail": "http://avatar.renjian.com/1049/120x120_3.jpg", "truncated": false, "user": {"created_at": "2009-08-08 02:22:53 +0800", "description": "\u4e00\u4e2a\u505a\u81ea\u5df1\u559c\u6b22\u505a\u7684\u4e8b\u60c5\u7684\u5c0f\u5c0f\u7a0b\u5e8f\u5458\u2026\u2026", "favourites_count": 103, "followers_count": 217, "following_count": 125, "gender": 1, "id": 1049, "is_followed_me": 0, "is_following": 0, "name": "Arthur", "profile_image_url": "http://avatar.renjian.com/1049/120x120_6.jpg", "protected": false, "score": 5343, "screen_name": "Arthraim", "url": "http://arthraim.cn/"}}'''
  #SAMPLE_JSON = '''{"created_at": "Fri Jan 26 23:17:14 +0000 2007", "id": 4391023, "text": "A l\u00e9gp\u00e1rn\u00e1s haj\u00f3m tele van angoln\u00e1kkal.", "user": {"description": "Canvas. JC Penny. Three ninety-eight.", "id": 718443, "location": "Okinawa, Japan", "name": "Kesuke Miyagi", "profile_image_url": "http://twitter.com/system/user/profile_image/718443/normal/kesuke.png", "screen_name": "kesuke", "url": "http://twitter.com/kesuke"}}'''

  def _GetSampleUser(self):
    return renjian.User(id=1049,
                        name='Arthur',
                        screen_name='Arthraim',
                        description='一个做自己喜欢做的事情的小小程序员……',
                        profile_image_url='http://avatar.renjian.com/1049/120x120_6.jpg',
                        url='http://arthraim.cn/',
                        protected=False,
                        created_at='2009-08-08 02:22:53 +0800',
                        followers_count=217,
                        following_count=125,
                        favourites_count=103,
                        is_followed_me=0,
                        is_following=0,
                        score=5343,
                        gender=1)

  def _GetSampleStatus(self):
    return renjian.Status(id=349507,
                          created_at='2009-12-24 14:33:01 +0800',
                          relative_date='1小时前',
                          text='@kinki [:O]',
                          source='网站',
                          truncated=False,
                          in_reply_to_status_id=349505,
                          in_reply_to_user_id=1479,
                          in_reply_to_screen_name='kinki',
                          favorited=False,
                          original_url='http://arthraim.cn/',
                          status_type='LINK',
                          link_title='Arthraim.cn - programing',
                          link_desc='my fucking blog',
                          thumbnail='http://avatar.renjian.com/1049/120x120_3.jpg',
                          level=1,
                          root_screen_name='Arthraim',
                          root_status_id=349381,
                          all_zt_num=3,
                          stick=True,
                          favoriters=['asfman','pippo'],
                          user=self._GetSampleUser())

  def testInit(self):
    '''Test the renjian.Status constructor'''
    status = renjian.Status(id=349507,
                          created_at='2009-12-24 14:33:01 +0800',
                          relative_date='1小时前',
                          text='@kinki [:O]',
                          source='网站',
                          truncated=False,
                          in_reply_to_status_id=349505,
                          in_reply_to_user_id=1479,
                          in_reply_to_screen_name='kinki',
                          favorited=False,
                          original_url='http://arthraim.cn/',
                          status_type='LINK',
                          link_title='Arthraim.cn - programing',
                          link_desc='my fucking blog',
                          thumbnail='http://avatar.renjian.com/1049/120x120_3.jpg',
                          level=1,
                          root_screen_name='Arthraim',
                          root_status_id=349381,
                          all_zt_num=3,
                          stick=True,
                          favoriters=['asfman','pippo'],
                          user=self._GetSampleUser())

  def testGettersAndSetters(self):
    '''Test all of the renjian.Status getters and setters'''
    status = renjian.Status()
    status.SetId(349507)
    self.assertEqual(349507, status.GetId())
    status.SetCreatedAt('2009-12-24 14:33:01 +0800')
    self.assertEqual('2009-12-24 14:33:01 +0800', status.GetCreatedAt())
    status.SetRelativeDate('1小时前')
    self.assertEqual('1小时前', status.GetRelativeDate())
    status.SetText('@kinki [:O]')
    self.assertEqual('@kinki [:O]', status.GetText())
    status.SetSource('网站')
    self.assertEqual('网站', status.GetSource())
    status.SetTruncated('false')
    self.assertEqual('false', status.GetTruncated())
    status.SetInReplyToStatusId(349505)
    self.assertEqual(349505, status.GetInReplyToStatusId())
    status.SetInReplyToUserId(1479)
    self.assertEqual(1479, status.GetInReplyToUserId())
    status.SetInReplyToScreenName('kinki')
    self.assertEqual('kinki', status.GetInReplyToScreenName())
    status.SetFavorited('false')
    self.assertEqual('false', status.GetFavorited())
    status.SetOriginalUrl('http://arthraim.cn/')
    self.assertEqual('http://arthraim.cn/', status.GetOriginalUrl())
    status.SetStatusType('LINK')
    self.assertEqual('LINK', status.GetStatusType())
    status.SetLinkTitle('Arthraim.cn - programing')
    self.assertEqual('Arthraim.cn - programing', status.GetLinkTitle())
    status.SetLinkDesc('my fucking blog')
    self.assertEqual('my fucking blog', status.GetLinkDesc())
    status.SetThumbnail('http://avatar.renjian.com/1049/120x120_3.jpg')
    self.assertEqual('http://avatar.renjian.com/1049/120x120_3.jpg', status.GetThumbnail())
    status.SetLevel(1)
    self.assertEqual(1, status.GetLevel())
    status.SetRootScreenName('Arthraim')
    self.assertEqual('Arthraim', status.GetRootScreenName())
    status.SetRootStatusId(349381)
    self.assertEqual(349381, status.GetRootStatusId())
    status.SetAllZtNum(3)
    self.assertEqual(3, status.GetAllZtNum())
    status.SetStick('true')
    self.assertEqual('true', status.GetStick())
    status.SetFavoriters(['asfman','pippo'])
    self.assertEqual(['asfman','pippo'], status.GetFavoriters())
    status.SetUser(self._GetSampleUser())
    self.assertEqual(1049, status.GetUser().id)

  def testProperties(self):
    '''Test all of the renjian.Status properties'''
    status = renjian.Status()
    status.id = 349507
    self.assertEqual(349507, status.id)
    status.created_at = '2009-12-24 14:33:01 +0800'
    self.assertEqual('2009-12-24 14:33:01 +0800', status.created_at)
    status.relative_date = '1小时前'
    self.assertEqual('1小时前', status.relative_date)
    status.text = '@kinki [:O]'
    self.assertEqual('@kinki [:O]', status.text)
    status.source = '网站'
    self.assertEqual('网站', status.source)
    status.truncated = 'false'
    self.assertEqual('false', status.truncated)
    status.in_reply_to_status_id = 349505
    self.assertEqual(349505, status.in_reply_to_status_id)
    status.in_reply_to_user_id = 1479
    self.assertEqual(1479, status.in_reply_to_user_id)
    status.in_reply_to_screen_name = 'kinki'
    self.assertEqual('kinki', status.in_reply_to_screen_name)
    status.favorited = 'false'
    self.assertEqual('false', status.favorited)
    status.original_url = 'http://arthraim.cn/'
    self.assertEqual('http://arthraim.cn/', status.original_url)
    status.status_type = 'LINK'
    self.assertEqual('LINK', status.status_type)
    status.link_title = 'Arthraim.cn - programing'
    self.assertEqual('Arthraim.cn - programing', status.link_title)
    status.link_desc = 'my fucking blog'
    self.assertEqual('my fucking blog', status.link_desc)
    status.thumbnail = 'http://avatar.renjian.com/1049/120x120_3.jpg'
    self.assertEqual('http://avatar.renjian.com/1049/120x120_3.jpg', status.thumbnail)
    status.level = 1
    self.assertEqual(1, status.level)
    status.root_screen_name = 'Arthraim'
    self.assertEqual('Arthraim', status.root_screen_name)
    status.root_status_id = 349381
    self.assertEqual(349381, status.root_status_id)
    status.all_zt_num = 3
    self.assertEqual(3, status.all_zt_num)
    status.stick = 'true'
    self.assertEqual('true', status.stick)
    status.favoriters = ['asfman','pippo']
    self.assertEqual(['asfman','pippo'], status.favoriters)
    status.user = self._GetSampleUser()
    self.assertEqual(1049, status.user.id)

#  def _ParseDate(self, string):
#    return calendar.timegm(time.strptime(string, '%b %d %H:%M:%S %Y'))
#
#  def testRelativeCreatedAt(self):
#    '''Test various permutations of Status relative_created_at'''
#    status = renjian.Status(created_at='Fri Jan 01 12:00:00 +0000 2007')
#    status.now = self._ParseDate('Jan 01 12:00:00 2007')
#    self.assertEqual('about a second ago', status.relative_created_at)
#    status.now = self._ParseDate('Jan 01 12:00:01 2007')
#    self.assertEqual('about a second ago', status.relative_created_at)
#    status.now = self._ParseDate('Jan 01 12:00:02 2007')
#    self.assertEqual('about 2 seconds ago', status.relative_created_at)
#    status.now = self._ParseDate('Jan 01 12:00:05 2007')
#    self.assertEqual('about 5 seconds ago', status.relative_created_at)
#    status.now = self._ParseDate('Jan 01 12:00:50 2007')
#    self.assertEqual('about a minute ago', status.relative_created_at)
#    status.now = self._ParseDate('Jan 01 12:01:00 2007')
#    self.assertEqual('about a minute ago', status.relative_created_at)
#    status.now = self._ParseDate('Jan 01 12:01:10 2007')
#    self.assertEqual('about a minute ago', status.relative_created_at)
#    status.now = self._ParseDate('Jan 01 12:02:00 2007')
#    self.assertEqual('about 2 minutes ago', status.relative_created_at)
#    status.now = self._ParseDate('Jan 01 12:31:50 2007')
#    self.assertEqual('about 31 minutes ago', status.relative_created_at)
#    status.now = self._ParseDate('Jan 01 12:50:00 2007')
#    self.assertEqual('about an hour ago', status.relative_created_at)
#    status.now = self._ParseDate('Jan 01 13:00:00 2007')
#    self.assertEqual('about an hour ago', status.relative_created_at)
#    status.now = self._ParseDate('Jan 01 13:10:00 2007')
#    self.assertEqual('about an hour ago', status.relative_created_at)
#    status.now = self._ParseDate('Jan 01 14:00:00 2007')
#    self.assertEqual('about 2 hours ago', status.relative_created_at)
#    status.now = self._ParseDate('Jan 01 19:00:00 2007')
#    self.assertEqual('about 7 hours ago', status.relative_created_at)
#    status.now = self._ParseDate('Jan 02 11:30:00 2007')
#    self.assertEqual('about a day ago', status.relative_created_at)
#    status.now = self._ParseDate('Jan 04 12:00:00 2007')
#    self.assertEqual('about 3 days ago', status.relative_created_at)
#    status.now = self._ParseDate('Feb 04 12:00:00 2007')
#    self.assertEqual('about 34 days ago', status.relative_created_at)

  def testAsJsonString(self):
    '''Test the renjian.Status AsJsonString method'''
    self.assertEqual(StatusTest.SAMPLE_JSON, self._GetSampleStatus().AsJsonString())
    # sequence is not same, dictionary will sort the properties

  def testAsDict(self):
    '''Test the renjian.Status AsDict method'''
    status = self._GetSampleStatus()
    data = status.AsDict()
    self.assertEqual(349507, data['id'])
    self.assertEqual('2009-12-24 14:33:01 +0800', data['created_at'])
    self.assertEqual('@kinki [:O]', data['text'])
    self.assertEqual(1049, data['user']['id'])

  def testEq(self):
    '''Test the renjian.Status __eq__ method'''
    status = renjian.Status()
    status.id=349507
    status.created_at='2009-12-24 14:33:01 +0800'
    status.relative_date='1小时前'
    status.text='@kinki [:O]'
    status.source='网站'
    status.truncated=False
    status.in_reply_to_status_id=349505
    status.in_reply_to_user_id=1479
    status.in_reply_to_screen_name='kinki'
    status.favorited=False
    status.original_url='http://arthraim.cn/'
    status.status_type='LINK'
    status.link_title='Arthraim.cn - programing'
    status.link_desc='my fucking blog'
    status.thumbnail='http://avatar.renjian.com/1049/120x120_3.jpg'
    status.level=1
    status.root_screen_name='Arthraim'
    status.root_status_id=349381
    status.all_zt_num=3
    status.stick=True
    status.favoriters=['asfman','pippo']
    status.user=self._GetSampleUser()
    sample = self._GetSampleStatus()
    self.assertEqual(sample.id, status.id)
    self.assertEqual(sample.created_at, status.created_at)
    self.assertEqual(sample.relative_date, status.relative_date)
    self.assertEqual(sample.text, status.text)
    self.assertEqual(sample.source, status.source)
    self.assertEqual(sample.truncated, status.truncated)
    self.assertEqual(sample.in_reply_to_status_id, status.in_reply_to_status_id)
    self.assertEqual(sample.in_reply_to_user_id, status.in_reply_to_user_id)
    self.assertEqual(sample.in_reply_to_screen_name, status.in_reply_to_screen_name)
    self.assertEqual(sample.favorited, status.favorited)
    self.assertEqual(sample.original_url, status.original_url)
    self.assertEqual(sample.status_type, status.status_type)
    self.assertEqual(sample.link_title, status.link_title)
    self.assertEqual(sample.link_desc, status.link_desc)
    self.assertEqual(sample.thumbnail, status.thumbnail)
    self.assertEqual(sample.level, status.level)
    self.assertEqual(sample.root_screen_name, status.root_screen_name)
    self.assertEqual(sample.root_status_id, status.root_status_id)
    self.assertEqual(sample.all_zt_num, status.all_zt_num)
    self.assertEqual(sample.stick, status.stick)
    self.assertEqual(sample.favoriters, status.favoriters)
    self.assertEqual(sample.user.id, status.user.id)
    
  def testNewFromJsonDict(self):
    '''Test the renjian.User NewFromJsonDict method'''
    data = simplejson.loads(StatusTest.SAMPLE_JSON)
    status = renjian.Status.NewFromJsonDict(data)
    self.assertEqual(self._GetSampleStatus(), status)  

class UserTest(unittest.TestCase):

  SAMPLE_JSON = '''{"created_at": "2009-08-08 02:22:53 +0800", "description": "\u4e00\u4e2a\u505a\u81ea\u5df1\u559c\u6b22\u505a\u7684\u4e8b\u60c5\u7684\u5c0f\u5c0f\u7a0b\u5e8f\u5458\u2026\u2026", "favourites_count": 103, "followers_count": 217, "following_count": 125, "gender": 1, "id": 1049, "is_followed_me": 0, "is_following": 0, "name": "Arthur", "profile_image_url": "http://avatar.renjian.com/1049/120x120_6.jpg", "protected": false, "score": 5343, "screen_name": "Arthraim", "url": "http://arthraim.cn/"}'''

  def _GetSampleUser(self):
    return renjian.User(id=1049,
                        name='Arthur',
                        screen_name='Arthraim',
                        description='一个做自己喜欢做的事情的小小程序员……',
                        profile_image_url='http://avatar.renjian.com/1049/120x120_6.jpg',
                        url='http://arthraim.cn/',
                        protected=False,
                        created_at='2009-08-08 02:22:53 +0800',
                        followers_count=217,
                        following_count=125,
                        favourites_count=103,
                        is_followed_me=0,
                        is_following=0,
                        score=5343,
                        gender=1)

  def testInit(self):
    '''Test the renjian.User constructor'''
    user = renjian.User(id=1049,
                        name='Arthur',
                        screen_name='Arthraim',
                        description='一个做自己喜欢做的事情的小小程序员……',
                        profile_image_url='http://avatar.renjian.com/1049/120x120_6.jpg',
                        url='http://arthraim.cn/',
                        protected=False,
                        created_at='2009-08-08 02:22:53 +0800',
                        followers_count=217,
                        following_count=125,
                        favourites_count=103,
                        is_followed_me=0,
                        is_following=0,
                        score=5343,
                        gender=1)

  def testGettersAndSetters(self):
    '''Test all of the renjian.User getters and setters'''
    user = renjian.User()
    user.SetId(1049)
    self.assertEqual(1049, user.GetId())
    user.SetName('Arthur')
    self.assertEqual('Arthur', user.GetName())
    user.SetScreenName('Arthraim')
    self.assertEqual('Arthraim', user.GetScreenName())
    user.SetDescription('一个做自己喜欢做的事情的小小程序员……')
    self.assertEqual('一个做自己喜欢做的事情的小小程序员……', user.GetDescription())
    user.SetProfileImageUrl('http://avatar.renjian.com/1049/120x120_6.jpg')
    self.assertEqual('http://avatar.renjian.com/1049/120x120_6.jpg', user.GetProfileImageUrl())
    user.SetUrl('http://arthraim.cn/')
    self.assertEqual('http://arthraim.cn/', user.GetUrl())
    user.SetProtected('false')
    self.assertEqual('false', user.GetProtected())
    user.SetCreatedAt('2009-08-08 02:22:53 +0800')
    self.assertEqual('2009-08-08 02:22:53 +0800', user.GetCreatedAt())
    user.SetFollowersCount(217)
    self.assertEqual(217, user.GetFollowersCount())
    user.SetFollowingCount(125)
    self.assertEqual(125, user.GetFollowingCount())
    user.SetFavouritesCount(103)
    self.assertEqual(103, user.GetFavouritesCount())
    user.SetIsFollowedMe(0)
    self.assertEqual(0, user.GetIsFollowedMe())
    user.SetIsFollowing(0)
    self.assertEqual(0, user.GetIsFollowing())
    user.SetScore(5343)
    self.assertEqual(5343, user.GetScore())
    user.SetGender(1)
    self.assertEqual(1, user.GetGender())

  def testProperties(self):
    '''Test all of the renjian.User properties'''
    user = renjian.User()
    user.id = 1049
    self.assertEqual(1049, user.id)
    user.name = 'Arthur'
    self.assertEqual('Arthur', user.name)
    user.screenname =  'Arthraim'
    self.assertEqual('Arthraim', user.screenname)
    user.description = '一个做自己喜欢做的事情的小小程序员……'
    self.assertEqual('一个做自己喜欢做的事情的小小程序员……', user.description)
    user.profile_image_url = 'http://avatar.renjian.com/1049/120x120_6.jpg'
    self.assertEqual('http://avatar.renjian.com/1049/120x120_6.jpg', user.profile_image_url)
    user.url = 'http://arthraim.cn/'
    self.assertEqual('http://arthraim.cn/', user.url)
    user.protected = 'false'
    self.assertEqual('false', user.protected)
    user.created_at = '2009-08-08 02:22:53 +0800'
    self.assertEqual('2009-08-08 02:22:53 +0800', user.created_at)
    user.followers_count = 217
    self.assertEqual(217, user.followers_count)
    user.following_count = 125
    self.assertEqual(125, user.following_count)
    user.favourites_count = 103
    self.assertEqual(103, user.favourites_count)
    user.is_followed_me = 0
    self.assertEqual(0, user.is_followed_me)
    user.is_following = 0
    self.assertEqual(0, user.is_followed_me)
    user.score = 5343
    self.assertEqual(5343, user.score)
    user.gender = 1 
    self.assertEqual(1, user.gender)

  def testAsJsonString(self):
    '''Test the renjian.User AsJsonString method'''
    self.assertEqual(UserTest.SAMPLE_JSON,
                     self._GetSampleUser().AsJsonString())

  def testAsDict(self):
    '''Test the renjian.User AsDict method'''
    user = self._GetSampleUser()
    data = user.AsDict()
    self.assertEqual(1049, data['id'])
    self.assertEqual('Arthur', data['name'])
    self.assertEqual('Arthraim', data['screen_name'])
    self.assertEqual('一个做自己喜欢做的事情的小小程序员……', data['description'])
    self.assertEqual('http://avatar.renjian.com/1049/120x120_6.jpg', data['profile_image_url'])
    self.assertEqual('http://arthraim.cn/', data['url'])
    self.assertEqual(False, data['protected'])
    self.assertEqual('2009-08-08 02:22:53 +0800', data['created_at'])
    self.assertEqual(217, data['followers_count'])
    self.assertEqual(125, data['following_count'])
    self.assertEqual(103, data['favourites_count'])
    self.assertEqual(0, data['is_followed_me'])
    self.assertEqual(0, data['is_following'])
    self.assertEqual(5343, data['score'])
    self.assertEqual(1, data['gender'])
    

  def testEq(self):
    '''Test the renjian.User __eq__ method'''
    user = renjian.User()
    user.id=1049,
    user.name='Arthur',
    user.screen_name='Arthraim',
    user.description='一个做自己喜欢做的事情的小小程序员……',
    user.profile_image_url='http://avatar.renjian.com/1049/120x120_6.jpg',
    user.url='http://arthraim.cn/',
    user.protected=False,
    user.created_at='2009-08-08 02:22:53 +0800',
    user.followers_count=217,
    user.following_count=125,
    user.favourites_count=103,
    user.is_followed_me=0,
    user.is_following=0,
    user.score=5343,
    user.gender=1

  def testNewFromJsonDict(self):
    '''Test the renjian.User NewFromJsonDict method'''
    data = simplejson.loads(UserTest.SAMPLE_JSON)
    user = renjian.User.NewFromJsonDict(data)
    self.assertEqual(self._GetSampleUser(), user)

class DirectMessageTest(unittest.TestCase):

  #SAMPLE_JSON = '''{"id": 61159,"sender_id": 97,"recipient_id": 1049,"created_at": "2009-12-07 15:29:13 +0800","sender_screen_name": "rensea","recipient_screen_name": "Arthraim","text": "您顶的帖子四格已被删除","sender": {"id": 97,"name": "人间团队","screen_name": "renjian","description": "我们是人间团队！","profile_image_url": "http://avatar.renjian.com/97/120x120_1.jpg","url": "","protected": false,"created_at": "2009-07-01 17:46:32 +0800","followers_count": 4776,"following_count": 0,"favourites_count": 17,"is_followed_me": 0,"is_following": 1,"score": 9874,"gender": 0},"recipient": {"id": 1049,"name": "Arthur","screen_name": "Arthraim","description": "一个做自己喜欢做的事情的小小程序员……","profile_image_url": "http://avatar.renjian.com/1049/120x120_7.jpg","url": "http://arthraim.cn/","protected": false,"created_at": "2009-08-08 02:22:53 +0800","followers_count": 228,"following_count": 129,"favourites_count": 106,"is_followed_me": 0,"is_following": 0,"score": 5628,"gender": 1}}'''
  SAMPLE_JSON = '''{"created_at": "2009-08-08 02:22:53 +0800", "id": 61159, "recipient": {"created_at": "2009-08-08 02:22:53 +0800", "description": "\\u4e00\\u4e2a\\u505a\\u81ea\\u5df1\\u559c\\u6b22\\u505a\\u7684\\u4e8b\\u60c5\\u7684\\u5c0f\\u5c0f\\u7a0b\\u5e8f\\u5458\\u2026\\u2026", "favourites_count": 103, "followers_count": 217, "following_count": 125, "gender": 1, "id": 1049, "is_followed_me": 0, "is_following": 0, "name": "Arthur", "profile_image_url": "http://avatar.renjian.com/1049/120x120_6.jpg", "protected": false, "score": 5343, "screen_name": "Arthraim", "url": "http://arthraim.cn/"}, "recipient_id": 1049, "recipient_screen_name": "Arthraim", "sender": {"created_at": "2009-07-01 17:46:32 +0800", "description": "\\u6211\\u4eec\\u662f\\u4eba\\u95f4\\u56e2\\u961f\\uff01", "favourites_count": 17, "followers_count": 4775, "following_count": 0, "gender": 0, "id": 97, "is_followed_me": 0, "is_following": 1, "name": "\\u4eba\\u95f4\\u56e2\\u961f", "profile_image_url": "http://avatar.renjian.com/97/120x120_1.jpg", "protected": false, "score": 9874, "screen_name": "renjian", "url": "http://renjian.com/"}, "sender_id": 97, "sender_screen_name": "rensea", "text": "\\u60a8\\u9876\\u7684\\u5e16\\u5b50\\u56db\\u683c\\u5df2\\u88ab\\u5220\\u9664"}'''

  def _GetSampleDirectMessage(self):
    return renjian.DirectMessage(id=61159,
                                 created_at='2009-08-08 02:22:53 +0800',
                                 sender_id=97,
                                 sender_screen_name='rensea',
                                 recipient_id=1049,
                                 recipient_screen_name='Arthraim',
                                 text='您顶的帖子四格已被删除',
                                 sender=self._GetSampleSender(),
                                 recipient=self._GetSampleRecipient())
    
  def _GetSampleSender(self):
    return renjian.User(id=97,
                        name='人间团队',
                        screen_name='renjian',
                        description='我们是人间团队！',
                        profile_image_url='http://avatar.renjian.com/97/120x120_1.jpg',
                        url='http://renjian.com/',
                        protected=False,
                        created_at='2009-07-01 17:46:32 +0800',
                        followers_count=4775,
                        following_count=0,
                        favourites_count=17,
                        is_followed_me=0,
                        is_following=1,
                        score=9874,
                        gender=0)  
  
  def _GetSampleRecipient(self):
    return renjian.User(id=1049,
                        name='Arthur',
                        screen_name='Arthraim',
                        description='一个做自己喜欢做的事情的小小程序员……',
                        profile_image_url='http://avatar.renjian.com/1049/120x120_6.jpg',
                        url='http://arthraim.cn/',
                        protected=False,
                        created_at='2009-08-08 02:22:53 +0800',
                        followers_count=217,
                        following_count=125,
                        favourites_count=103,
                        is_followed_me=0,
                        is_following=0,
                        score=5343,
                        gender=1)  

  def testInit(self):
    '''Test the renjian.DirectMessage constructor'''
    user = renjian.DirectMessage(id=61159,
                                 created_at='2009-08-08 02:22:53 +0800',
                                 sender_id=97,
                                 sender_screen_name='rensea',
                                 recipient_id=1049,
                                 recipient_screen_name='Arthraim',
                                 text='您顶的帖子四格已被删除',
                                 sender=self._GetSampleSender(),
                                 recipient=self._GetSampleRecipient())
    
  def testGettersAndSetters(self):
    '''Test all of the renjian.DirectMessage getters and setters'''
    directMessage = renjian.DirectMessage()
    directMessage.SetId(61159)
    self.assertEqual(61159, directMessage.GetId())
    directMessage.SetCreatedAt('2009-08-08 02:22:53 +0800')
    self.assertEqual('2009-08-08 02:22:53 +0800', directMessage.GetCreatedAt())
    directMessage.SetSenderId(97)
    self.assertEqual(97, directMessage.GetSenderId())
    directMessage.SetSenderScreenName('rensea')
    self.assertEqual('rensea', directMessage.GetSenderScreenName())
    directMessage.SetRecipientId(1049)
    self.assertEqual(1049, directMessage.GetRecipientId())
    directMessage.SetRecipientScreenName('Arthraim')
    self.assertEqual('Arthraim', directMessage.GetRecipientScreenName())
    directMessage.SetText('您顶的帖子四格已被删除')
    self.assertEqual('您顶的帖子四格已被删除', directMessage.GetText())
    directMessage.SetSender(self._GetSampleSender())
    self.assertEqual(self._GetSampleSender(), directMessage.GetSender())
    directMessage.SetRecipient(self._GetSampleRecipient())
    self.assertEqual(self._GetSampleRecipient(), directMessage.GetRecipient())
    
  def testProperties(self):
    '''Test all of the renjian.DirectMessage properties'''
    directMessage = renjian.DirectMessage()
    directMessage.id = 61159
    self.assertEqual(61159, directMessage.id)
    directMessage.created_at = '2009-08-08 02:22:53 +0800'
    self.assertEqual('2009-08-08 02:22:53 +0800', directMessage.created_at)
    directMessage.sender_id  = 97
    self.assertEqual(97, directMessage.sender_id)
    directMessage.sender_screen_name = 'rensea'
    self.assertEqual('rensea', directMessage.sender_screen_name)
    directMessage.recipient_id = 1049
    self.assertEqual(1049, directMessage.recipient_id)
    directMessage.recipient_screen_name = 'Arthraim'
    self.assertEqual('Arthraim', directMessage.recipient_screen_name)
    directMessage.text = '您顶的帖子四格已被删除'
    self.assertEqual('您顶的帖子四格已被删除', directMessage.text)
    directMessage.sender = self._GetSampleSender()
    self.assertEqual(self._GetSampleSender(), directMessage.sender)
    directMessage.recipient = self._GetSampleRecipient()
    self.assertEqual(self._GetSampleRecipient(), directMessage.recipient)

  def testAsJsonString(self):
    '''Test the renjian.DirectMessage AsJsonString method'''
    self.assertEqual(DirectMessageTest.SAMPLE_JSON,
                     self._GetSampleDirectMessage().AsJsonString())

  def testAsDict(self):
    '''Test the renjian.DirectMessage AsDict method'''
    directMessage = self._GetSampleDirectMessage()
    data = directMessage.AsDict()
    self.assertEqual(61159, data['id'])
    self.assertEqual('2009-08-08 02:22:53 +0800', data['created_at'])
    self.assertEqual(97, data['sender_id'])
    self.assertEqual('rensea', data['sender_screen_name'])
    self.assertEqual(1049, data['recipient_id'])
    self.assertEqual('Arthraim', data['recipient_screen_name'])
    self.assertEqual('您顶的帖子四格已被删除', data['text'])
    self.assertEqual(self._GetSampleSender().id, data['sender']['id'])
    self.assertEqual(self._GetSampleRecipient().id, data['recipient']['id'])
    
  def testEq(self):
    '''Test the renjian.DirectMessage __eq__ method'''
    directMessage = renjian.DirectMessage()
    directMessage.id=61159
    directMessage.created_at='2009-08-08 02:22:53 +0800'
    directMessage.sender_id=97
    directMessage.sender_screen_name='rensea'
    directMessage.recipient_id=1049
    directMessage.recipient_screen_name='Arthraim'
    directMessage.text='您顶的帖子四格已被删除'
    directMessage.sender=self._GetSampleSender()
    directMessage.recipient=self._GetSampleRecipient()

  def testNewFromJsonDict(self):
    '''Test the renjian.DirectMessage NewFromJsonDict method'''
    data = simplejson.loads(DirectMessageTest.SAMPLE_JSON)
    directMessage = renjian.DirectMessage.NewFromJsonDict(data)
    self.assertEqual(self._GetSampleDirectMessage(), directMessage)
    
class ConversationTest(unittest.TestCase):

  SAMPLE_JSON = '''{"id": 363332, "last_status_id": 364076, "owner": {"created_at": "2009-08-08 02:22:53 +0800", "description": "\\u4e00\\u4e2a\\u505a\\u81ea\\u5df1\\u559c\\u6b22\\u505a\\u7684\\u4e8b\\u60c5\\u7684\\u5c0f\\u5c0f\\u7a0b\\u5e8f\\u5458\\u2026\\u2026", "favourites_count": 107, "followers_count": 241, "following_count": 133, "gender": 1, "id": 1049, "is_followed_me": 0, "is_following": 0, "name": "Arthur", "profile_image_url": "http://avatar.renjian.com/1049/120x120_6.jpg", "protected": false, "score": 5671, "screen_name": "Arthraim", "url": "http://arthraim.cn/"}, "text": "\\u539f\\u6765\\u4ee5\\u524d\\u7684\\u4eba\\u95f4\\u7f51\\u662f\\u8fd9\\u6837\\u7684~", "unread_count": 0}'''

  def _GetSampleConversation(self):
    return renjian.Conversation(id=363332,
                                last_status_id=364076,
                                text='原来以前的人间网是这样的~',
                                unread_count=0,
                                owner=self._GetSampleOwner())
    
  def _GetSampleOwner(self):
    return renjian.User(id=1049,
                        name='Arthur',
                        screen_name='Arthraim',
                        description='一个做自己喜欢做的事情的小小程序员……',
                        profile_image_url='http://avatar.renjian.com/1049/120x120_6.jpg',
                        url='http://arthraim.cn/',
                        protected=False,
                        created_at='2009-08-08 02:22:53 +0800',
                        followers_count=241,
                        following_count=133,
                        favourites_count=107,
                        is_followed_me=0,
                        is_following=0,
                        score=5671,
                        gender=1)  

  def testInit(self):
    '''Test the renjian.Conversation constructor'''
    user = renjian.Conversation(id=363332,
                                last_status_id=364076,
                                text='原来以前的人间网是这样的~',
                                unread_count=0,
                                owner=self._GetSampleOwner())

  def testGettersAndSetters(self):
    '''Test all of the renjian.Conversation getters and setters'''
    conversation = renjian.Conversation()
    conversation.SetId(363332)
    self.assertEqual(363332, conversation.GetId())
    conversation.SetLastStatusId(364076)
    self.assertEqual(364076, conversation.GetLastStatusId())
    conversation.SetText('原来以前的人间网是这样的~')
    self.assertEqual('原来以前的人间网是这样的~', conversation.GetText())
    conversation.SetUnreadCount(0)
    self.assertEqual(0, conversation.GetUnreadCount())
    conversation.SetOwner(self._GetSampleOwner())
    self.assertEqual(self._GetSampleOwner(), conversation.GetOwner())
    
  def testProperties(self):
    '''Test all of the renjian.Conversation properties'''
    conversation = renjian.Conversation()
    conversation.id = 363332
    self.assertEqual(363332, conversation.id)
    conversation.last_status_id = 364076
    self.assertEqual(364076, conversation.last_status_id)
    conversation.text = '原来以前的人间网是这样的~'
    self.assertEqual('原来以前的人间网是这样的~', conversation.text)
    conversation.unread_count = 0
    self.assertEqual(0, conversation.unread_count)
    conversation.owner = self._GetSampleOwner()
    self.assertEqual(self._GetSampleOwner(), conversation.owner)

  def testAsJsonString(self):
    '''Test the renjian.Conversation AsJsonString method'''
    self.assertEqual(ConversationTest.SAMPLE_JSON,
                     self._GetSampleConversation().AsJsonString())

  def testAsDict(self):
    '''Test the renjian.Conversation AsDict method'''
    conversation = self._GetSampleConversation()
    data = conversation.AsDict()
    self.assertEqual(363332, data['id'])
    self.assertEqual(364076, data['last_status_id'])
    self.assertEqual('原来以前的人间网是这样的~', data['text'])
    self.assertEqual(0, data['unread_count'])
    self.assertEqual(self._GetSampleOwner().id, data['owner']['id'])
    
  def testEq(self):
    '''Test the renjian.Conversation __eq__ method'''
    directMessage = renjian.Conversation()
    directMessage.id=363332
    directMessage.last_status_id=364076
    directMessage.sender_id=97
    directMessage.text='原来以前的人间网是这样的~'
    directMessage.unread_count=0
    directMessage.owner=self._GetSampleOwner()

  def testNewFromJsonDict(self):
    '''Test the renjian.Conversation NewFromJsonDict method'''
    data = simplejson.loads(ConversationTest.SAMPLE_JSON)
    conversation = renjian.Conversation.NewFromJsonDict(data)
    self.assertEqual(self._GetSampleConversation(), conversation)

class FileCacheTest(unittest.TestCase):

  def testInit(self):
    '''Test the renjian._FileCache constructor'''
    cache = renjian._FileCache()
    self.assert_(cache is not None, 'cache is None')

  def testSet(self):
    '''Test the renjian._FileCache.Set method'''
    cache = renjian._FileCache()
    cache.Set("foo",'Hello World!')
    cache.Remove("foo")

  def testRemove(self):
    '''Test the renjian._FileCache.Remove method'''
    cache = renjian._FileCache()
    cache.Set("foo",'Hello World!')
    cache.Remove("foo")
    data = cache.Get("foo")
    self.assertEqual(data, None, 'data is not None')

  def testGet(self):
    '''Test the renjian._FileCache.Get method'''
    cache = renjian._FileCache()
    cache.Set("foo",'Hello World!')
    data = cache.Get("foo")
    self.assertEqual('Hello World!', data)
    cache.Remove("foo")

  def testGetCachedTime(self):
    '''Test the renjian._FileCache.GetCachedTime method'''
    now = time.time()
    cache = renjian._FileCache()
    cache.Set("foo",'Hello World!')
    cached_time = cache.GetCachedTime("foo")
    delta = cached_time - now
    self.assert_(delta <= 1,
                 'Cached time differs from clock time by more than 1 second.')
    cache.Remove("foo")

class ApiTest(unittest.TestCase):

  def setUp(self):
    self._urllib = MockUrllib()
    api = renjian.Api(username='test', password='test')
    api.SetCache(NullCache())
    api.SetUrllib(self._urllib)
    self._api = api

  def testrenjianError(self):
    '''Test that renjian responses containing an error message are wrapped.'''
    self._AddHandler('http://api.renjian.com/statuses/public_timeline.json',
                     curry(self._OpenTestData, 'public_timeline_error.json'))
    # Manually try/catch so we can check the exception's value
    try:
      statuses = self._api.GetPublicTimeline()
    except renjian.RenjianError, error:
      # If the error message matches, the test passes
      self.assertEqual('test error', error.message)
    else:
      self.fail('renjianError expected')

  def testGetPublicTimeline(self):
    '''Test the renjian.Api GetPublicTimeline method'''
    self._AddHandler('http://api.renjian.com/statuses/public_timeline.json?count=5&max_id=367987&page=1&since_id=300000',
                     curry(self._OpenTestData, 'public_timeline.json'))
    statuses = self._api.GetPublicTimeline(page=1, since_id=300000, max_id=367987, count=5)
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(5, len(statuses))
    self.assertEqual(367986, statuses[0].id)

  def testGetFriendsTimeline(self):
    '''Test the renjian.Api GetFriendsTimeline method'''
    self._AddHandler('http://api.renjian.com/statuses/friends_timeline/arthraim.json?count=5&max_id=368084&page=1&since_id=300000',
                     curry(self._OpenTestData, 'friends_timeline-arthraim.json'))
    statuses = self._api.GetFriendsTimeline(user='arthraim', page=1, since_id=300000, max_id=368084, count=5)
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(5, len(statuses))
    self.assertEqual(1049, statuses[0].user.id)

  def testGetUserTimeline(self):
    '''Test the renjian.Api GetUserTimeline method'''
    self._AddHandler('http://api.renjian.com/statuses/user_timeline/arthraim.json?count=5&max_id=367987&page=1&since_id=300000',
                     curry(self._OpenTestData, 'user_timeline-arthraim.json'))
    statuses = self._api.GetUserTimeline(user='arthraim', page=1, since_id=300000, max_id=367987, count=5)
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(367937, statuses[0].id)
    self.assertEqual(1049, statuses[0].user.id)

  def testGetStatus(self):
    '''Test the renjian.Api GetStatus method'''
    self._AddHandler('http://api.renjian.com/statuses/show/367462.json',
                     curry(self._OpenTestData, 'show-367462.json'))
    status = self._api.GetStatus(367462)
    self.assertEqual(367462, status.id)
    self.assertEqual(1049, status.user.id)

  def testGetMentions(self):
    '''Test the renjian.Api GetMentions method'''
    self._AddHandler('http://api.renjian.com/statuses/mentions.json?count=5&max_id=367795&page=2&since_id=350000',
                     curry(self._OpenTestData, 'mentions.json'))
    statuses = self._api.GetMentions(page=2, since_id=350000, max_id=367795, count=5)
    self.assertEqual(367454, statuses[0].id)

  def testDestroyStatus(self):
    '''Test the renjian.Api DestroyStatus method'''
    self._AddHandler('http://api.renjian.com/statuses/destroy/367462.json',
                     curry(self._OpenTestData, 'status-destroy.json'))
    status = self._api.DestroyStatus(367462)
    self.assertEqual(367462, status.id)

  def testPostText(self):
    '''Test the renjian.Api PostText method'''
    self._AddHandler('http://api.renjian.com/statuses/update.json',
                     curry(self._OpenTestData, 'post-text.json'))
    status = self._api.PostText(text=u'Arthraim在测试代码', in_reply_to_status_id=350000)
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(u'Arthraim在测试代码', status.text)
    self.assertEqual(350000, status.in_reply_to_status_id)
    
  def testPostLink(self):
    '''Test the renjian.Api PostLink method'''
    self._AddHandler('http://api.renjian.com/statuses/update.json',
                     curry(self._OpenTestData, 'post-link.json'))
    status = self._api.PostLink(text=u'测试连接', 
                                original_url=u'http://g.cn/',
                                in_reply_to_status_id=350000,
                                link_title=u'Google',
                                link_desc=u'')
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(u'测试连接', status.text)
    self.assertEqual(None, status.in_reply_to_status_id)

  def testGetFollowings(self):
    '''Test the renjian.Api GetFollowings method'''
    self._AddHandler('http://api.renjian.com/statuses/followings/arthraim.json',
                     curry(self._OpenTestData, 'followings.json'))
    users = self._api.GetFollowings(user='arthraim')
    self.assertEqual(5195, users[0].id)

  def testGetFollowers(self):
    '''Test the renjian.Api GetFollowers method'''
    self._AddHandler('http://api.renjian.com/statuses/followers/arthraim.json',
                     curry(self._OpenTestData, 'followers.json'))
    users = self._api.GetFollowers(user='arthraim')
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(1364, users[0].id)
    
#
#  def testGetFeatured(self):
#    '''Test the renjian.Api GetFeatured method'''
#    self._AddHandler('http://renjian.com/statuses/featured.json',
#                     curry(self._OpenTestData, 'featured.json'))
#    users = self._api.GetFeatured()
#    # This is rather arbitrary, but spot checking is better than nothing
#    stevenwright = [u.status for u in users if u.screen_name == 'stevenwright']
#    self.assertEqual(86991742, stevenwright[0].id)

  def testGetUser(self):
    '''Test the renjian.Api GetUser method'''
    self._AddHandler('http://api.renjian.com/users/show/arthraim.json',
                     curry(self._OpenTestData, 'show-arthraim.json'))
    user = self._api.GetUser(user='arthraim')
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(1049, user.id)

  def testGetDirectMessages(self):
    '''Test the renjian.Api GetDirectMessages method'''
    self._AddHandler('http://api.renjian.com/direct_messages/receive.json?count=1&page=1&since_id=96765',
                     curry(self._OpenTestData, 'direct_messages_receive.json'))
    statuses = self._api.GetDirectMessages(count=1, since_id=96765, page=1)
    print(statuses[0].text)
    self.assertEqual(u"您的帖子已被删除:@wangc 同学的博文cnnbboy's Dream » 人间 ＝＝ 围脖？？NO，人间＝＝ 微社区 ", statuses[0].text)
    
  def testGetDirectMessagesSent(self):
    '''Test the renjian.Api GetDirectMessages method'''
    self._AddHandler('http://api.renjian.com/direct_messages/sent.json?count=1&page=1&since_id=89714',
                     curry(self._OpenTestData, 'direct_messages_sent.json'))
    statuses = self._api.GetDirectMessagesSent(count=1, since_id=89714, page=1)
    print(statuses[0].text)
    self.assertEqual(u"今天天气不错…………", statuses[0].text)
    

  def testPostDirectMessage(self):
    '''Test the renjian.Api PostDirectMessage method'''
    self._AddHandler('http://api.renjian.com/direct_messages/new.json',
                     curry(self._OpenTestData, 'direct_messages-new.json'))
    status = self._api.PostDirectMessage(user='rubyQ', text=u'今天天气不错…………')
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(u'今天天气不错…………', status.text)

  def testDestroyDirectMessage(self):
    '''Test the renjian.Api DestroyDirectMessage method'''
    self._AddHandler('http://api.renjian.com/direct_messages/destroy/96766.json',
                     curry(self._OpenTestData, 'direct_message-destroy.json'))
    status = self._api.DestroyDirectMessage(96766)
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(1049, status.sender_id)

  def testCreateFriendship(self):
    '''Test the renjian.Api CreateFriendship method'''
    self._AddHandler('http://api.renjian.com/friendships/create.json',
                     curry(self._OpenTestData, 'friendship-create.json'))
    user = self._api.CreateFriendship(user='renjian')
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(1049, user.id)

  def testDestroyFriendship(self):
    '''Test the renjian.Api DestroyFriendship method'''
    self._AddHandler('http://api.renjian.com/friendships/destroy.json',
                     curry(self._OpenTestData, 'friendship-destroy.json'))
    user = self._api.DestroyFriendship(user='renjian')
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(1049, user.id)
    
  def testExistFriendship(self):
    '''Test the renjian.Api ExistFriendship method'''
    self._AddHandler('http://api.renjian.com/friendships/exists.json?user_b=3&user_a=2', 
                     curry(self._OpenTestData, 'friendship-exist.json'))
    result = self._api.ExistFriendship(user_a='2', user_b='3')
    self.assertEqual(True, result)
    
  def testGetFollowingIds(self):
    '''Test the renjian.Api GetFollowingIds method'''
    self._AddHandler('http://api.renjian.com/followings/ids.json?id=1049', 
                     curry(self._OpenTestData, 'following_ids.json'))
    result = self._api.GetFollowingIds(id='1049')
    self.assertEqual(5195, result[0])
    
  def testGetFollowerIds(self):
    '''Test the renjian.Api GetFollowerIds method'''
    self._AddHandler('http://api.renjian.com/followers/ids.json?id=1049', 
                     curry(self._OpenTestData, 'follower_ids.json'))
    result = self._api.GetFollowerIds(id='1049')
    self.assertEqual(5728, result[0])
    
  def testGetFavorites(self):
    '''Test the renjian.Api GetPublicTimeline method'''
    self._AddHandler('http://api.renjian.com/favorites/list.json?page=2',
                     curry(self._OpenTestData, 'favorites_list.json'))
    statuses = self._api.GetFavorites(page=2)
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(20, len(statuses))
    self.assertEqual(350069, statuses[0].id)
    
  def testCreateFavorite(self):
    '''test the renjian.Api CreateFavorite method'''
    self._AddHandler('http://api.renjian.com/favorites/create/367434.json', 
                     curry(self._OpenTestData, 'favorite-status.json'))
    result = self._api.CreateFavorite(status_id='367434')
    self.assertEqual(367434, result.id)
    
  def testDestroyFavorite(self):
    '''test the renjian.Api CreateFavorite method'''
    self._AddHandler('http://api.renjian.com/favorites/destroy/367434.json', 
                     curry(self._OpenTestData, 'favorite-status.json'))
    result = self._api.DestroyFavorite(status_id='367434')
    self.assertEqual(367434, result.id)
    
  def testUpdateUserProfile(self):
    '''test the renjian.Api UpdateUserProfile method'''
    self._AddHandler('http://api.renjian.com/account/update_profile.json', 
                     curry(self._OpenTestData, 'show-arthraim.json'))
    user = self._api.UpdateUserProfile(nickname='Arthur',
                                       username='arthraim', 
                                       location='China', 
                                       email='arthraim@gmail.com', 
                                       url='http://arthraim.cn/',
                                       description="一个做自己喜欢做的事情的小小程序员……")
    self.assertEqual(1049, user.id)
    self.assertEqual('Arthur', user.name)
    self.assertEqual('Arthraim', user.screen_name)
    self.assertEqual('一个做自己喜欢做的事情的小小程序员……', user.description)
    
  def testBlockUser(self):
    '''test the renjian.Api BlockUser method'''
    self._AddHandler('http://api.renjian.com/blocks/create.json', 
                     curry(self._OpenTestData, 'show-arthraim.json'))
    user = self._api.BlockUser(id='1049')
    self.assertEqual(1049, user.id)
    
  def testUnblockUser(self):
    '''test the renjian.Api UnblockUser method'''
    self._AddHandler('http://api.renjian.com/blocks/destory.json', 
                     curry(self._OpenTestData, 'show-arthraim.json'))
    user = self._api.UnblockUser(id='1049')
    self.assertEqual(1049, user.id)
    
  def testGetMyConversations(self):
    '''test the renjian.Api GetMyConversations method'''
    self._AddHandler('http://api.renjian.com/conversations/my_conversations.json?count=3&page=1&since_id=150000', 
                     curry(self._OpenTestData, 'my_conversations.json'))
    conversations = self._api.GetMyConversations(since_id=150000, count=3, page=1)
    self.assertEqual(5, len(conversations))
    self.assertEqual(360447, conversations[0].id)
    
  def testGetConversationByStatusId(self):
    '''Test the renjian.Api GetConversationByStatusId method'''
    self._AddHandler('http://api.renjian.com/conversations/show_by_status.json?count=5&id=360512&since_id=360512&page=1',
                     curry(self._OpenTestData, 'conversation-show_by_status.json'))
    statuses = self._api.GetConversationByStatusId(id='360512', page=1, since_id=360512, count=5, show_all=False)
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(360516, statuses[0].id)
    self.assertEqual(1049, statuses[0].user.id)
    
  def testGetConversationByConversationId(self):
    '''Test the renjian.Api GetConversationByConversationId method'''
    self._AddHandler('http://api.renjian.com/conversations/statuses.json?count=5&id=360447&since_id=360512&page=1',
                     curry(self._OpenTestData, 'conversation-by_conversation_id.json'))
    statuses = self._api.GetConversationByConversationId(id='360447', page=1, since_id=360512, count=5, show_all=False)
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(360516, statuses[0].id)
    self.assertEqual(1049, statuses[0].user.id)
      
# TODO: add test code

  def _AddHandler(self, url, callback):
    self._urllib.AddHandler(url, callback)

  def _GetTestDataPath(self, filename):
    directory = os.path.dirname(os.path.abspath(__file__))
    test_data_dir = os.path.join(directory, 'testdata')
    return os.path.join(test_data_dir, filename)

  def _OpenTestData(self, filename):
    return open(self._GetTestDataPath(filename))

class MockUrllib(object):
  '''A mock replacement for urllib that hardcodes specific responses.'''

  def __init__(self):
    self._handlers = {}
    self.HTTPBasicAuthHandler = MockHTTPBasicAuthHandler

  def AddHandler(self, url, callback):
    self._handlers[url] = callback

  def build_opener(self, *handlers):
    return MockOpener(self._handlers)

class MockOpener(object):
  '''A mock opener for urllib'''

  def __init__(self, handlers):
    self._handlers = handlers
    self._opened = False

  def open(self, url, data=None):
    if self._opened:
      raise Exception('MockOpener already opened.')
    if url in self._handlers:
      self._opened = True
      return self._handlers[url]()
    else:
      raise Exception('Unexpected URL %s' % url)

  def close(self):
    if not self._opened:
      raise Exception('MockOpener closed before it was opened.')
    self._opened = False

class MockHTTPBasicAuthHandler(object):
  '''A mock replacement for HTTPBasicAuthHandler'''

  def add_password(self, realm, uri, user, passwd):
    # TODO(dewitt): Add verification that the proper args are passed
    pass


class NullCache(object):
  '''A no-op replacement for the cache class'''

  def Get(self, key):
    return None

  def Set(self, key, data):
    pass

  def Remove(self, key):
    pass

  def GetCachedTime(self, key):
    return None


class curry:
  # http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52549

  def __init__(self, fun, *args, **kwargs):
    self.fun = fun
    self.pending = args[:]
    self.kwargs = kwargs.copy()

  def __call__(self, *args, **kwargs):
    if kwargs and self.kwargs:
      kw = self.kwargs.copy()
      kw.update(kwargs)
    else:
      kw = kwargs or self.kwargs
    return self.fun(*(self.pending + args), **kw)


def suite():
  suite = unittest.TestSuite()
  suite.addTests(unittest.makeSuite(FileCacheTest))
  suite.addTests(unittest.makeSuite(StatusTest))
  suite.addTests(unittest.makeSuite(UserTest))
  suite.addTests(unittest.makeSuite(ApiTest))
  return suite
  

if __name__ == '__main__':
  unittest.main()
