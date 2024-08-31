# -*- encoding: utf-8 -*-

from soc_common.utils import str_utils, file_utils, log_utils
import os
import sys
import re
import cv2
import time

import multiprocessing
import traceback

import exifread

# import pytz
import datetime
from win32com.propsys import propsys, pscon

from PIL import Image
import piexif
import pillow_heif

def get_img_create_time(path):
  f = open(path, 'rb')
  suf = file_utils.get_file_suffix(path).lower()
  try:
    dt = ''
    if suf == 'heic':
      # heif_file = pillow_heif.read_heif(path)
      heif_file = pillow_heif.open_heif(path, convert_hdr_to_8bit=False)
      if heif_file.info.get("exif", None):
        exif_dict = piexif.load(heif_file.info["exif"], key_is_name=True)
        dt = exif_dict.get('Exif', {}).get('DateTimeOriginal', '')
    else:
      tags = exifread.process_file(f)
      dt = tags.get('EXIF DateTimeOriginal', None) if tags.get(
          'EXIF DateTimeOriginal', None) != None else tags.get('Image DateTime', '')
    if dt == '':
      dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.stat(path).st_mtime))
    dt = str(dt).replace(' ', '_').replace('-', '').replace(':', '').replace('b', '').replace('\'', '')
    if len(dt) > 15:
      return dt[0:15]
    return dt
  except Exception as e:
    print(traceback.format_exc())
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.stat(path).st_mtime))
    dt = str(dt).replace(' ', '_').replace('-', '').replace(':', '').replace('b', '').replace('\'', '')
    return dt
  finally:
    f.close()


def get_video_time(filename):
  try:

    properties = propsys.SHGetPropertyStoreFromParsingName(filename)
    dt = properties.GetValue(pscon.PKEY_Media_DateEncoded).GetValue()
    if not isinstance(dt, datetime.datetime):
      # In Python 2, PyWin32 returns a custom time type instead of
      # using a datetime subclass. It has a Format method for strftime
      # style formatting, but let's just convert it to datetime:
      if dt == None:
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.stat(filename).st_mtime))
        dt = str(dt).replace(' ', '_').replace('-', '').replace(':', '').replace('b', '').replace('\'', '')
        return dt

      dt = datetime.datetime.fromtimestamp(int(dt))
      dt = dt.replace(tzinfo=pytz.timezone('UTC'))
    dt = dt.astimezone(datetime.timezone(datetime.timedelta(hours=8)))
    return dt.strftime("%Y%m%d_%H%M%S")
  except Exception as e:
    # print("filename:"+filename + "; " + traceback.format_exc())
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.stat(filename).st_mtime))
    dt = str(dt).replace(' ', '_').replace('-', '').replace(':', '').replace('b', '').replace('\'', '')
    return dt
  finally:
    pass


