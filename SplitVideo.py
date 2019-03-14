from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import argparse
import time
import IPython
import os, fnmatch
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--path")
args = parser.parse_args()
# ffmpeg_extract_subclip("full.mp4", start_seconds, end_seconds, targetname="cut.mp4")

def get_all_file(path):
	array_video = []
	listOfFiles = os.listdir(path)
	pattern = "*.mp4"
	for entry in listOfFiles:
		if fnmatch.fnmatch(entry, pattern):
			array_video.append(entry)
	array_video = np.asarray(array_video)
	print("get all file done", array_video.shape)
	return array_video

def sub_clip_data(args):
	array_video = get_all_file(args.path)

	for name in array_video:
		data = name.split('_')
		newname = data[0]
		dir_path = os.getcwd().replace('\\','/')
		start_second = int(data[2])
		end_seconds = int(data[3].replace('.mp4',''))
		input_video = str(args.path + '/' + name)
		output_video = str(dir_path + '/' + newname + '_'+ data[1] + '.mp4')
		print("start_second", start_second, "end_seconds", end_seconds,"input_video", input_video, 'output_video', output_video)
		#IPython.embed()
		ffmpeg_extract_subclip(input_video, start_second, end_seconds, targetname=output_video)
		
		#remove_file(input_video)

def remove_file(path):
	os.remove(path)

while (1):
	sub_clip_data(args)
	time.sleep(30)
	pass