#!/usr/bin/python2.6
# coding=UTF8

__author__ = 'Arthur Wang'
__version__ = '0.1'


import base64
import calendar
import os
import rfc822
import simplejson
import sys
import tempfile
import textwrap
import time
import urllib
import urllib2
import urlparse

try:
  from hashlib import md5
except ImportError:
  from md5 import md5


CHARACTER_LIMIT = 140


class RenjianError(Exception):
  '''Base class for Renjian errors'''
  
  @property
  def message(self):
    '''Returns the first argument used to construct this error.'''
    return self.args[0]


class Status(object):
  '''A class representing the Status structure used by the renjian API.

  The Status structure exposes the following properties:
  
    status.id
    status.created_at
    status.created_at_in_seconds(Read Only)
    status.relative_date
    status.text
    status.source
    status.truncated
    status.in_reply_to_status_id
    status.in_reply_to_user_id
    status.in_reply_to_screen_name
    status.favorited
    status.original_url
    status.status_type
    status.link_title
    status.link_desc
    status.thumbnail
    status.level
    status.root_screen_name
    status.root_status_id
    status.all_zt_num
    status.stick
    status.favoriters
    status.user
  '''
  def __init__(self, 
               id=None,
               created_at=None,
               relative_date=None,
               text=None,
               source=None,
               truncated=None,
               in_reply_to_status_id=None,
               in_reply_to_user_id=None,
               in_reply_to_screen_name=None,
               favorited=None,
               original_url=None,
               status_type=None,
               link_title=None,
               link_desc=None,
               thumbnail=None,
               level=None,
               root_screen_name=None,
               root_status_id=None,
               all_zt_num=None,
               stick=None,
               favoriters=None,
               user=None):
    '''An object to hold a Renjian status message.

    This class is normally instantiated by the renjian.Api class and
    returned in a sequence.

    Note: Dates are posted in the form "2009-08-15 02:21:36 +0800"

    '''
    self.id=id
    self.created_at=created_at
    self.relative_date=relative_date
    self.text=text
    self.source=source
    self.truncated=truncated
    self.in_reply_to_status_id=in_reply_to_status_id
    self.in_reply_to_user_id=in_reply_to_user_id
    self.in_reply_to_screen_name=in_reply_to_screen_name
    self.favorited=favorited
    self.original_url=original_url
    self.status_type=status_type
    self.link_title=link_title
    self.link_desc=link_desc
    self.thumbnail=thumbnail
    self.level=level
    self.root_screen_name=root_screen_name
    self.root_status_id=root_status_id
    self.all_zt_num=all_zt_num
    self.stick=stick
    self.favoriters=favoriters
    self.user=user

  def GetId(self):
    return self._id
  def SetId(self, id):
    self._id = id
  id = property(GetId, SetId,
                doc='The unique id of this status message.')

  def GetCreatedAt(self):
    return self._created_at
  def SetCreatedAt(self, created_at):
    self._created_at = created_at
  created_at = property(GetCreatedAt, SetCreatedAt,
                        doc='The time this status message was posted. ')

