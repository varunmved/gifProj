import re

def commentHasTimes(comment):
  return len(timesInComment(comment)) > 0

def timesInComment(comment):
  split = comment.split()
  times = []
  r = re.compile('(\d{1,2}:){1,2}\d\d')
  for word in split:
    if (r.match(word)):
      times.append(secondsIn(word))
  return times

def secondsIn(timeString):
  nums = timeString.split(':');
  secs = int(0)
  for num in nums:
    secs = secs * 60
    secs = secs + int(num)
  return secs

def formatTime(timeString):
  l = len(timeString)
  if (l == 4 || l == 6 || l == 7):
    return formatTime('0' + timeString)
  if (l == 5):
    return formatTime(':' + timeString)
  return timeString

#print secondsIn('60')
#print secondsIn('1:00')
#print secondsIn('1:60')

#print timesInComment("01:12:12 asdfasdf 1:2:05 1::3 :23 23 4:5  5:05 a3:45  1:13:40", "")