def get_video_duration(filename):
  """_summary_

  Args:
      filename (_type_): _description_
以下是opencv-python可以获取视频的相关信息，可以通过从0开始的序号获取
CV_CAP_PROP_POS_MSEC 视频文件的当前位置（以毫秒为单位）或视频捕获时间戳。
CV_CAP_PROP_POS_FRAMES 接下来要解码/捕获的帧的基于0的索引。
CV_CAP_PROP_POS_AVI_RATIO 视频文件的相对位置：0 - 电影的开始，1 - 电影的结尾。
CV_CAP_PROP_FRAME_WIDTH 视频流中帧的宽度。
CV_CAP_PROP_FRAME_HEIGHT 视频流中帧的高度。
CV_CAP_PROP_FPS 帧速率。
CV_CAP_PROP_FOURCC 编解码器的4字符代码。
CV_CAP_PROP_FRAME_COUNT 视频文件中的帧数。
CV_CAP_PROP_FORMAT 返回的Mat对象的格式 retrieve() 。
CV_CAP_PROP_MODE 指示当前捕获模式的特定于后端的值。
CV_CAP_PROP_BRIGHTNESS 图像的亮度（仅适用于相机）。
CV_CAP_PROP_CONTRAST 图像对比度（仅适用于相机）。
CV_CAP_PROP_SATURATION 图像的饱和度（仅适用于相机）。
CV_CAP_PROP_HUE 图像的色调（仅适用于相机）。
CV_CAP_PROP_GAIN 图像的增益（仅适用于相机）。
CV_CAP_PROP_EXPOSURE 曝光（仅适用于相机）。
CV_CAP_PROP_CONVERT_RGB 布尔标志，指示是否应将图像转换为RGB。
CV_CAP_PROP_WHITE_BALANCE_U 白平衡设置的U值（注意：目前仅支持DC1394 v 2.x后端）
CV_CAP_PROP_WHITE_BALANCE_V 白平衡设置的V值（注意：目前仅支持DC1394 v 2.x后端）
CV_CAP_PROP_RECTIFICATION 立体摄像机的整流标志（注意：目前仅支持DC1394 v 2.x后端）
CV_CAP_PROP_ISO_SPEED摄像机 的ISO速度（注意：目前仅支持DC1394 v 2.x后端）
CV_CAP_PROP_BUFFERSIZE 存储在内部缓冲存储器中的帧数（注意：目前仅支持DC1394 v 2.x后端）
  Returns:
      _type_: _description_
  """
  cap = cv2.VideoCapture(filename)
  if cap.isOpened():
    rate = cap.get(cv2.CAP_PROP_FPS)
    frame_num = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    duration = frame_num / rate

    if duration > 120:
      return str(int(duration / 60)) + 'm' + str(int(duration % 60)) + 's'
    return str(int(duration)) + 's'
  return ''


def rename(olgImgPath, newImgPath, oldNefPath='', newNefPath=''):
  file_utils.move(olgImgPath, newImgPath)
  if file_utils.is_file(oldNefPath):
    file_utils.move(oldNefPath, newNefPath)


def rename_img(imgInfo):
  global pre_name
  olgImgPath = os.path.join(imgInfo[0], imgInfo[1])

  dt = get_img_create_time(olgImgPath)
  if None == dt or '' == dt:
    dt = imgInfo[1][0:imgInfo[1].rfind('.')]

  suf = file_utils.get_file_suffix(imgInfo[1])
  nef = 'NEF'

  newImgPath = os.path.join(imgInfo[0], pre_name+'_'+dt+'.'+suf)

  oldNefPath = os.path.join(imgInfo[0], imgInfo[1].replace(suf, nef))
  newNefPath = os.path.join(imgInfo[0], pre_name+'_'+dt+'.'+nef)

  if not file_utils.is_file(newImgPath):
    rename(olgImgPath, newImgPath, oldNefPath, newNefPath)
    return ''

  for i in range(1, 100):

    newImgPath = os.path.join(imgInfo[0], pre_name+'_'+dt+'_'+str(i)+'.'+suf)
    newNefPath = os.path.join(imgInfo[0], pre_name+'_'+dt+'_'+str(i)+'.'+nef)

    if not file_utils.is_file(newImgPath):
      rename(olgImgPath, newImgPath, oldNefPath, newNefPath)
      return ''
  return None


def rename_video(imgInfo):
  global pre_name
  filePath = os.path.join(imgInfo[0], imgInfo[1])

  dt = get_video_time(filePath)
  if None == dt or '' == dt:
    dt = imgInfo[1][0:imgInfo[1].rfind('.')]

  durationStr = get_video_duration(filePath)
  dt += '_'+durationStr

  suf = file_utils.get_file_suffix(imgInfo[1])

  newVideoPath = os.path.join(imgInfo[0], pre_name+'_'+dt+'.'+suf)

  rename(filePath, newVideoPath)