#  def GetCreatedAtInSeconds(self):
#    return calendar.timegm(rfc822.parsedate(self.created_at))
#  created_at_in_seconds = property(GetCreatedAtInSeconds,
#                                   doc="The time this status message was "
#                                       "posted, in seconds since the epoch")

  def GetRelativeDate(self):
    return self._relative_date
  def SetRelativeDate(self, relative_date):
      self._relative_date = relative_date
  relative_date = property(GetRelativeDate, SetRelativeDate,
                           doc="The relative date which calculated by server.")

  def GetText(self):
    return self._text
  def SetText(self, text):
    self._text = text
  text = property(GetText, SetText,
                  doc='The text of this status message.')

  def GetSource(self):
    return self._source
  def SetSource(self, source):
    self._source = source
  source = property(GetSource, SetSource,
                    doc='The source which post this status message.')

  def GetTruncated(self):
    return self._truncated
  def SetTruncated(self, truncated):
    self._truncated = truncated
  truncated = property(GetTruncated, SetTruncated,
                       doc='The flag represents if the status message is truncated into 140. ')

  def GetInReplyToStatusId(self):
    return self._in_reply_to_status_id
  def SetInReplyToStatusId(self, in_reply_to_status_id):
    self._in_reply_to_status_id = in_reply_to_status_id
  in_reply_to_status_id = property(GetInReplyToStatusId, SetInReplyToStatusId,
                                   doc='The id of a status which is replied by this status.')

  def GetInReplyToUserId(self):
    return self._in_reply_to_user_id
  def SetInReplyToUserId(self, in_reply_to_user_id):
    self._in_reply_to_user_id = in_reply_to_user_id
  in_reply_to_user_id = property(GetInReplyToUserId, SetInReplyToUserId,
                                 doc='The id of a user which is replied by this status.')

  def GetInReplyToScreenName(self):
    return self._in_reply_to_screen_name
  def SetInReplyToScreenName(self, in_reply_to_screen_name):
    self._in_reply_to_screen_name = in_reply_to_screen_name
  in_reply_to_screen_name = property(GetInReplyToScreenName, SetInReplyToScreenName,
                                     doc='The screen name of a user whick is replied by this status.')
  
  def GetFavorited(self):
    return self._favorited
  def SetFavorited(self, favorited):
    self._favorited = favorited
  favorited = property(GetFavorited, SetFavorited,
                       doc='The favorited state of this status message.')
  
  def GetOriginalUrl(self):
      return self._original_url
  def SetOriginalUrl(self, original_url):
      self._original_url = original_url
  original_url = property(GetOriginalUrl, SetOriginalUrl,
                          doc='The original url of the link or picture that this status contains.')
  
  def GetStatusType(self):
      return self._status_type
  def SetStatusType(self, status_type):
      self._status_type = status_type
  status_type = property(GetStatusType, SetStatusType,
                         doc='The status type of this status.'
                             'It is TEXT, PICTURE or LINK')
  
  def GetLinkTitle(self):
      return self._link_title
  def SetLinkTitle(self, link_title):
      self._link_title = link_title
  link_title = property(GetLinkTitle, SetLinkTitle,
                        doc='The title of the link which this status contains.')
  
  def GetLinkDesc(self):
      return self._link_desc
  def SetLinkDesc(self, link_desc):
      self._link_desc = link_desc
  link_desc = property(GetLinkDesc, SetLinkDesc,
                       doc='The description of the link which this status contains.')
  
  def GetLevel(self):
      return self._level
  def SetLevel(self, level):
      self._level = level
  level = property(GetLevel, SetLevel,
                   doc='The level of this status.' 
                       'It will be 1 if you post it first.')
  
  def GetThumbnail(self):
      return self._thumbnail
  def SetThumbnail(self, thumbnail):
      self._thumbnail = thumbnail
  thumbnail = property(GetThumbnail, SetThumbnail,
                       doc='The thumbnail url of the link or picture.')
  
  def GetRootScreenName(self):
      return self._root_screen_name
  def SetRootScreenName(self, root_screen_name):
      self._root_screen_name = root_screen_name
  root_screen_name = property(GetRootScreenName, SetRootScreenName,
                              doc='The screen name of the root status of this status.')
  
  def GetRootStatusId(self):
      return self._root_status_id
  def SetRootStatusId(self, root_status_id):
      self._root_status_id = root_status_id
  root_status_id = property(GetRootStatusId, SetRootStatusId,
                            doc='The if of the root status of this status.')
  
  def GetAllZtNum(self):
      return self._all_zt_num
  def SetAllZtNum(self, all_zt_num):
      self._all_zt_num = all_zt_num
  all_zt_num = property(GetAllZtNum, SetAllZtNum,
                        doc='The number counting how many times this status was resent.')
  
  def GetStick(self):
      return self._stick
  def SetStick(self, stick):
      self._stick = stick
  stick = property(GetStick, SetStick,
                   doc='The flag represents if this status is stuck')
  
  def GetFavoriters(self):
      return self._favoriters
  def SetFavoriters(self, favoriters):
      self._favoriters = favoriters
  favoriters = property(GetFavoriters, SetFavoriters,
                        doc='The screen names users who set this status as their favorites.')

  def GetUser(self):
    return self._user
  def SetUser(self, user):
    self._user = user
  user = property(GetUser, SetUser,
                  doc='A renjian.User reprenting the entity posting this '
                      'status message')

  #TODO: need modify
  '''
  def GetRelativeCreatedAt(self):
    fudge = 1.25
    delta  = long(self.now) - long(self.created_at_in_seconds)

    if delta < (1 * fudge):
      return 'about a second ago'
    elif delta < (60 * (1/fudge)):
      return 'about %d seconds ago' % (delta)
    elif delta < (60 * fudge):
      return 'about a minute ago'
    elif delta < (60 * 60 * (1/fudge)):
      return 'about %d minutes ago' % (delta / 60)
    elif delta < (60 * 60 * fudge):
      return 'about an hour ago'
    elif delta < (60 * 60 * 24 * (1/fudge)):
      return 'about %d hours ago' % (delta / (60 * 60))
    elif delta < (60 * 60 * 24 * fudge):
      return 'about a day ago'
    else:
      return 'about %d days ago' % (delta / (60 * 60 * 24))

  relative_created_at = property(GetRelativeCreatedAt,
                                 doc='Get a human readable string representing'
                                     'the posting time')
  '''

  def __ne__(self, other):
    return not self.__eq__(other)

  def __eq__(self, other):
    try:
      return other and \
             self.id == other.id and \
             self.created_at == other.created_at and \
             self.relative_date == other.relative_date and \
             self.text == other.text and \
             self.source == other.source and \
             self.truncated == other.truncated and \
             self.in_reply_to_status_id == other.in_reply_to_status_id and \
             self.in_reply_to_user_id == other.in_reply_to_user_id and \
             self.in_reply_to_screen_name == other.in_reply_to_screen_name and \
             self.favorited == other.favorited and \
             self.original_url == other.original_url and \
             self.status_type == other.status_type and \
             self.link_title == other.link_title and \
             self.link_desc == other.link_desc and \
             self.thumbnail == other.thumbnail and \
             self.level == other.level and \
             self.root_screen_name == other.root_screen_name and \
             self.root_status_id == other.root_status_id and \
             self.all_zt_num == other.all_zt_num and \
             self.stick == other.stick and \
             self.favoriters == other.favoriters and \
             self.user == other.user
    except AttributeError:
      return False

  def __str__(self):
    '''A string representation of this renjian.Status instance.

    The return value is the same as the JSON string representation.

    Returns:
      A string representation of this renjian.Status instance.
    '''
    return self.AsJsonString()

  def AsJsonString(self):
    '''A JSON string representation of this renjian.Status instance.

    Returns:
      A JSON string representation of this renjian.Status instance
   '''
    return simplejson.dumps(self.AsDict(), sort_keys=True)

  def AsDict(self):
    '''A dict representation of this renjian.Status instance.

    The return value uses the same key names as the JSON representation.

    Return:
      A dict representing this renjian.Status instance
    '''
    data = {}
    if self.id:
      data['id'] = self.id
    if self.created_at:
      data['created_at'] = self.created_at
    if self.relative_date:
      data['relative_date'] = self.relative_date
    if self.text:
      data['text'] = self.text
    if self.source:
      data['source'] = self.source
    if self.truncated is not None:
      data['truncated'] = self.truncated
    if self.in_reply_to_status_id:
      data['in_reply_to_status_id'] = self.in_reply_to_status_id
    if self.in_reply_to_user_id:
      data['in_reply_to_user_id'] = self.in_reply_to_user_id
    if self.in_reply_to_screen_name:
      data['in_reply_to_screen_name'] = self.in_reply_to_screen_name
    if self.favorited is not None:
      data['favorited'] = self.favorited
    if self.original_url:
      data['original_url'] = self.original_url
    if self.status_type:
      data['status_type'] = self.status_type
    if self.link_title:
      data['link_title'] = self.link_title
    if self.link_desc:
      data['link_desc'] = self.link_desc
    if self.thumbnail:
      data['thumbnail'] = self.thumbnail    
    if self.level:
      data['level'] = self.level
    if self.root_screen_name:
      data['root_screen_name'] = self.root_screen_name
    if self.root_status_id:
      data['root_status_id'] = self.root_status_id
    if self.all_zt_num is not None:
      data['all_zt_num'] = self.all_zt_num
    if self.stick is not None:
      data['stick'] = self.stick
    if self.favoriters:
      data['favoriters'] = self.favoriters
    if self.user:
      data['user'] = self.user.AsDict()
    return data

  @staticmethod
  def NewFromJsonDict(data):
    '''Create a new instance based on a JSON dict.

    Args:
      data: A JSON dict, as converted from the JSON in the renjian API
    Returns:
      A renjian.Status instance
    '''
    if 'user' in data:
      user = User.NewFromJsonDict(data['user'])
    else:
      user = None
    return Status(id=data.get('id', None),
                  created_at=data.get('created_at', None),
                  relative_date=data.get('relative_date', None),
                  text=data.get('text', None),
                  source=data.get('source', None),
                  truncated=data.get('truncated', None),
                  in_reply_to_status_id=data.get('in_reply_to_status_id', None),
                  in_reply_to_user_id=data.get('in_reply_to_user_id', None),
                  in_reply_to_screen_name=data.get('in_reply_to_screen_name', None),
                  favorited=data.get('favorited', None),
                  original_url=data.get('original_url', None),
                  status_type=data.get('status_type', None),
                  link_title=data.get('link_title', None),
                  link_desc=data.get('link_desc', None),
                  thumbnail=data.get('thumbnail', None),
                  level=data.get('level', None),
                  root_screen_name=data.get('root_screen_name', None),
                  root_status_id=data.get('root_status_id', None),
                  all_zt_num=data.get('all_zt_num', None),
                  stick=data.get('stick', None),
                  favoriters=data.get('favoriters', None),
                  user=user)


class User(object):
  '''A class representing the User structure used by the renjian API.

  The User structure exposes the following properties:

    user.id
    user.name
    user.screen_name
    user.description
    user.profile_image_url
    user.url
    user.protected
    user.created_at
    user.followers_count
    user.following_count
    user.favourites_count
    user.is_followed_me
    user.is_following
    user.score
    user.gender
  '''
  def __init__(self,
               id=None,
               name=None,
               screen_name=None,
               description=None,
               profile_image_url=None,
               url=None,
               protected=None,
               created_at=None,
               followers_count=None,
               following_count=None,
               favourites_count=None,
               is_followed_me=None,
               is_following=None,
               score=None,
               gender=None):
      
    self.id = id
    self.name = name
    self.screen_name = screen_name
    self.description = description
    self.profile_image_url = profile_image_url
    self.url = url
    self.protected = protected
    self.created_at = created_at
    self.followers_count = followers_count
    self.following_count = following_count
    self.favourites_count = favourites_count
    self.is_followed_me = is_followed_me
    self.is_following = is_following
    self.score = score
    self.gender = gender

  def GetId(self):
    return self._id
  def SetId(self, id):
    self._id = id
  id = property(GetId, SetId,
                doc='The unique id of this user.')

  def GetName(self):
    return self._name
  def SetName(self, name):
    self._name = name
  name = property(GetName, SetName,
                  doc='The real name of this user.')

  def GetScreenName(self):
    return self._screen_name
  def SetScreenName(self, screen_name):
    self._screen_name = screen_name
  screen_name = property(GetScreenName, SetScreenName,
                         doc='The short username of this user.')

  def GetDescription(self):
    return self._description
  def SetDescription(self, description):
    self._description = description
  description = property(GetDescription, SetDescription,
                         doc='The short text description of this user.')

  def GetProfileImageUrl(self):
    return self._profile_image_url
  def SetProfileImageUrl(self, profile_image_url):
    self._profile_image_url = profile_image_url
  profile_image_url= property(GetProfileImageUrl, SetProfileImageUrl,
                              doc='The url of the thumbnail of this user.')
  
  def GetUrl(self):
    return self._url
  def SetUrl(self, url):
    self._url = url
  url = property(GetUrl, SetUrl,
                 doc='The homepage url of this user.')

  def GetProtected(self):
    return self._protected
  def SetProtected(self, protected):
    self._protected = protected
  protected = property(GetProtected, SetProtected,
                       doc='The flag represents if this user is protected.')

  def GetCreatedAt(self):
    return self._created_at
  def SetCreatedAt(self, created_at):
    self._created_at = created_at
  created_at = property(GetCreatedAt, SetCreatedAt,
                        doc='The date time who this user registered.')

  def GetFollowersCount(self):
    return self._followers_count
  def SetFollowersCount(self, followers_count):
    self._followers_count = followers_count
  followers_count = property(GetFollowersCount, SetFollowersCount,
                             doc='The number of users following this user.')

  def GetFollowingCount(self):
    return self._following_count
  def SetFollowingCount(self, followers_count):
    self._following_count = followers_count
  following_count = property(GetFollowingCount, SetFollowingCount,
                             doc='The number of users this user following.')

  def GetFavouritesCount(self):
    return self._favourites_count
  def SetFavouritesCount(self, followers_count):
    self._favourites_count = followers_count
  favourites_count = property(GetFavouritesCount, SetFavouritesCount,
                              doc='The number of favourites for this user.')
  
  def GetIsFollowedMe(self):
    return self._is_followed_me
  def SetIsFollowedMe(self, is_followed_me):
    self._is_followed_me = is_followed_me
  is_followed_me = property(GetIsFollowedMe, SetIsFollowedMe,
                            doc='The flag represents if this user is following the authorized user.')
  
  def GetIsFollowing(self):
    return self._is_following
  def SetIsFollowing(self, is_following):
    self._is_following = is_following
  is_following = property(GetIsFollowing, SetIsFollowing,
                 doc='The flag represents if the authorized user is following this user.')
  
  def GetScore(self):
    return self._score
  def SetScore(self, score):
    self._score = score
  score = property(GetScore, SetScore,
                   doc='The score who this user has.')
  
  def GetGender(self):
    return self._gender
  def SetGender(self, gender):
    self._gender = gender
  gender = property(GetGender, SetGender,
                    doc='The gender of this user.')

  def __ne__(self, other):
    return not self.__eq__(other)

  def __eq__(self, other):
    try:
      return other and \
             self.id == other.id and \
             self.name == other.name and \
             self.screen_name == other.screen_name and \
             self.description == other.description and \
             self.profile_image_url == other.profile_image_url and \
             self.url == other.url and \
             self.protected == other.protected and \
             self.created_at == other.created_at and \
             self.followers_count == other.followers_count and \
             self.following_count == other.following_count and \
             self.favourites_count == other.favourites_count and \
             self.is_followed_me == other.is_followed_me and \
             self.is_following == other.is_following and \
             self.score == other.score and \
             self.gender == other.gender
    except AttributeError:
      return False

  def __str__(self):
    '''A string representation of this renjian.User instance.

    The return value is the same as the JSON string representation.

    Returns:
      A string representation of this renjian.User instance.
    '''
    return self.AsJsonString()

  def AsJsonString(self):
    '''A JSON string representation of this renjian.User instance.

    Returns:
      A JSON string representation of this renjian.User instance
   '''
    return simplejson.dumps(self.AsDict(), sort_keys=True)

  def AsDict(self):
    '''A dict representation of this renjian.User instance.

    The return value uses the same key names as the JSON representation.

    Return:
      A dict representing this renjian.User instance
    '''
    data = {}
    if self.id:
      data['id'] = self.id
    if self.name:
      data['name'] = self.name
    if self.screen_name:
      data['screen_name'] = self.screen_name
    if self.description:
      data['description'] = self.description
    if self.profile_image_url:
      data['profile_image_url'] = self.profile_image_url
    if self.url:
      data['url'] = self.url
    if self.protected is not None:
      data['protected'] = self.protected
    if self.created_at:
      data['created_at'] = self.created_at
    if self.followers_count is not None:
      data['followers_count'] = self.followers_count
    if self.following_count is not None:
      data['following_count'] = self.following_count
    if self.favourites_count is not None:
      data['favourites_count'] = self.favourites_count
    if self.is_followed_me is not None:
      data['is_followed_me'] = self.is_followed_me
    if self.is_following is not None:
      data['is_following'] = self.is_following
    if self.score is not None:
      data['score'] = self.score
    if self.gender is not None:
      data['gender'] = self.gender
      
    return data

  @staticmethod
  def NewFromJsonDict(data):
    '''Create a new instance based on a JSON dict.

    Args:
      data: A JSON dict, as converted from the JSON in the renjian API
    Returns:
      A renjian.User instance
    '''
    return User(id=data.get('id', None),
                name=data.get('name', None),
                screen_name=data.get('screen_name', None),
                description=data.get('description', None),
                profile_image_url=data.get('profile_image_url', None),
                url=data.get('url', None),
                protected = data.get('protected', None),
                created_at = data.get('created_at', None),
                followers_count=data.get('followers_count', None),
                following_count=data.get('following_count', None),
                favourites_count=data.get('favourites_count', None),
                is_followed_me=data.get('is_followed_me', None),
                is_following=data.get('is_following', None),
                score=data.get('score', None),
                gender=data.get('gender', None))


class DirectMessage(object):
  '''A class representing the DirectMessage structure used by the renjian API.

  The DirectMessage structure exposes the following properties:

    direct_message.id
    direct_message.created_at
    direct_message.created_at_in_seconds # read only
    direct_message.sender_id
    direct_message.sender_screen_name
    direct_message.recipient_id
    direct_message.recipient_screen_name
    direct_message.text
    direct_message.sender
    direct_message.recipient
  '''

  def __init__(self,
               id=None,
               created_at=None,
               sender_id=None,
               sender_screen_name=None,
               recipient_id=None,
               recipient_screen_name=None,
               text=None,
               sender=None,
               recipient=None):
    '''An object to hold a renjian direct message.

    This class is normally instantiated by the renjian.Api class and
    returned in a sequence.

    Note: Dates are posted in the form "Sat Jan 27 04:17:38 +0000 2007"

    Args:
      id: The unique id of this direct message
      created_at: The time this direct message was posted
      sender_id: The id of the renjian user that sent this message
      sender_screen_name: The name of the renjian user that sent this message
      recipient_id: The id of the renjian that received this message
      recipient_screen_name: The name of the renjian that received this message
      text: The text of this direct message
    '''
    self.id = id
    self.created_at = created_at
    self.sender_id = sender_id
    self.sender_screen_name = sender_screen_name
    self.recipient_id = recipient_id
    self.recipient_screen_name = recipient_screen_name
    self.text = text
    self.sender = sender
    self.recipient = recipient

  def GetId(self):
    return self._id
  def SetId(self, id):
    self._id = id
  id = property(GetId, SetId,
                doc='The unique id of this direct message.')

  def GetCreatedAt(self):
    return self._created_at
  def SetCreatedAt(self, created_at):
    self._created_at = created_at
  created_at = property(GetCreatedAt, SetCreatedAt,
                        doc='The time this direct message was posted.')

