#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'zak'
import sys
import ast
import argparse
import operator
import collections
from os import path, listdir


def main(data_file=None, multiple_files=None):
    """
    team_points --> '{name: points}' this is the format of the object tracking the team points
    :param data_file: Parameter to be passed in, represents a single file
    :param multiple_files: Parameter to be passed in, represents a single to many files
    Prints Results at end.
    """
    team_points = {}
    if data_file:
        team_points = calculate([data_file], team_points)
    if multiple_files:
        try:
            files = ast.literal_eval(multiple_files)
            team_points = calculate(files, team_points)
        except:
            if not data_file and not path.exists(multiple_files):
                sys.exit('String given is not in a list format or path given does not exist')
            filelist = ['{}/{}'.format(multiple_files, f) for f in listdir(multiple_files)]
            team_points = calculate(filelist, team_points)
    team_points = collections.OrderedDict(sorted(team_points.items()))
    team_points = sorted(team_points.items(), key=operator.itemgetter(1), reverse=True)
    prev_value = None
    prev_rank = None
    outliner = 0
    for i, item in enumerate(team_points, start=1):
        i -= outliner
        if prev_value == item[1]:
            i = prev_rank
            outliner += 1
        else:
            prev_value = item[1]
        prev_rank = i
        print('{}. {}, {}'.format(i, item[0], '{} {}'.format(item[1], 'pts' if item[1] != 1 else 'pt')))


def calculate(files, team_points):
    for score_file in files:
        with open(score_file, 'r') as readfile:
            file_data = readfile.readlines()
            for item in file_data:
                teams = item.strip('\n').split(',')
                first_team = teams[0][:teams[0].rfind(' ')].lstrip()
                first_team_score = teams[0][teams[0].rfind(' '):].lstrip()
                second_team = teams[1][:teams[1].rfind(' ')].lstrip()
                second_team_score = teams[1][teams[1].rfind(' '):].lstrip()
                if first_team_score == second_team_score:
                    first_team_points = second_team_points = 1
                elif first_team_score > second_team_score:
                    first_team_points = 3
                    second_team_points = 0
                elif first_team_score < second_team_score:
                    first_team_points = 0
                    second_team_points = 3
                team_points[first_team] = int(team_points.get(first_team, 0)) + first_team_points
                team_points[second_team] = int(team_points.get(second_team, 0)) + second_team_points
    return team_points


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Print points for Teams entered.')
    parser.add_argument('--file', type=str, help="python script.py --file /tmp/data  (Please specify full path ....e.g. /tmp/file.txt)")
    parser.add_argument('--multiple_files', type=str, help="""
    python script.py --multiple_files  "['/tmp/data.txt','/tmp/data1.txt', '/tmp/data1.txt']" or\
    If you enter the directory containing all the files, it will grab all the files in that directory.""")

    args = parser.parse_args()
    if args.file or args.multiple_files:
        main(args.file, args.multiple_files)
    else:
        print("""Please provide a valid Command e.g.:\n
1) python script.py --file  /tmp/data.txt\n
2) python script.py --multiple_files  ['/tmp/data.txt', '/tmp/data1.txt', '/tmp/data1.txt'] or python script.py --multiple_files /tmp/
-> all two options can be given at the same time, It will however join the results""")


