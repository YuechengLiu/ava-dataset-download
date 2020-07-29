import pandas as pd 
import requests
import time 
import os 

if not os.path.exists('./test_videos'):
    os.mkdir('./test_videos')
if not os.path.exists('./train_val_videos'):
    os.mkdir('./train_val_videos')

train_val_videos = pd.read_csv('train_val_video_names.txt', header=None).values.reshape(-1)
test_videos = pd.read_csv('test_video_names.txt', header=None).values.reshape(-1)

url_train_val = 'https://s3.amazonaws.com/ava-dataset/trainval/'
url_test = 'https://s3.amazonaws.com/ava-dataset/test/'

for i in range(train_val_videos.shape[0]):
    filename = train_val_videos[i]
    if filename in os.listdir('./train_val_videos/'):
        print('skip {}'.format(filename))
        continue
    file_url = url_train_val + filename
    outfile = './train_val_videos/' + filename
    print('begin to download file {}'.format(filename))
    time_start = time.time()
    try:
        r = requests.get(file_url)
        with open(outfile, 'wb') as f:
            f.write(r.content)
    except:
        with open('failed_train_val_videos.txt', 'a+') as f:
            f.write(filename + '\n')
    else:
        print('video {} has been download sucessfully, time consumption: {} s'.format(
            filename, time.time() - time_start))


for i in range(test_videos.shape[0]):
    filename = test_videos[i]
    if filename in os.listdir('./test_videos/'):
        print('skip {}'.format(filename))
        continue
    file_url = url_test + filename
    outfile = './test_videos/' + filename
    print('begin to download file {}'.format(filename))
    time_start = time.time()
    try:
        r = requests.get(file_url)
        with open(outfile, 'wb') as f:
            f.write(r.content)
    except:
        with open('failed_test_videos.txt', 'a+') as f:
            f.write(filename + '\n')
    else:
        print('video {} has been download sucessfully, time consumption: {} s'.format(
             filename, time.time() - time_start))
