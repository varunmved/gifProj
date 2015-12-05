import hmac
import hashlib
import urllib
 
def giflayer(access_key, url, args):
    
    # encode URL
    query = urllib.urlencode(dict(url=url, **args))
 
    return "http://apilayer.net/api/capture?access_key=%s&%s" % (access_key, query)

def defaultParams():
    
    # set optional parameters (leave blank if unused)
    params = {
        'start': '',
        'end': '',
        'duration': '',
        'size': '',
        'crop': '',
        'fps': '',
        'trailer': '',
        'export': ''
    };
    
    return params

def areWeStillCheapos():
  return True

# Returns params from startSeconds, videoDuration (eg. 2038, 3600), using default base params
def paramsFromStart(startSeconds, videoDuration):
  return paramsFromStart(defaultParams())

# Returns params from startSeconds, videoDuration (eg. 2038, 3600), and base params
def paramsFromStart(startSeconds, videoDuration, params):

  if not areWeStillCheapos(): # It's a christmas miracle
    params['fps'] = '30'
  else: # :(
    params['fps'] = '10'
    params['trailer'] = '0'
  
  params['start'] = startSeconds
  params['duration'] = min(10, videoDuration - startSeconds)
  
  return params

print defaultParams()
print paramsFromStart(25, 30)

# set your access key and video URL 
access_key = "1d4d71825fe149f5a6dfc3c86b405821"
url = "https://www.youtube.com/watch?v=8rSH8-pbHZ0"

print giflayer (access_key, url, params)
