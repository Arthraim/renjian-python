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

  SAMPLE_JSON = u'''{"id": 349615,"created_at": "2009-12-24 15:20:17 +0800","relative_date": "13分钟前","text": "","source": "网站","truncated": false,"favorited": false,"original_url": "http://img1.renjian.com/2009/12/4745/47efa3d5bedbe2662380ebca6709e8f5_1261639217539_357x423.jpeg","status_type": "PICTURE","link_title": "","link_desc": "","thumbnail": "http://img1.renjian.com/2009/12/4745/47efa3d5bedbe2662380ebca6709e8f5_1261639217539_357x423small.jpeg","link_url": "http://img1.renjian.com/2009/12/4745/47efa3d5bedbe2662380ebca6709e8f5_1261639217539_357x423small.jpeg","level": 1,"all_zt_num": 0,"stick": true,"favoriters": ["asfman"],"user": {"id": 4745,"name": "Kazira","screen_name": "Kazira","description": "品味现实主义烈酒.","profile_image_url": "http://avatar.renjian.com/4745/120x120_6.jpg","url": "http://www.kazira.net","protected": false,"created_at": "2009-12-22 16:47:24 +0800","followers_count": 58,"following_count": 139,"favourites_count": 4,"is_followed_me": 0,"is_following": 0,"score": 230,"gender": 1}},{"id": 349662,"created_at": "2009-12-24 15:31:53 +0800","relative_date": "1分钟前","text": "@renjian :P","source": "网站","truncated": false,"in_reply_to_status_id": 349657,"in_reply_to_user_id": 97,"in_reply_to_screen_name": "renjian","favorited": false,"original_url": "","status_type": "TEXT","link_title": "","link_desc": "","level": 1,"root_screen_name": "renjian","root_status_id": 349657,"all_zt_num": 1,"stick": true,"favoriters": [],"user": {"id": 1479,"name": "kinki喵呜","screen_name": "kinki","description": "吃喝嫖賭抽 坑蒙拐騙偷","profile_image_url": "http://avatar.renjian.com/1479/120x120_12.jpg","url": "","protected": false,"created_at": "2009-08-23 17:58:07 +0800","followers_count": 241,"following_count": 300,"favourites_count": 78,"is_followed_me": 1,"is_following": 1,"score": 1475,"gender": 0}},{"id": 346307,"created_at": "2009-12-23 18:29:59 +0800","relative_date": "21小时前","text": "快来看push","source": "书签","truncated": false,"favorited": false,"original_url": "http://www.javaeye.com/news/12565","status_type": "LINK","link_title": "CometD 1.0发布，基于Ajax push技术的事件路由总线程序 - Web前端 - JavaEye新闻","link_desc": "CometD 1.0发布，基于Ajax push技术的事件路由总线程序 - Web前端 - JavaEye新闻","thumbnail": "http://img1.renjian.com/2009/12/downloadImg/-21271860521261564199629.png","link_url": "http://img1.renjian.com/2009/12/downloadImg/-21271860521261564199629.png","level": 1,"root_status_id": 346307,"all_zt_num": 2,"stick": true,"favoriters": ["pippo"],"user": {"id": 1049,"name": "Arthur","screen_name": "Arthraim","description": "一个做自己喜欢做的事情的小小程序员……","profile_image_url": "http://avatar.renjian.com/1049/120x120_6.jpg","url": "http://arthraim.cn/","protected": false,"created_at": "2009-08-08 02:22:53 +0800","followers_count": 217,"following_count": 125,"favourites_count": 103,"is_followed_me": 0,"is_following": 0,"score": 5343,"gender": 1}}'''

  def _GetSampleUser(self):
    return renjian.User(id=4745,
                        name='Kazira',
                        screen_name='Kazira',
                        description=u'品味现实主义烈酒.',
                        profile_image_url='http://avatar.renjian.com/4745/120x120_6.jpg',
                        url='http://www.kazira.net',
                        protected='false',
                        created_at='2009-12-22 16:47:24 +0800',
                        followers_count=58,
                        following_count=139,
                        favourites_count=4,
                        is_followed_me=0,
                        is_following=0,
                        score=230,
                        gender=1)

  def _GetSampleStatus(self):
    return renjian.Status(id=349615,
                          created_at='2009-12-24 15:20:17 +0800',
                          relative_date='13分钟前',
                          text='say something',
                          source='网站',
                          truncated='false',
                          favorited='false',
                          original_url='http://img1.renjian.com/2009/12/4745/47efa3d5bedbe2662380ebca6709e8f5_1261639217539_357x423.jpeg',
                          status_type='PICTURE',
                          link_title=None,
                          link_desc=None,
                          thumbnail='http://img1.renjian.com/2009/12/4745/47efa3d5bedbe2662380ebca6709e8f5_1261639217539_357x423small.jpeg',
                          link_url='http://img1.renjian.com/2009/12/4745/47efa3d5bedbe2662380ebca6709e8f5_1261639217539_357x423small.jpeg',
                          level=1,
                          root_status_id=349615,
                          all_zt_num=1,
                          stick='true',
                          favoriters=['asfman'],
                          user=self._GetSampleUser())

  def testInit(self):
    '''Test the renjian.Status constructor'''
    status = renjian.Status(id=349615,
                          created_at='2009-12-24 15:47:56 +0800',
                          relative_date='13分钟前',
                          text='say something',
                          source='网站',
                          truncated='false',
                          favorited='false',
                          original_url='http://img1.renjian.com/2009/12/4745/47efa3d5bedbe2662380ebca6709e8f5_1261639217539_357x423.jpeg',
                          status_type='PICTURE',
                          link_title=u'随便叽歪几句中文',
                          link_desc=u'继续叽歪',
                          thumbnail='http://img1.renjian.com/2009/12/4745/47efa3d5bedbe2662380ebca6709e8f5_1261639217539_357x423small.jpeg',
                          link_url='http://img1.renjian.com/2009/12/4745/47efa3d5bedbe2662380ebca6709e8f5_1261639217539_357x423small.jpeg',
                          level=1,
                          root_status_id=349615,
                          all_zt_num=1,
                          stick='true',
                          favoriters=['asfman','arthraim'],
                          user=self._GetSampleUser())

  def testGettersAndSetters(self):
    '''Test all of the renjian.Status getters and setters'''
    status = renjian.Status()
    status.SetId(4391023)
    self.assertEqual(4391023, status.GetId())
    created_at = calendar.timegm((2007, 1, 26, 23, 17, 14, -1, -1, -1))
    status.SetCreatedAt('2009-12-24 15:47:56 +0800')
    self.assertEqual('2009-12-24 15:47:56 +0800', status.GetCreatedAt())
    self.assertEqual(created_at, status.GetCreatedAtInSeconds())
    status.SetNow(created_at + 10)
    self.assertEqual("about 10 seconds ago", status.GetRelativeCreatedAt())
    status.SetText(u'asdfasfdasdfasdfsad')
    self.assertEqual(u'asdf.',
                     status.GetText())
    status.SetUser(self._GetSampleUser())
    self.assertEqual(718443, status.GetUser().id)

  def testProperties(self):
    '''Test all of the renjian.Status properties'''
    status = renjian.Status()
    status.id = 1
    self.assertEqual(1, status.id)
    created_at = calendar.timegm((2007, 1, 26, 23, 17, 14, -1, -1, -1))
    status.created_at = 'Fri Jan 26 23:17:14 +0000 2007'
    self.assertEqual('Fri Jan 26 23:17:14 +0000 2007', status.created_at)
    self.assertEqual(created_at, status.created_at_in_seconds)
    status.now = created_at + 10
    self.assertEqual('about 10 seconds ago', status.relative_created_at)
    status.user = self._GetSampleUser()
    self.assertEqual(718443, status.user.id)

  def _ParseDate(self, string):
    return calendar.timegm(time.strptime(string, '%b %d %H:%M:%S %Y'))

  def testRelativeCreatedAt(self):
    '''Test various permutations of Status relative_created_at'''
    status = renjian.Status(created_at='Fri Jan 01 12:00:00 +0000 2007')
    status.now = self._ParseDate('Jan 01 12:00:00 2007')
    self.assertEqual('about a second ago', status.relative_created_at)
    status.now = self._ParseDate('Jan 01 12:00:01 2007')
    self.assertEqual('about a second ago', status.relative_created_at)
    status.now = self._ParseDate('Jan 01 12:00:02 2007')
    self.assertEqual('about 2 seconds ago', status.relative_created_at)
    status.now = self._ParseDate('Jan 01 12:00:05 2007')
    self.assertEqual('about 5 seconds ago', status.relative_created_at)
    status.now = self._ParseDate('Jan 01 12:00:50 2007')
    self.assertEqual('about a minute ago', status.relative_created_at)
    status.now = self._ParseDate('Jan 01 12:01:00 2007')
    self.assertEqual('about a minute ago', status.relative_created_at)
    status.now = self._ParseDate('Jan 01 12:01:10 2007')
    self.assertEqual('about a minute ago', status.relative_created_at)
    status.now = self._ParseDate('Jan 01 12:02:00 2007')
    self.assertEqual('about 2 minutes ago', status.relative_created_at)
    status.now = self._ParseDate('Jan 01 12:31:50 2007')
    self.assertEqual('about 31 minutes ago', status.relative_created_at)
    status.now = self._ParseDate('Jan 01 12:50:00 2007')
    self.assertEqual('about an hour ago', status.relative_created_at)
    status.now = self._ParseDate('Jan 01 13:00:00 2007')
    self.assertEqual('about an hour ago', status.relative_created_at)
    status.now = self._ParseDate('Jan 01 13:10:00 2007')
    self.assertEqual('about an hour ago', status.relative_created_at)
    status.now = self._ParseDate('Jan 01 14:00:00 2007')
    self.assertEqual('about 2 hours ago', status.relative_created_at)
    status.now = self._ParseDate('Jan 01 19:00:00 2007')
    self.assertEqual('about 7 hours ago', status.relative_created_at)
    status.now = self._ParseDate('Jan 02 11:30:00 2007')
    self.assertEqual('about a day ago', status.relative_created_at)
    status.now = self._ParseDate('Jan 04 12:00:00 2007')
    self.assertEqual('about 3 days ago', status.relative_created_at)
    status.now = self._ParseDate('Feb 04 12:00:00 2007')
    self.assertEqual('about 34 days ago', status.relative_created_at)

  def testAsJsonString(self):
    '''Test the renjian.Status AsJsonString method'''
    self.assertEqual(StatusTest.SAMPLE_JSON,
                     self._GetSampleStatus().AsJsonString())

  def testAsDict(self):
    '''Test the renjian.Status AsDict method'''
    status = self._GetSampleStatus()
    data = status.AsDict()
    self.assertEqual(4391023, data['id'])
    self.assertEqual('Fri Jan 26 23:17:14 +0000 2007', data['created_at'])
    self.assertEqual(u'asdfasdfs.', data['text'])
    self.assertEqual(718443, data['user']['id'])

  def testEq(self):
    '''Test the renjian.Status __eq__ method'''
    status = renjian.Status()
    status.created_at = 'Fri Jan 26 23:17:14 +0000 2007'
    status.id = 4391023
    status.text = u'df'
    status.user = self._GetSampleUser()
    self.assertEqual(status, self._GetSampleStatus())

  def testNewFromJsonDict(self):
    '''Test the renjian.Status NewFromJsonDict method'''
    data = simplejson.loads(StatusTest.SAMPLE_JSON)
    status = renjian.Status.NewFromJsonDict(data)
    self.assertEqual(self._GetSampleStatus(), status)
