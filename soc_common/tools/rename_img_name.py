# -*- encoding: utf-8 -*-

from soc_common.utils import str_utils, file_utils, log_utils
import os
import sys
import re

import multiprocessing
import traceback

import exifread


def get_img_create_time(path):
  f = open(path, 'rb')

  try:
    tags = exifread.process_file(f)

    dt = tags.get('EXIF DateTimeOriginal', None) if tags.get(
        'EXIF DateTimeOriginal', None) != None else tags.get('Image DateTime', '')
    dt = str(dt).replace(' ', '_').replace(':', '')
    return dt
  except Exception as e:
    log_utils.get_logger('.\\rename_error.log').info(traceback.format_exc())
    return None
  finally:
    f.close()


def video_duration_3(filename):
  cap = cv2.VideoCapture(filename)
  if cap.isOpened():
    rate = cap.get(5)
    frame_num = cap.get(7)
    duration = frame_num / rate
    return duration
  return -1


def rename(olgImgPath, newImgPath, oldNefPath, newNefPath):
  file_utils.move(olgImgPath, newImgPath)
  if file_utils.is_file(oldNefPath):
    file_utils.move(oldNefPath, newNefPath)


def rename_img(imgInfo):
  global img_name
  # print(floder

  if '.nef' in imgInfo[1][-4:].lower():
    return None
  olgImgPath = '%s\\%s' % (imgInfo[0], imgInfo[1])
  dt = get_img_create_time(olgImgPath)
  if None == dt or '' == dt:
    dt = imgInfo[1][0:imgInfo[1].rfind('.')]

  suf = file_utils.get_file_suffix(imgInfo[1])
  nef = 'NEF'

  newImgPath = '%s\\%s_%s.%s' % (imgInfo[0], img_name, dt, suf)

  oldNefPath = '%s\\%s' % (imgInfo[0], imgInfo[1].replace(suf, nef))
  newNefPath = '%s\\%s_%s.%s' % (imgInfo[0], img_name, dt, nef)

  if not file_utils.is_file(newImgPath):
    rename(olgImgPath, newImgPath, oldNefPath, newNefPath)
    return ''

  for i in range(1, 100):

    newImgPath = '%s\\%s_%s_%d.%s' % (imgInfo[0], img_name, dt, i, suf)
    newNefPath = '%s\\%s_%s_%d.%s' % (imgInfo[0], img_name, dt, i, nef)

    if not file_utils.is_file(newImgPath):
      rename(olgImgPath, newImgPath, oldNefPath, newNefPath)
      return ''
  return None


def walk2(path):
  ''' 
      列举path下的所有文件、文件夹
  '''
  fpaths = []
  for pt, fl, fi in os.walk(path):
    for f in fi:
      p = os.path.join(pt, f)
      fpaths.append((pt, f))
  return fpaths


def main():
  path = u'F:\\MT7-CL00'

  paths = walk2(path)
  cpu_count = multiprocessing.cpu_count()
  print(paths)
  pool = multiprocessing.Pool(processes=cpu_count)

  print(pool.map(rename_img, paths))

  # print(rename_img(paths[0])


img_name = u'YH-MT7'

# img_name = u'桃花村鲜花港'

if __name__ == '__main__':
  # sys.setdefaultencoding('utf-8')

  path = u'F:\\MT7-CL00'
  main(path)

  # p = 'xx.xx.jpg'
  # # print(
  # print(p[0:p.rfind('.')]

  # print(file_helper.get_file_suffix(u'DSC_4877.JPG')