#  def GetCreatedAtInSeconds(self):
#    return calendar.timegm(rfc822.parsedate(self.created_at))
#  created_at_in_seconds = property(GetCreatedAtInSeconds,
#                                   doc="The time this direct message was "
#                                       "posted, in seconds since the epoch")

  def GetSenderId(self):
    return self._sender_id
  def SetSenderId(self, sender_id):
    self._sender_id = sender_id
  sender_id = property(GetSenderId, SetSenderId,
                       doc='The unique sender id of this direct message.')

  def GetSenderScreenName(self):
    return self._sender_screen_name
  def SetSenderScreenName(self, sender_screen_name):
    self._sender_screen_name = sender_screen_name
  sender_screen_name = property(GetSenderScreenName, SetSenderScreenName,
                                doc='The unique sender screen name of this direct message.')

  def GetRecipientId(self):
    return self._recipient_id
  def SetRecipientId(self, recipient_id):
    self._recipient_id = recipient_id
  recipient_id = property(GetRecipientId, SetRecipientId,
                          doc='The unique recipient id of this direct message.')

  def GetRecipientScreenName(self):
    return self._recipient_screen_name
  def SetRecipientScreenName(self, recipient_screen_name):
    self._recipient_screen_name = recipient_screen_name
  recipient_screen_name = property(GetRecipientScreenName, SetRecipientScreenName,
                                   doc='The unique recipient screen name of this direct message.')

  def GetText(self):
    return self._text
  def SetText(self, text):
    self._text = text
  text = property(GetText, SetText,
                  doc='The text of this direct message')
  
  def GetSender(self):
    return self._sender
  def SetSender(self, sender):
    self._sender = sender
  sender = property(GetSender, SetSender,
                    doc='The renjian.User object of sender.')
  
  def GetRecipient(self):
    return self._recipient
  def SetRecipient(self, recipient):
    self._recipient = recipient
  recipient = property(GetRecipient, SetRecipient,
                       doc='The renjian.User object of recipient.')

  def __ne__(self, other):
    return not self.__eq__(other)

  def __eq__(self, other):
    try:
      return other and \
          self.id == other.id and \
          self.created_at == other.created_at and \
          self.sender_id == other.sender_id and \
          self.sender_screen_name == other.sender_screen_name and \
          self.recipient_id == other.recipient_id and \
          self.recipient_screen_name == other.recipient_screen_name and \
          self.text == other.text and \
          self.sender == other.sender and \
          self.recipient == other.recipient
    except AttributeError:
      return False

  def __str__(self):
    '''A string representation of this renjian.DirectMessage instance.

    The return value is the same as the JSON string representation.

    Returns:
      A string representation of this renjian.DirectMessage instance.
    '''
    return self.AsJsonString()

  def AsJsonString(self):
    '''A JSON string representation of this renjian.DirectMessage instance.

    Returns:
      A JSON string representation of this renjian.DirectMessage instance
   '''
    return simplejson.dumps(self.AsDict(), sort_keys=True)

  def AsDict(self):
    '''A dict representation of this renjian.DirectMessage instance.

    The return value uses the same key names as the JSON representation.

    Return:
      A dict representing this renjian.DirectMessage instance
    '''
    data = {}
    if self.id:
      data['id'] = self.id
    if self.created_at:
      data['created_at'] = self.created_at
    if self.sender_id:
      data['sender_id'] = self.sender_id
    if self.sender_screen_name:
      data['sender_screen_name'] = self.sender_screen_name
    if self.recipient_id:
      data['recipient_id'] = self.recipient_id
    if self.recipient_screen_name:
      data['recipient_screen_name'] = self.recipient_screen_name
    if self.text:
      data['text'] = self.text
    if self.sender:
      data['sender'] = self.sender.AsDict();
    if self.recipient:
      data['recipient'] = self.recipient.AsDict();
    return data

  @staticmethod
  def NewFromJsonDict(data):
    '''Create a new instance based on a JSON dict.

    Args:
      data: A JSON dict, as converted from the JSON in the renjian API
    Returns:
      A renjian.DirectMessage instance
    '''
    if 'sender' in data:
      sender = User.NewFromJsonDict(data['sender'])
    else:
      sender = None
    if 'recipient' in data:
      recipient = User.NewFromJsonDict(data['recipient'])
    else:
      recipient = None
    return DirectMessage(created_at=data.get('created_at', None),
                         recipient_id=data.get('recipient_id', None),
                         sender_id=data.get('sender_id', None),
                         text=data.get('text', None),
                         sender_screen_name=data.get('sender_screen_name', None),
                         id=data.get('id', None),
                         recipient_screen_name=data.get('recipient_screen_name', None),
                         sender=sender,
                         recipient=recipient)


class Conversation(object):
  '''A class representing the Conversation structure used by the renjian API.

  The Conversation structure exposes the following properties:

    conversation.id
    conversation.last_status_id
    conversation.text
    conversation.unread_count
    conversation.owner
  '''
  def __init__(self,
               id=None,
               last_status_id=None,
               text=None,
               unread_count=None,
               owner=None):
    '''An object to hold a renjian conversation.

    This class is normally instantiated by the renjian.Api class and
    returned in a sequence.

    Args:
      id: The unique id of conversation
      last_status_id: The last status id of the conversation
      text: Description of conversation(first status's text)
      unread_count: Unread count of statuses in Conversation 
      owner: A User object represent the ownder of the Conversation
    '''
    self.id = id
    self.last_status_id = last_status_id
    self.text = text
    self.unread_count = unread_count
    self.owner = owner

  def GetId(self):
    return self._id
  def SetId(self, id):
    self._id = id
  id = property(GetId, SetId,
                doc='The unique id of this conversation.')

  def GetLastStatusId(self):
    return self._last_status_id
  def SetLastStatusId(self, last_status_id):
    self._last_status_id = last_status_id
  last_status_id = property(GetLastStatusId, SetLastStatusId,
                            doc='The last status id of the conversation.')

  def GetText(self):
    return self._text
  def SetText(self, text):
    self._text = text
  text = property(GetText, SetText,
                  doc='Description of conversation(first Status.text)')
  
  def GetUnreadCount(self):
    return self._unread_count
  def SetUnreadCount(self, unread_count):
    self._unread_count = unread_count
  unread_count = property(GetUnreadCount, SetUnreadCount,
                          doc='Unread count of statuses in Conversation.')
  
  def GetOwner(self):
    return self._owner
  def SetOwner(self, owner):
    self._owner = owner
  owner = property(GetOwner, SetOwner,
                   doc='A User object represent the ownder of the Conversation')

  def __ne__(self, other):
    return not self.__eq__(other)

  def __eq__(self, other):
    try:
      return other and \
          self.id == other.id and \
          self.last_status_id == other.last_status_id and \
          self.text == other.text and \
          self.unread_count == other.unread_count and \
          self.owner == other.owner
    except AttributeError:
      return False

  def __str__(self):
    '''A string representation of this renjian.Conversation instance.

    The return value is the same as the JSON string representation.

    Returns:
      A string representation of this renjian.Conversation instance.
    '''
    return self.AsJsonString()

  def AsJsonString(self):
    '''A JSON string representation of this renjian.Conversation instance.

    Returns:
      A JSON string representation of this renjian.Conversation instance
   '''
    return simplejson.dumps(self.AsDict(), sort_keys=True)

  def AsDict(self):
    '''A dict representation of this renjian.Conversation instance.

    The return value uses the same key names as the JSON representation.

    Return:
      A dict representing this renjian.Conversation instance
    '''
    data = {}
    if self.id:
      data['id'] = self.id
    if self.last_status_id:
      data['last_status_id'] = self.last_status_id
    if self.text:
      data['text'] = self.text
    if self.unread_count is not None:
      data['unread_count'] = self.unread_count
    if self.owner:
      data['owner'] = self.owner.AsDict()
    return data

  @staticmethod
  def NewFromJsonDict(data):
    '''Create a new instance based on a JSON dict.

    Args:
      data: A JSON dict, as converted from the JSON in the renjian API
    Returns:
      A renjian.Conversation instance
    '''
    if 'owner' in data:
      owner = User.NewFromJsonDict(data['owner'])
    else:
      owner = None
    return Conversation(id=data.get('id', None),
                        last_status_id=data.get('last_status_id', None),
                        text=data.get('text', None),
                        unread_count=data.get('unread_count', None),
                        owner=owner)
    

