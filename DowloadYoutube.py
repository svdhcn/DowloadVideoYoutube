import pytube
import csv
import numpy as np
import IPython
import argparse
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

import pandas as pd

import os, fnmatch

youtube_id = []

parser = argparse.ArgumentParser()
parser.add_argument("--csv")
parser.add_argument("--path")
args = parser.parse_args()

#print (args.echo)

# dowload video youtube
from pytube import YouTube
import os

def downloadYouTube(args):
	#list_youtube = np.asarray(youtube_id[int(args.start_index):int(args.end_index)])
	if not os.path.exists(args.path):
			os.makedirs(args.path)
			print("Create new forlder done!")
	dataset = pd.read_csv(args.csv)
	'''dataset.values.shape[0]'''
	for index in range(1, dataset.values.shape[0]):
		url = 'https://www.youtube.com/watch?v=' + dataset.iloc[index][1]
		newName = str(dataset.iloc[index][0])+'_'+ str(dataset.iloc[index][1])+'_'+str(dataset.iloc[index][2])+'_'+str(dataset.iloc[index][3])+".mp4"
		print(url)
		try:
			yt = YouTube(url)
			nameVideo = yt.title
			stream = yt.streams.filter(res = "360p").filter(progressive=True).filter(subtype='mp4').first()
			stream.download(output_path= args.path, filename=newName)
					
		except:
			print('The ID of video is wrong !!!')

downloadYouTube(args)