"""
class UserTest(unittest.TestCase):

  SAMPLE_JSON = '''{"description": "Indeterminate things", "id": 673483, "location": "San Francisco, CA", "name": "DeWitt", "profile_image_url": "http://renjian.com/system/user/profile_image/673483/normal/me.jpg", "screen_name": "dewitt", "status": {"created_at": "Fri Jan 26 17:28:19 +0000 2007", "id": 4212713, "text": "\\"Select all\\" and archive your Gmail inbox.  The page loads so much faster!"}, "url": "http://unto.net/"}'''

  def _GetSampleStatus(self):
    return renjian.Status(created_at='Fri Jan 26 17:28:19 +0000 2007',
                          id=4212713,
                          text='"Select all" and archive your Gmail inbox. '
                               ' The page loads so much faster!')

  def _GetSampleUser(self):
    return renjian.User(id=673483,
                        name='DeWitt',
                        screen_name='dewitt',
                        description=u'Indeterminate things',
                        location='San Francisco, CA',
                        url='http://unto.net/',
                        profile_image_url='http://renjian.com/system/user/prof'
                                          'ile_image/673483/normal/me.jpg',
                        status=self._GetSampleStatus())



  def testInit(self):
    '''Test the renjian.User constructor'''
    user = renjian.User(id=673483,
                        name='DeWitt',
                        screen_name='dewitt',
                        description=u'Indeterminate things',
                        url='http://renjian.com/dewitt',
                        profile_image_url='http://renjian.com/system/user/prof'
                                          'ile_image/673483/normal/me.jpg',
                        status=self._GetSampleStatus())

  def testGettersAndSetters(self):
    '''Test all of the renjian.User getters and setters'''
    user = renjian.User()
    user.SetId(673483)
    self.assertEqual(673483, user.GetId())
    user.SetName('DeWitt')
    self.assertEqual('DeWitt', user.GetName())
    user.SetScreenName('dewitt')
    self.assertEqual('dewitt', user.GetScreenName())
    user.SetDescription('Indeterminate things')
    self.assertEqual('Indeterminate things', user.GetDescription())
    user.SetLocation('San Francisco, CA')
    self.assertEqual('San Francisco, CA', user.GetLocation())
    user.SetProfileImageUrl('http://renjian.com/system/user/profile_im'
                            'age/673483/normal/me.jpg')
    self.assertEqual('http://renjian.com/system/user/profile_image/673'
                     '483/normal/me.jpg', user.GetProfileImageUrl())
    user.SetStatus(self._GetSampleStatus())
    self.assertEqual(4212713, user.GetStatus().id)

  def testProperties(self):
    '''Test all of the renjian.User properties'''
    user = renjian.User()
    user.id = 673483
    self.assertEqual(673483, user.id)
    user.name = 'DeWitt'
    self.assertEqual('DeWitt', user.name)
    user.screen_name = 'dewitt'
    self.assertEqual('dewitt', user.screen_name)
    user.description = 'Indeterminate things'
    self.assertEqual('Indeterminate things', user.description)
    user.location = 'San Francisco, CA'
    self.assertEqual('San Francisco, CA', user.location)
    user.profile_image_url = 'http://renjian.com/system/user/profile_i' \
                             'mage/673483/normal/me.jpg'
    self.assertEqual('http://renjian.com/system/user/profile_image/6734'
                     '83/normal/me.jpg', user.profile_image_url)
    self.status = self._GetSampleStatus()
    self.assertEqual(4212713, self.status.id)

  def testAsJsonString(self):
    '''Test the renjian.User AsJsonString method'''
    self.assertEqual(UserTest.SAMPLE_JSON,
                     self._GetSampleUser().AsJsonString())

  def testAsDict(self):
    '''Test the renjian.User AsDict method'''
    user = self._GetSampleUser()
    data = user.AsDict()
    self.assertEqual(673483, data['id'])
    self.assertEqual('DeWitt', data['name'])
    self.assertEqual('dewitt', data['screen_name'])
    self.assertEqual('Indeterminate things', data['description'])
    self.assertEqual('San Francisco, CA', data['location'])
    self.assertEqual('http://renjian.com/system/user/profile_image/6734'
                     '83/normal/me.jpg', data['profile_image_url'])
    self.assertEqual('http://unto.net/', data['url'])
    self.assertEqual(4212713, data['status']['id'])

  def testEq(self):
    '''Test the renjian.User __eq__ method'''
    user = renjian.User()
    user.id = 673483
    user.name = 'DeWitt'
    user.screen_name = 'dewitt'
    user.description = 'Indeterminate things'
    user.location = 'San Francisco, CA'
    user.profile_image_url = 'http://renjian.com/system/user/profile_image/67' \
                             '3483/normal/me.jpg'
    user.url = 'http://unto.net/'
    user.status = self._GetSampleStatus()
    self.assertEqual(user, self._GetSampleUser())

  def testNewFromJsonDict(self):
    '''Test the renjian.User NewFromJsonDict method'''
    data = simplejson.loads(UserTest.SAMPLE_JSON)
    user = renjian.User.NewFromJsonDict(data)
    self.assertEqual(self._GetSampleUser(), user)


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
    self._AddHandler('http://renjian.com/statuses/public_timeline.json',
                     curry(self._OpenTestData, 'public_timeline_error.json'))
    # Manually try/catch so we can check the exception's value
    try:
      statuses = self._api.GetPublicTimeline()
    except renjian.renjianError, error:
      # If the error message matches, the test passes
      self.assertEqual('test error', error.message)
    else:
      self.fail('renjianError expected')

  def testGetPublicTimeline(self):
    '''Test the renjian.Api GetPublicTimeline method'''
    self._AddHandler('http://renjian.com/statuses/public_timeline.json?since_id=12345',
                     curry(self._OpenTestData, 'public_timeline.json'))
    statuses = self._api.GetPublicTimeline(since_id=12345)
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(20, len(statuses))
    self.assertEqual(89497702, statuses[0].id)

  def testGetUserTimeline(self):
    '''Test the renjian.Api GetUserTimeline method'''
    self._AddHandler('http://renjian.com/statuses/user_timeline/kesuke.json?count=1&since=Tue%2C+27+Mar+2007+22%3A55%3A48+GMT',
                     curry(self._OpenTestData, 'user_timeline-kesuke.json'))
    statuses = self._api.GetUserTimeline('kesuke', count=1, since='Tue, 27 Mar 2007 22:55:48 GMT')
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(89512102, statuses[0].id)
    self.assertEqual(718443, statuses[0].user.id)

  def testGetFriendsTimeline(self):
    '''Test the renjian.Api GetFriendsTimeline method'''
    self._AddHandler('http://renjian.com/statuses/friends_timeline/kesuke.json',
                     curry(self._OpenTestData, 'friends_timeline-kesuke.json'))
    statuses = self._api.GetFriendsTimeline('kesuke')
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(20, len(statuses))
    self.assertEqual(718443, statuses[0].user.id)

  def testGetStatus(self):
    '''Test the renjian.Api GetStatus method'''
    self._AddHandler('http://renjian.com/statuses/show/89512102.json',
                     curry(self._OpenTestData, 'show-89512102.json'))
    status = self._api.GetStatus(89512102)
    self.assertEqual(89512102, status.id)
    self.assertEqual(718443, status.user.id)

  def testDestroyStatus(self):
    '''Test the renjian.Api DestroyStatus method'''
    self._AddHandler('http://renjian.com/statuses/destroy/103208352.json',
                     curry(self._OpenTestData, 'status-destroy.json'))
    status = self._api.DestroyStatus(103208352)
    self.assertEqual(103208352, status.id)

  def testPostUpdate(self):
    '''Test the renjian.Api PostUpdate method'''
    self._AddHandler('http://renjian.com/statuses/update.json',
                     curry(self._OpenTestData, 'update.json'))
    status = self._api.PostUpdate(u'asdfasdf')
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(u'asdf', status.text)

  def testGetReplies(self):
    '''Test the renjian.Api GetReplies method'''
    self._AddHandler('http://renjian.com/statuses/replies.json?page=1',
                     curry(self._OpenTestData, 'replies.json'))
    statuses = self._api.GetReplies(page=1)
    self.assertEqual(36657062, statuses[0].id)

  def testGetFriends(self):
    '''Test the renjian.Api GetFriends method'''
    self._AddHandler('http://renjian.com/statuses/friends.json?page=1',
                     curry(self._OpenTestData, 'friends.json'))
    users = self._api.GetFriends(page=1)
    buzz = [u.status for u in users if u.screen_name == 'buzz']
    self.assertEqual(89543882, buzz[0].id)

  def testGetFollowers(self):
    '''Test the renjian.Api GetFollowers method'''
    self._AddHandler('http://renjian.com/statuses/followers.json?page=1',
                     curry(self._OpenTestData, 'followers.json'))
    users = self._api.GetFollowers(page=1)
    # This is rather arbitrary, but spot checking is better than nothing
    alexkingorg = [u.status for u in users if u.screen_name == 'alexkingorg']
    self.assertEqual(89554432, alexkingorg[0].id)

  def testGetFeatured(self):
    '''Test the renjian.Api GetFeatured method'''
    self._AddHandler('http://renjian.com/statuses/featured.json',
                     curry(self._OpenTestData, 'featured.json'))
    users = self._api.GetFeatured()
    # This is rather arbitrary, but spot checking is better than nothing
    stevenwright = [u.status for u in users if u.screen_name == 'stevenwright']
    self.assertEqual(86991742, stevenwright[0].id)

  def testGetDirectMessages(self):
    '''Test the renjian.Api GetDirectMessages method'''
    self._AddHandler('http://renjian.com/direct_messages.json?page=1',
                     curry(self._OpenTestData, 'direct_messages.json'))
    statuses = self._api.GetDirectMessages(page=1)
    self.assertEqual(u'asdfasdfs', statuses[0].text)

  def testPostDirectMessage(self):
    '''Test the renjian.Api PostDirectMessage method'''
    self._AddHandler('http://renjian.com/direct_messages/new.json',
                     curry(self._OpenTestData, 'direct_messages-new.json'))
    status = self._api.PostDirectMessage('test', u'zxcvzxcv')
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(u'asdfasdfdsf', status.text)

  def testDestroyDirectMessage(self):
    '''Test the renjian.Api DestroyDirectMessage method'''
    self._AddHandler('http://renjian.com/direct_messages/destroy/3496342.json',
                     curry(self._OpenTestData, 'direct_message-destroy.json'))
    status = self._api.DestroyDirectMessage(3496342)
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(673483, status.sender_id)

  def testCreateFriendship(self):
    '''Test the renjian.Api CreateFriendship method'''
    self._AddHandler('http://renjian.com/friendships/create/dewitt.json',
                     curry(self._OpenTestData, 'friendship-create.json'))
    user = self._api.CreateFriendship('dewitt')
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(673483, user.id)

  def testDestroyFriendship(self):
    '''Test the renjian.Api DestroyFriendship method'''
    self._AddHandler('http://renjian.com/friendships/destroy/dewitt.json',
                     curry(self._OpenTestData, 'friendship-destroy.json'))
    user = self._api.DestroyFriendship('dewitt')
    # This is rather arbitrary, but spot checking is better than nothing
    self.assertEqual(673483, user.id)

  def testGetUser(self):
    '''Test the renjian.Api GetUser method'''
    self._AddHandler('http://renjian.com/users/show/dewitt.json',
                     curry(self._OpenTestData, 'show-dewitt.json'))
    user = self._api.GetUser('dewitt')
    self.assertEqual('dewitt', user.screen_name)
    self.assertEqual(89586072, user.status.id)

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
  
"""

if __name__ == '__main__':
  unittest.main()