class Api(object):
  '''A python interface into the Renjian API

  By default, the Api caches results for 1 minute.

  Example usage:

    To create an instance of the twitter.Api class, with no authentication:

      >>> import renjian
      >>> api = renjian.Api()

    To fetch the most recently posted public twitter status messages:

      >>> statuses = api.GetPublicTimeline()
      >>> print [s.user.name for s in statuses]
      [u'DeWitt', u'Kesuke Miyagi', u'ev', u'Buzz Andersen', u'Biz Stone'] #...

    To fetch a single user's public status messages, where "user" is either
    a Renjian "short name" or their user id.

      >>> statuses = api.GetUserTimeline(user)
      >>> print [s.text for s in statuses]

    To use authentication, instantiate the renjian.Api class with a
    username and password:

      >>> api = renjian.Api(username='renjian user', password='renjian pass')

    To fetch your friends (after being authenticated):

      >>> users = api.GetFriends()
      >>> print [u.name for u in users]

    To post a renjian status message (after being authenticated):

      >>> status = api.PostUpdate('I love renjian-python!')
      >>> print status.text
      I love renjian-python!

    There are many other methods, including:

      >>> api.PostUpdates(status)
      >>> api.PostDirectMessage(user, text)
      >>> api.GetUser(user)
      >>> api.GetReplies()
      >>> api.GetUserTimeline(user)
      >>> api.GetStatus(id)
      >>> api.DestroyStatus(id)
      >>> api.GetFriendsTimeline(user)
      >>> api.GetFriends(user)
      >>> api.GetFollowers()
      >>> api.GetFeatured()
      >>> api.GetDirectMessages()
      >>> api.PostDirectMessage(user, text)
      >>> api.DestroyDirectMessage(id)
      >>> api.DestroyFriendship(user)
      >>> api.CreateFriendship(user)
      >>> api.GetUserByEmail(email)
  '''

  DEFAULT_CACHE_TIMEOUT = 60 # cache for 1 minute

  _API_REALM = 'Twitter API'

  def __init__(self,
               username=None,
               password=None,
               input_encoding=None,
               request_headers=None):
    '''Instantiate a new renjian.Api object.

    Args:
      username: The username of the twitter account.  [optional]
      password: The password for the twitter account. [optional]
      input_encoding: The encoding used to encode input strings. [optional]
      request_header: A dictionary of additional HTTP request headers. [optional]
    '''
    self._cache = _FileCache()
    self._urllib = urllib2
    self._cache_timeout = Api.DEFAULT_CACHE_TIMEOUT
    self._InitializeRequestHeaders(request_headers)
    self._InitializeUserAgent()
    self._InitializeDefaultParameters()
    self._input_encoding = input_encoding
    self.SetCredentials(username, password)

  def GetPublicTimeline(self, 
                        since_id=None,
                        max_id=None,
                        count=None,
                        page=None):
    '''Fetch the sequnce of public renjian.Status message for all users.

    Args:
      since_id:
        Returns only public statuses with an ID greater than (that is,
        more recent than) the specified ID. [Optional]
      max_id:
        Returns only public statuses with an ID smaller than (that is,
        more recent than) the specified ID. [Optional]
      count: 
        Specifies the number of statuses to retrieve. May not be
        greater than 200. [Optional]
      page:
        ....

    Returns:
      An sequence of renjian.Status instances, one for each message
    '''
    parameters = {}
    if since_id:
      parameters['since_id'] = since_id
    if count:
      parameters['count'] = count
    if page:
      parameters['page'] = page
    url = 'http://api.renjian.com/statuses/public_timeline.json'
    json = self._FetchUrl(url,  parameters=parameters)
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return [Status.NewFromJsonDict(x) for x in data]

  def GetFriendsTimeline(self,
                         user=None,
                         since_id=None,
                         max_id=None,
                         count=None,
                         page=None):
    '''Fetch the sequence of renjian.Status messages for a user's friends

    The renjian.Api instance must be authenticated if the user is private.

    Args:
      user:
        Specifies the ID or screen name of the user for whom to return
        the friends_timeline.  If unspecified, the username and password
        must be set in the renjian.Api instance.  [Optional]
      since_id:
        Returns only public statuses with an ID greater than (that is,
        more recent than) the specified ID. [Optional]
      max_id:
        Returns only public statuses with an ID smaller than (that is,
        more recent than) the specified ID. [Optional]
      count: 
        Specifies the number of statuses to retrieve. May not be
        greater than 200. [Optional]
      page:
        ....

    Returns:
      A sequence of renjian.Status instances, one for each message
    '''
    if user:
      url = 'http://api.renjian.com/statuses/friends_timeline/%s.json' % user
    elif not user and not self._username:
      raise RenjianError("User must be specified if API is not authenticated.")
    else:
      url = 'http://api.renjian.com/statuses/friends_timeline.json'
    parameters = {}
    if count is not None:
      try:
        if int(count) > 500:
          raise RenjianError("'count' may not be greater than 500")
      except ValueError:
        raise RenjianError("'count' must be an integer")
      parameters['count'] = count
    if page:
      parameters['page'] = page
    if since_id:
      parameters['since_id'] = since_id
    if max_id:
      parameters['max_id'] = max_id
    json = self._FetchUrl(url, parameters=parameters)
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return [Status.NewFromJsonDict(x) for x in data]

  def GetUserTimeline(self, 
                      user=None,
                      since_id=None,
                      max_id=None,
                      count=None,
                      page=None):
    '''Fetch the sequence of public renjian.Status messages for a single user.

    The renjian.Api instance must be authenticated if the user is private.

    Args:
      user:
        Specifies the ID or screen name of the user for whom to return
        the friends_timeline.  If unspecified, the username and password
        must be set in the renjian.Api instance.  [Optional]
      since_id:
        Returns only public statuses with an ID greater than (that is,
        more recent than) the specified ID. [Optional]
      max_id:
        Returns only public statuses with an ID smaller than (that is,
        more recent than) the specified ID. [Optional]
      count: 
        Specifies the number of statuses to retrieve. May not be
        greater than 200. [Optional]
      page:
        ....
        
    Returns:
      A sequence of renjian.Status instances, one for each message up to count
    '''
    if user:
      url = 'http://api.renjian.com/statuses/user_timeline/%s.json' % user
    elif not user and not self._username:
      raise RenjianError("User must be specified if API is not authenticated.")
    else:
      url = 'http://api.renjian.com/statuses/user_timeline.json'
    parameters = {}
    if count is not None:
      try:
        if int(count) > 500:
          raise RenjianError("'count' may not be greater than 500")
      except ValueError:
        raise RenjianError("'count' must be an integer")
      parameters['count'] = count
    if page:
      parameters['page'] = page
    if since_id:
      parameters['since_id'] = since_id
    if max_id:
      parameters['max_id'] = max_id
    json = self._FetchUrl(url, parameters=parameters)
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return [Status.NewFromJsonDict(x) for x in data]

  def GetStatus(self, id):
    '''Returns a single status message.

    The renjian.Api instance must be authenticated if the status message is private.

    Args:
      id: The numerical ID of the status you're trying to retrieve.

    Returns:
      A renjian.Status instance representing that status message
    '''
    try:
      if id:
        long(id)
    except:
      raise RenjianError("id must be an long integer")
    url = 'http://api.renjian.com/statuses/%s.json' % id
    json = self._FetchUrl(url)
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return Status.NewFromJsonDict(data)

  def GetMentions(self,
                 since_id=None,
                 max_id=None,
                 count=None,
                 page=None):
    '''Get a sequence of status messages representing the 20 most recent
    replies (status updates prefixed with @username) to the authenticating
    user.

    Args:
      since_id:
        Returns only public statuses with an ID greater than (that is,
        more recent than) the specified ID. [Optional]
      max_id:
        Returns only public statuses with an ID smaller than (that is,
        more recent than) the specified ID. [Optional]
      count: 
        Specifies the number of statuses to retrieve. May not be
        greater than 200. [Optional]
      page:
        ....

    Returns:
      A sequence of twitter.Status instances, one for each reply to the user.
    '''
    url = 'http://api.renjian.com/statuses/mentions.json'
    if not self._username:
      raise RenjianError("The renjian.Api instance must be authenticated.")
    parameters = {}
    if count is not None:
      try:
        if int(count) > 500:
          raise RenjianError("'count' may not be greater than 500")
      except ValueError:
        raise RenjianError("'count' must be an integer")
      parameters['count'] = count
    if page:
      parameters['page'] = page
    if since_id:
      parameters['since_id'] = since_id
    if max_id:
      parameters['max_id'] = max_id
    json = self._FetchUrl(url, parameters=parameters)
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return [Status.NewFromJsonDict(x) for x in data]

  def DestroyStatus(self, id):
    '''Destroys the status specified by the required ID parameter.

    The renjian.Api instance must be authenticated and thee
    authenticating user must be the author of the specified status.

    Args:
      id: The numerical ID of the status you're trying to destroy.

    Returns:
      A renjian.Status instance representing the destroyed status message
    '''
    try:
      if id:
        long(id)
    except:
      raise RenjianError("id must be an integer")
    url = 'http://api.renjian.com/statuses/destroy/%s.json' % id
    json = self._FetchUrl(url, post_data={})
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return Status.NewFromJsonDict(data)

  def PostText(self, text, in_reply_to_status_id=None):
    '''Post a renjian pure text status message from the authenticated user.

    The renjian.Api instance must be authenticated.

    Args:
      text:
        The message text to be posted.  Must be less than or equal to
        140 characters.
      in_reply_to_status_id:
        The ID of an existing status that the status to be posted is
        in reply to.  This implicitly sets the in_reply_to_user_id
        attribute of the resulting status to the user ID of the
        message being replied to.  Invalid/missing status IDs will be
        ignored. [Optional]
    Returns:
      A renjian.Status instance representing the message posted.
    '''
    if not self._username:
      raise RenjianError("The renjian.Api instance must be authenticated.")

    url = 'http://api.renjian.com/statuses/update.json'

    if len(text) > CHARACTER_LIMIT:
      raise RenjianError("Text must be less than or equal to %d characters. "
                         "Consider using PostUpdates." % CHARACTER_LIMIT)

    data = {'text': text,
            'status_type': 'TEXT'}
    if in_reply_to_status_id:
      data['in_reply_to_status_id'] = in_reply_to_status_id
    json = self._FetchUrl(url, post_data=data)
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return Status.NewFromJsonDict(data)

  def PostLink(self, 
               text, 
               original_url=None,
               in_reply_to_status_id=None,
               link_title=None,
               link_desc=None):
    '''Post a renjian status message with a link from the authenticated user.

    The renjian.Api instance must be authenticated.

    Args:
      text:
        The message text to be posted.  Must be less than or equal to
        140 characters.
      original_url:
        The link's url. It must be filled in.
      in_reply_to_status_id:
        The ID of an existing status that the status to be posted is
        in reply to.  This implicitly sets the in_reply_to_user_id
        attribute of the resulting status to the user ID of the
        message being replied to.  Invalid/missing status IDs will be
        ignored. [Optional]
      link_title:
        The title the the link which the user post, if client do not want
        to  get the title itself ,please fill it with the link's url. [Optional]
      link_desc:
        Some word describe about the link which the user post, 
        if client do not want to  get the title itself ,
        please fill it with the link's url. [Optional]
      
    Returns:
      A renjian.Status instance representing the message posted.
    '''
    if not self._username:
      raise RenjianError("The renjian.Api instance must be authenticated.")

    url = 'http://api.renjian.com/statuses/update.json'

    if len(text) > CHARACTER_LIMIT:
      raise RenjianError("Text must be less than or equal to %d characters. "
                         "Consider using PostUpdates." % CHARACTER_LIMIT)
      
    if not original_url:
      raise RenjianError("original_url must not be null.")

    data = {'text': text,
            'status_type': 'LINK',
            'original_url': original_url}
    if in_reply_to_status_id:
      data['in_reply_to_status_id'] = in_reply_to_status_id
    if link_title:
      data['link_title'] = link_title
    if link_desc:
      data['link_desc'] = link_desc
    json = self._FetchUrl(url, post_data=data)
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return Status.NewFromJsonDict(data)

  def PostPicture(self):
    pass
    # TODO: status_type = 'PICTURE' 
  
  def GetFollowings(self, user=None):
    '''Fetch the sequence of renjian.User instances, one for each friend.

    Args:
      user: 
        the username or id of the user whose followings you are fetching.  If
        not specified, defaults to the authenticated user. [optional]

    The renjian.Api instance must be authenticated.

    Returns:
      A sequence of renjian.User instances, one for each friend
    '''
    if not self._username:
      raise RenjianError("renjian.Api instance must be authenticated")
    if user:
      url = 'http://api.renjian.com/statuses/friends/%s.json' % user 
    else:
      url = 'http://api.renjian.com/statuses/friends.json'
    json = self._FetchUrl(url)
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return [User.NewFromJsonDict(x) for x in data]

  def GetFollowers(self, user=None):
    '''Fetch the sequence of renjian.User instances, one for each follower
    
    Args:
      user: 
        the username or id of the user whose followers you are fetching.  If
        not specified, defaults to the authenticated user. [optional]

    The renjian.Api instance must be authenticated.

    Returns:
      A sequence of renjian.User instances, one for each follower
    '''
    if not self._username:
      raise RenjianError("renjian.Api instance must be authenticated")
    if user:
      url = 'http://api.renjian.com/statuses/followers/%s.json' % user 
    else:
      url = 'http://api.renjian.com/statuses/followers.json'
    json = self._FetchUrl(url)
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return [User.NewFromJsonDict(x) for x in data]

  def GetUser(self, user):
    '''Returns a single user.

    The renjian.Api instance must be authenticated.

    Args:
      user: The username or id of the user to retrieve.

    Returns:
      A renjian.User instance representing that user
    '''
    if not user:
      raise RenjianError("user must not be null")
    url = 'http://api.renjian.com/users/show/%s.json' % user
    json = self._FetchUrl(url)
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return User.NewFromJsonDict(data)

  def GetDirectMessages(self, count=None, since_id=None, page=None):
    '''Returns a list of the direct messages sent to the authenticating user.

    The renjian.Api instance must be authenticated.

    Args:
      count: 
        Specifies the number of statuses to retrieve. May not be
        greater than 500. [Optional]
      since_id:
        Returns only public statuses with an ID greater than (that is,
        more recent than) the specified ID. [Optional]
      page:
        ...

    Returns:
      A sequence of renjian.DirectMessage instances
    '''
    url = 'http://api.renjian.com/direct_messages/receive.json'
    if not self._username:
      raise RenjianError("The renjian.Api instance must be authenticated.")
    parameters = {}
    if count:
      parameters['count'] = since
    if since_id:
      parameters['since_id'] = since_id
    if page:
      parameters['page'] = page 
    json = self._FetchUrl(url, parameters=parameters)
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return [DirectMessage.NewFromJsonDict(x) for x in data]

  def GetDirectMessagesSent(self, count=None, since_id=None, page=None):
    '''Returns a list of the direct messages the authenticating user sent.

    The renjian.Api instance must be authenticated.

    Args:
      count: 
        Specifies the number of statuses to retrieve. May not be
        greater than 500. [Optional]
      since_id:
        Returns only public statuses with an ID greater than (that is,
        more recent than) the specified ID. [Optional]
      page:
        ...

    Returns:
      A sequence of renjian.DirectMessage instances
    '''
    url = 'http://api.renjian.com/direct_messages/sent.json'
    if not self._username:
      raise RenjianError("The renjian.Api instance must be authenticated.")
    parameters = {}
    if count:
      parameters['count'] = since
    if since_id:
      parameters['since_id'] = since_id
    if page:
      parameters['page'] = page 
    json = self._FetchUrl(url, parameters=parameters)
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return [DirectMessage.NewFromJsonDict(x) for x in data]

  def PostDirectMessage(self, user, text):
    '''Post a renjian direct message from the authenticated user

    The renjian.Api instance must be authenticated.

    Args:
      user: The ID or screen name of the recipient user.
      text: The message text to be posted.  Must be less than 140 characters.

    Returns:
      A renjian.DirectMessage instance representing the message posted
    '''
    if not self._username:
      raise RenjianError("The renjian.Api instance must be authenticated.")
    url = 'http://api.renjian.com/direct_messages/new.json'
    data = {'text': text, 
            'user': user}
    json = self._FetchUrl(url, post_data=data)
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return DirectMessage.NewFromJsonDict(data)

  def DestroyDirectMessage(self, id):
    '''Destroys the direct message specified in the required ID parameter.

    The renjian.Api instance must be authenticated, and the
    authenticating user must be the recipient of the specified direct
    message.

    Args:
      id: The id of the direct message to be destroyed

    Returns:
      A renjian.DirectMessage instance representing the message destroyed
    '''
    if not self._username:
      raise RenjianError("The renjian.Api instance must be authenticated.")
    url = 'http://api.renjian.com/direct_messages/destroy/%s.json' % id
    json = self._FetchUrl(url, post_data={})
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return DirectMessage.NewFromJsonDict(data)

  def CreateFriendship(self, user):
    '''Befriends the user specified in the user parameter as the authenticating user.

    The renjian.Api instance must be authenticated.

    Args:
      The ID or screen name of the user to befriend.
    Returns:
      A renjian.User instance representing the befriended user.
    '''
    if not self._username:
      raise RenjianError("The renjian.Api instance must be authenticated.")
    url = 'http://api.renjian.com/friendships/create.json'
    parameters = {}
    if user:
      parameters['user'] = user
    json = self._FetchUrl(url, post_data=parameters)
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return User.NewFromJsonDict(data)

  def DestroyFriendship(self, user):
    '''Discontinues friendship with the user specified in the user parameter.

    The renjian.Api instance must be authenticated.

    Args:
      The ID or screen name of the user  with whom to discontinue friendship.
    Returns:
      A renjian.User instance representing the discontinued friend.
    '''
    if not self._username:
      raise RenjianError("The renjian.Api instance must be authenticated.")
    url = 'http://api.renjian.com/friendships/destroy.json'
    parameters = {}
    if user:
      parameters['user'] = user
    json = self._FetchUrl(url, post_data=parameters)
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return User.NewFromJsonDict(data)

  def ExistFriendship(self, user_a, user_b):
    '''Test if user_a is following user_b
    
    Args:
      user_a: The ID or screen name of the user_a
      user_b: The ID or screen name of the user_b
    Returns:
      A boolean true if user_a is following user_b, else false.  
    '''  
    url = 'http://api.renjian.com/friendships/exists.json'
    parameters = {'user_a': user_a,
                  'user_b': user_b}
    json = self._FetchUrl(url, post_data=parameters)
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return data.is_follow # true or false

  def GetFollowingIds(self, id):
    # TODO: maybe need a constructor
    pass

  def GetFollowerIds(self, user):
    # TODO: maybe need a constructor
    pass

  def GetFavorites(self, page):
    '''Get the authenticating user's favorite status.
    Returns the favorite status when successful.

    The renjian instance must be authenticated.

    Args:
      The page of all the status.
    Returns:
      All the renjian.Status instance representing the user favorited.
    '''
    url = 'http://api.renjian.com/favorites/list.json'
    parameters = {'page': page}
    json = self._FetchUrl(url, post_data=parameters)
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return [Status.NewFromJsonDict(x) for x in data]

  def CreateFavorite(self, status):
    '''Favorites the status specified in the status parameter as the authenticating user.
    Returns the favorite status when successful.

    The renjian.Api instance must be authenticated.

    Args:
      The renjian.Status instance to mark as a favorite.
    Returns:
      A renjian.Status instance representing the newly-marked favorite.
    '''
    url = 'http://api.renjian.com/favorites/create/%s.json' % status.id
    json = self._FetchUrl(url, post_data={})
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return Status.NewFromJsonDict(data)

  def DestroyFavorite(self, status):
    '''Un-favorites the status specified in the ID parameter as the authenticating user.
    Returns the un-favorited status in the requested format when successful.

    The renjian.Api instance must be authenticated.

    Args:
      The renjian.Status to unmark as a favorite.
    Returns:
      A renjian.Status instance representing the newly-unmarked favorite.
    '''
    url = 'http://api.renjian.com/favorites/destroy/%s.json' % status.id
    json = self._FetchUrl(url, post_data={})
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return Status.NewFromJsonDict(data)

  def GetUserByEmail(self, email):
    '''Returns a single user by email address.

    Args:
      email: The email of the user to retrieve.
    Returns:
      A twitter.User instance representing that user
    '''
    url = 'http://twitter.com/users/show.json?email=%s' % email
    json = self._FetchUrl(url)
    data = simplejson.loads(json)
    self._CheckForRenjianError(data)
    return User.NewFromJsonDict(data)

  def SetCredentials(self, username, password):
    '''Set the username and password for this instance

    Args:
      username: The twitter username.
      password: The twitter password.
    '''
    self._username = username
    self._password = password

  def ClearCredentials(self):
    '''Clear the username and password for this instance
    '''
    self._username = None
    self._password = None

  def SetCache(self, cache):
    '''Override the default cache.  Set to None to prevent caching.

    Args:
      cache: an instance that supports the same API as the  twitter._FileCache
    '''
    self._cache = cache

  def SetUrllib(self, urllib):
    '''Override the default urllib implementation.

    Args:
      urllib: an instance that supports the same API as the urllib2 module
    '''
    self._urllib = urllib

  def SetCacheTimeout(self, cache_timeout):
    '''Override the default cache timeout.

    Args:
      cache_timeout: time, in seconds, that responses should be reused.
    '''
    self._cache_timeout = cache_timeout

  def SetUserAgent(self, user_agent):
    '''Override the default user agent

    Args:
      user_agent: a string that should be send to the server as the User-agent
    '''
    self._request_headers['User-Agent'] = user_agent

  def SetXTwitterHeaders(self, client, url, version):
    '''Set the X-Twitter HTTP headers that will be sent to the server.

    Args:
      client:
         The client name as a string.  Will be sent to the server as
         the 'X-Twitter-Client' header.
      url:
         The URL of the meta.xml as a string.  Will be sent to the server
         as the 'X-Twitter-Client-URL' header.
      version:
         The client version as a string.  Will be sent to the server
         as the 'X-Twitter-Client-Version' header.
    '''
    self._request_headers['X-Twitter-Client'] = client
    self._request_headers['X-Twitter-Client-URL'] = url
    self._request_headers['X-Twitter-Client-Version'] = version

  def SetSource(self, source):
    '''Suggest the "from source" value to be displayed on the Twitter web site.

    The value of the 'source' parameter must be first recognized by
    the Twitter server.  New source values are authorized on a case by
    case basis by the Twitter development team.

    Args:
      source:
        The source name as a string.  Will be sent to the server as
        the 'source' parameter.
    '''
    self._default_params['source'] = source

  def _BuildUrl(self, url, path_elements=None, extra_params=None):
    # Break url into consituent parts
    (scheme, netloc, path, params, query, fragment) = urlparse.urlparse(url)

    # Add any additional path elements to the path
    if path_elements:
      # Filter out the path elements that have a value of None
      p = [i for i in path_elements if i]
      if not path.endswith('/'):
        path += '/'
      path += '/'.join(p)

    # Add any additional query parameters to the query string
    if extra_params and len(extra_params) > 0:
      extra_query = self._EncodeParameters(extra_params)
      # Add it to the existing query
      if query:
        query += '&' + extra_query
      else:
        query = extra_query

    # Return the rebuilt URL
    return urlparse.urlunparse((scheme, netloc, path, params, query, fragment))

  def _InitializeRequestHeaders(self, request_headers):
    if request_headers:
      self._request_headers = request_headers
    else:
      self._request_headers = {}

  def _InitializeUserAgent(self):
    user_agent = 'Python-urllib/%s (python-twitter/%s)' % \
                 (self._urllib.__version__, __version__)
    self.SetUserAgent(user_agent)

  def _InitializeDefaultParameters(self):
    self._default_params = {}

  def _AddAuthorizationHeader(self, username, password):
    if username and password:
      basic_auth = base64.encodestring('%s:%s' % (username, password))[:-1]
      self._request_headers['Authorization'] = 'Basic %s' % basic_auth

  def _RemoveAuthorizationHeader(self):
    if self._request_headers and 'Authorization' in self._request_headers:
      del self._request_headers['Authorization']

  def _GetOpener(self, url, username=None, password=None):
    if username and password:
      self._AddAuthorizationHeader(username, password)
      handler = self._urllib.HTTPBasicAuthHandler()
      (scheme, netloc, path, params, query, fragment) = urlparse.urlparse(url)
      handler.add_password(Api._API_REALM, netloc, username, password)
      opener = self._urllib.build_opener(handler)
    else:
      opener = self._urllib.build_opener()
    opener.addheaders = self._request_headers.items()
    return opener

  def _Encode(self, s):
    if self._input_encoding:
      return unicode(s, self._input_encoding).encode('utf-8')
    else:
      return unicode(s).encode('utf-8')

  def _EncodeParameters(self, parameters):
    '''Return a string in key=value&key=value form

    Values of None are not included in the output string.

    Args:
      parameters:
        A dict of (key, value) tuples, where value is encoded as
        specified by self._encoding
    Returns:
      A URL-encoded string in "key=value&key=value" form
    '''
    if parameters is None:
      return None
    else:
      return urllib.urlencode(dict([(k, self._Encode(v)) for k, v in parameters.items() if v is not None]))

  def _EncodePostData(self, post_data):
    '''Return a string in key=value&key=value form

    Values are assumed to be encoded in the format specified by self._encoding,
    and are subsequently URL encoded.

    Args:
      post_data:
        A dict of (key, value) tuples, where value is encoded as
        specified by self._encoding
    Returns:
      A URL-encoded string in "key=value&key=value" form
    '''
    if post_data is None:
      return None
    else:
      return urllib.urlencode(dict([(k, self._Encode(v)) for k, v in post_data.items()]))

  def _CheckForRenjianError(self, data):
    """Raises a TwitterError if twitter returns an error message.

    Args:
      data: A python dict created from the Twitter json response
    Raises:
      TwitterError wrapping the twitter error message if one exists.
    """
    # Twitter errors are relatively unlikely, so it is faster
    # to check first, rather than try and catch the exception
    if 'error' in data:
      raise RenjianError(data['error'])

  def _FetchUrl(self,
                url,
                post_data=None,
                parameters=None,
                no_cache=None):
    '''Fetch a URL, optionally caching for a specified time.

    Args:
      url: The URL to retrieve
      post_data: 
        A dict of (str, unicode) key/value pairs.  If set, POST will be used.
      parameters:
        A dict whose key/value pairs should encoded and added 
        to the query string. [OPTIONAL]
      no_cache: If true, overrides the cache on the current request

    Returns:
      A string containing the body of the response.
    '''
    # Build the extra parameters dict
    extra_params = {}
    if self._default_params:
      extra_params.update(self._default_params)
    if parameters:
      extra_params.update(parameters)

    # Add key/value parameters to the query string of the url
    url = self._BuildUrl(url, extra_params=extra_params)

    # Get a url opener that can handle basic auth
    opener = self._GetOpener(url, username=self._username, password=self._password)

    encoded_post_data = self._EncodePostData(post_data)

    # Open and return the URL immediately if we're not going to cache
    if encoded_post_data or no_cache or not self._cache or not self._cache_timeout:
      url_data = opener.open(url, encoded_post_data).read()
      opener.close()
    else:
      # Unique keys are a combination of the url and the username
      if self._username:
        key = self._username + ':' + url
      else:
        key = url

      # See if it has been cached before
      last_cached = self._cache.GetCachedTime(key)

      # If the cached version is outdated then fetch another and store it
      if not last_cached or time.time() >= last_cached + self._cache_timeout:
        url_data = opener.open(url, encoded_post_data).read()
        opener.close()
        self._cache.Set(key, url_data)
      else:
        url_data = self._cache.Get(key)

    # Always return the latest version
    return url_data