def rename_file(fileInfo):
  global pre_name

  suf = file_utils.get_file_suffix(fileInfo[1]).lower()

  if 'nef' == suf or 'db' == suf:
    return None

  if suf in ['png', 'jpg', 'jpeg', 'bmp', 'heic', 'dng']:
    rename_img(fileInfo)
    return

  if suf in ['flv', 'avi', 'mov', 'mp4', 'wmv', 'mpeg', 'mpg']:
    rename_video(fileInfo)
    return
  print('no match path: '+ os.path.join(fileInfo[0], fileInfo[1]))


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
  path = u'F:\\2024-07新疆'

  paths = walk2(path)
  cpu_count = multiprocessing.cpu_count()
  print(paths)
  pool = multiprocessing.Pool(processes=cpu_count)

  print(pool.map(rename_file, paths))

  # dt = get_video_time('F:\\YH-iPhone14\\YH-iPhone0911.MOV')
  
  # dt = get_img_create_time('F:\\YH-iPhone14\\YH-iPhone2676.DNG')
  # print(dt)


#
pre_name = u'新疆'

# pre_name = u'桃花村鲜花港'

if __name__ == '__main__':
  # sys.setdefaultencoding('utf-8')

  main()

  # p = 'xx.xx.jpg'
  # # print(
  # print(p[0:p.rfind('.')]

  # print(file_helper.get_file_suffix(u'DSC_4877.JPG')



# 0th:
#   Make: b'Apple'
#   Model: b'iPhone 7 Plus'
#   Orientation: 6
#   XResolution: (72, 1)
#   YResolution: (72, 1)
#   ResolutionUnit: 2
#   Software: b'15.7.5'
#   DateTime: b'2023:04:29 15:47:06'
#   HostComputer: b'iPhone 7 Plus'
#   ExifTag: 224
#   GPSTag: 2076
# Exif:
#   ExposureTime: (1, 33)
#   FNumber: (9, 5)
#   ExposureProgram: 2
#   ISOSpeedRatings: 25
#   ExifVersion: b'0232'
#   DateTimeOriginal: b'2023:04:29 15:47:06'
#   DateTimeDigitized: b'2023:04:29 15:47:06'
#   OffsetTime: b'+08:00'
#   OffsetTimeOriginal: b'+08:00'
#   OffsetTimeDigitized: b'+08:00'
#   ShutterSpeedValue: (62913, 12436)
#   ApertureValue: (54823, 32325)
#   BrightnessValue: (53456, 12121)
#   ExposureBiasValue: (0, 1)
#   MeteringMode: 5
#   Flash: 16
#   FocalLength: (399, 100)
#   SubjectArea: (1069, 1662, 431, 429)
#   MakerNote: 1252 bytes.
#   SubSecTimeOriginal: b'472'
#   SubSecTimeDigitized: b'472'
#   ColorSpace: 65535
#   PixelXDimension: 4032
#   PixelYDimension: 3024
#   SensingMethod: 2
#   SceneType: b'\x01'
#   ExposureMode: 0
#   WhiteBalance: 0
#   FocalLengthIn35mmFilm: 28
#   LensSpecification: ((399, 100), (33, 5), (9, 5), (14, 5))
#   LensMake: b'Apple'
#   LensModel: 43 bytes.
# 1st:
# GPS:
#   GPSLatitudeRef: b'N'
#   GPSLatitude: ((30, 1), (29, 1), (1794, 100))
#   GPSLongitudeRef: b'E'
#   GPSLongitude: ((119, 1), (39, 1), (1451, 100))
#   GPSAltitudeRef: 0
#   GPSAltitude: (1083105, 6497)
#   GPSSpeedRef: b'K'
#   GPSSpeed: (0, 1)
#   GPSImgDirectionRef: b'T'
#   GPSImgDirection: (205202, 805)
#   GPSDestBearingRef: b'T'
#   GPSDestBearing: (205202, 805)
#   GPSDateStamp: b'2023:04:29'
#   GPSHPositioningError: (164501, 3721)
# Interop:
# thumbnail: