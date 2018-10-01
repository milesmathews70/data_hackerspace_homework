#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np
import math

def histogram_times(filename):
    times = [0] * 24
    x = 0
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    with open(filename) as f:
        csv_reader = csv.reader(f)
        airplane_crashes = list(csv_reader)
        for plane in airplane_crashes[1:]:
            if plane[1]:
                crash = plane[1]
                for letter in letters:
                    if str(letter) in str(crash):
                        x = 1
                        break
                if x != 1:
                    if '.' in crash:
                        l = str(crash).split('.')
                        if int((l[0])[0]) == 0:
                            times[int((l[0])[1])] += 1
                        else:
                            if (int(l[0]) > 23):
                                times = times
                            else:
                                times[int(l[0])] += 1
                    l = str(crash).split(':')
                    if int((l[0])[0]) == 0:
                        times[int((l[0])[1])] += 1
                    else:
                        if (int(l[0]) > 23):
                            times = times
                        else:
                            times[int(l[0])] += 1
    return times

def weigh_pokemons(filename, weight):
    returnpokemon = list()
    with open(filename) as f:
        data = json.load(f)
        for pokemon in data['pokemon']:
            splitweight = pokemon['weight'].split(" ")
            realweight = float(splitweight[0])
            if realweight == weight:
                returnpokemon.append(pokemon['name'])
    return returnpokemon

def single_type_candy_count(filename):
    count = 0
    with open(filename) as f:
        data = json.load(f)
        for pokemon in data['pokemon']:
                if len(pokemon['type']) == 1:
                    if 'candy_count' in pokemon:
                        count += pokemon['candy_count']
    return count

def reflections_and_projections(points):
    returnpoints = np.array(points)
    returnpoints *= [[0], [-1]]
    returnpoints += [[0], [1]]
    returnpoints *= [[1/math.sqrt(2), -1/math.sqrt(2)], [1/math.sqrt(2), 1/math.sqrt(2)]]
    returnpoints *= (1//10) * [[1, 3], [3, 9]]
    return returnpoints

def normalize(image):
    pic = image
    maxnum = np.amax(pic)
    minnum = np.amin(pic)
    for pixel in pic.flat:
        pixel *= float((255/(maxnum-minnum))*(pixel-minnum))
    return pic
def sigmoid_normalize(image):
    pass