class _FileCacheError(Exception):
  '''Base exception class for FileCache related errors'''


class _FileCache(object):

  DEPTH = 3

  def __init__(self,root_directory=None):
    self._InitializeRootDirectory(root_directory)

  def Get(self,key):
    path = self._GetPath(key)
    if os.path.exists(path):
      return open(path).read()
    else:
      return None

  def Set(self,key,data):
    path = self._GetPath(key)
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
      os.makedirs(directory)
    if not os.path.isdir(directory):
      raise _FileCacheError('%s exists but is not a directory' % directory)
    temp_fd, temp_path = tempfile.mkstemp()
    temp_fp = os.fdopen(temp_fd, 'w')
    temp_fp.write(data)
    temp_fp.close()
    if not path.startswith(self._root_directory):
      raise _FileCacheError('%s does not appear to live under %s' %
                            (path, self._root_directory))
    if os.path.exists(path):
      os.remove(path)
    os.rename(temp_path, path)

  def Remove(self,key):
    path = self._GetPath(key)
    if not path.startswith(self._root_directory):
      raise _FileCacheError('%s does not appear to live under %s' %
                            (path, self._root_directory ))
    if os.path.exists(path):
      os.remove(path)

  def GetCachedTime(self,key):
    path = self._GetPath(key)
    if os.path.exists(path):
      return os.path.getmtime(path)
    else:
      return None

  def _GetUsername(self):
    '''Attempt to find the username in a cross-platform fashion.'''
    try:
      return os.getenv('USER') or \
             os.getenv('LOGNAME') or \
             os.getenv('USERNAME') or \
             os.getlogin() or \
             'nobody'
    except (IOError, OSError), e:
      return 'nobody'

  def _GetTmpCachePath(self):
    username = self._GetUsername()
    cache_directory = 'python.cache_' + username
    return os.path.join(tempfile.gettempdir(), cache_directory)

  def _InitializeRootDirectory(self, root_directory):
    if not root_directory:
      root_directory = self._GetTmpCachePath()
    root_directory = os.path.abspath(root_directory)
    if not os.path.exists(root_directory):
      os.mkdir(root_directory)
    if not os.path.isdir(root_directory):
      raise _FileCacheError('%s exists but is not a directory' %
                            root_directory)
    self._root_directory = root_directory

  def _GetPath(self,key):
    try:
        hashed_key = md5(key).hexdigest()
    except TypeError:
        hashed_key = md5.new(key).hexdigest()
        
    return os.path.join(self._root_directory,
                        self._GetPrefix(hashed_key),
                        hashed_key)

  def _GetPrefix(self,hashed_key):
    return os.path.sep.join(hashed_key[0:_FileCache.DEPTH])
