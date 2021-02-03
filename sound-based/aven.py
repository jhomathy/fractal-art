import numpy as np
import simpleaudio as sa
import random

def fun_sound():

	# calculate note frequencies
	A_freq = 440

	scale = [A_freq * 2 ** (i / 12) for i in range(12)]

	# get timesteps for each sample, T is note duration in seconds
	sample_rate = 44100
	T = 0.5
	t = np.linspace(0, T, int(T * sample_rate), False)

	# generate sine wave notes

	notes = [random.choice(scale) for i in range(3)]

	note1 = np.sin(notes[0] * t * 2 * np.pi)
	note2 = np.sin(notes[1] * t * 2 * np.pi)
	note3 = np.sin(notes[2] * t * 2 * np.pi)

	# mix audio together
	audio = np.zeros((44100, 2))
	n = len(t)
	offset = 0
	audio[0 + offset: n + offset, 0] += note1
	audio[0 + offset: n + offset, 1] += 0.125 * note1
	offset = 5500
	audio[0 + offset: n + offset, 0] += 0.5 * note2
	audio[0 + offset: n + offset, 1] += 0.5 * note2
	offset = 11000
	audio[0 + offset: n + offset, 0] += 0.125 * note3
	audio[0 + offset: n + offset, 1] += note3

	# normalize to 16-bit range
	audio *= 32767 / np.max(np.abs(audio))
	# convert to 16-bit data
	audio = audio.astype(np.int16)

	return(audio)

loop = [fun_sound(), fun_sound(), fun_sound(), fun_sound()]
loop4 = loop * 4
sound = np.concatenate(loop4)

# start playback
play_obj = sa.play_buffer(sound, 2, 2, sample_rate)

# wait for playback to finish before exiting
play_obj.wait_done()
