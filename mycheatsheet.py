#!/usr/bin/python3

import yaml
import json
import sys
import hashlib
import getopt


def help():
    print("ADD    | mycheatsheet.py -a <alias> -d <description> -c <command>")
    print("REMOVE | mycheatsheet.py rm <id> OR <alias> ")
    print("LIST   | mycheatsheet.py list ")
    print("FIND   | mycheatsheet.py find <id> OR <alias> ")


def options(argv):
    alias = ''
    description = ''
    command = ''

    try:
        opts, args = getopt.getopt(argv, "a:d:c:")
    except getopt.GetoptError:
        print('test.py -i <alias> -o <description>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -a <alias> -d <description> -c <command>')
            sys.exit()
        elif opt in ("-a", "--alias"):
            alias = arg
        elif opt in ("-d", "--description"):
            description = arg
        elif opt in ("-c", "--command"):
            command = arg
    if(not alias or not description or not command):
        help()
    else:
        validated = [alias, description, command]
        return validated


def test_open_file():
    try:
        with open('.mycheatsheet.yml') as f:
            return 0
    except IOError:
        return 1


def create_file():
    try:
        f = open(".mycheatsheet.yml", "w+")
    except:
        return 1


def show_all_commands():
    with open(r'.mycheatsheet.yml') as file:
        yml = yaml.load(file, Loader=yaml.FullLoader)
        try:
            for x in yml:
                print(x)
                for y in yml[x]:
                    print(y, ':', yml[x][y])
        except:
            print("vazio")


def show_by_category(category):
    with open(r'.mycheatsheet.yml') as file:
        yml = yaml.load(file, Loader=yaml.FullLoader)
        try:
            for x in yml:
                if(yml.get(x).get("category") == "linux"):
                    print(x)
                    for y in yml[x]:
                        print(y, ':', yml[x][y])
        except:
            print("vazio")


def add_command(json_insertion):
    json_obj = json.dumps(json_insertion)
    ff = open(".mycheatsheet.yml", "a")
    yaml.dump(json_insertion, ff, default_flow_style=False)


def rm_command(id_or_alias):
    with open(r'.mycheatsheet.yml') as file:
        yml = yaml.load(file, Loader=yaml.FullLoader)

        try:
            yml.pop(id_or_alias)
        except:
            print("not found")

        json_obj = json.dumps(yml)
        ff = open(".mycheatsheet.yml", "w")
        yaml.dump(yml, ff, default_flow_style=False)


def find_command(alias):
    with open(r'.mycheatsheet.yml') as file:
        yml = yaml.load(file, Loader=yaml.FullLoader)

        try:
            if(yml.get(alias) is not None):
                print(yml.get(alias))
            else:
                print("not found")
        except:
            print("not found")


def md5_create(alias):
    m = hashlib.md5()
    m.update(alias.encode())
    # print(m.hexdigest())
    return m.hexdigest()


def call_manager(allargs):
    print(allargs)
    print(len(allargs))


if __name__ == "__main__":

    ready_file = True if test_open_file() == 0 else create_file()

    if(ready_file == True):
        pass
    else:
        sys.exit(2)



    call_manager(sys.argv)

    sys.exit(2)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "list"):
            show_all_commands()
    elif(len(sys.argv) == 3):
        if(sys.argv[1] == "find"):
            id_or_alias = sys.argv[2]
            find_command(id_or_alias)
        if(sys.argv[1] == "rm"):
            id_or_alias = sys.argv[2]
            rm_command(id_or_alias)
    elif(len(sys.argv) == 7):
        print(len(sys.argv))
        insertion = options(sys.argv[1:])
        id = md5_create(insertion[0])
        json_insertion = {insertion[0]: {'id': id, 'update': [
            insertion[1], insertion[2]]}}
        print(json_insertion)
        add_command(json_insertion)
    else:
        help()
        sys.exit(2)
        


