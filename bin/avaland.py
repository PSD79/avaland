#! /usr/bin/python3

from avaland.manager import SourceManager
from avaland.sources import *
import argparse

parser = argparse.ArgumentParser(description='Avaland Music Downloader')
parser.add_argument("--query", type=str,
                    help='an integer for the accumulator')

args = parser.parse_args()


def print_result(source, data, counter):
    print(source.title(), "results: ")
    for i in data.to_dict().keys():
        for j in range(3):
            if len(data.to_dict()[i]) - 1 < j:
                break
            if i == 'musics' or i == 'albums':
                print("\t", "%s- (%s)" % (counter, i), " -> ", data.to_dict()[i][j]['full_title'])
            elif i == 'artists':
                print("\t", "%s- (%s)" % (counter, i), " -> ", data.to_dict()[i][j]['full_name'])
            items.append(data.to_dict()[i][j])
            counter += 1
            print()

    return counter


if __name__ == '__main__':
    items = []
    counter = 1
    print("LOL")
    manager = SourceManager()
    print("lol2")
    manager.register(Bia2)
    manager.register(Nex1)
    manager.register(RapFarsi)
    print('lol3')
    search = manager.search(args.query)
    print("lol4")
    for source in search.keys():
        counter = print_result(source, search[source], counter)
    _input = input("select item to download (q for exit): ")
    if _input == "q":
        exit()
    print(items[int(_input) - 1])
