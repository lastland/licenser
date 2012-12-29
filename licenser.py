from os import path
import os
import shutil
import sys
import yaml

def _d_plus_f(d, f):
    return '/'.join([d, f])

def _d_plus_f_tuple(d, f):
    return (d, _d_plus_f(d, f))


if getattr(sys, 'frozen', None):
    basedir = sys._MEIPASS
else:
    basedir = path.dirname(path.realpath(__file__))
default_license_folder = _d_plus_f(basedir, '.licenses')
user_license_folder = path.expanduser("~/.licenses")
license_index_file = "index.yaml"

def _index_pos_tuple(d):
    return _d_plus_f_tuple(d, license_index_file)


find_license_order = [_index_pos_tuple(user_license_folder),
		      _index_pos_tuple(default_license_folder)]


def lookup_license_files_in_index(index, name):
    indices = yaml.load(open(index))
    if name not in indices:
	return None
    return indices[name]


def get_license_files_by_name(name):
    for d, f in find_license_order:
	if path.isdir(d) and path.isfile(f):
	    res = lookup_license_files_in_index(f, name)
	    if res != None:
		return (d, res)
    return None

def copy_license_files(license_folder, license_files, target):
    for (f, t) in license_files.iteritems():
	fp = _d_plus_f(license_folder, f)
	tp = _d_plus_f(target, t)
	shutil.copyfile(fp, tp)

def main(argv):
    license = argv[0]
    target = os.getcwd()
    if len(argv) > 1:
	target = argv[1]
    res = get_license_files_by_name(argv[0])
    if res == None:
	print "No such license!"
	raise
    copy_license_files(res[0], res[1], target)

if __name__ == "__main__":
    if len(sys.argv) > 1:
	main(sys.argv[1:])
    else:
	print "Usage: licenser <LICENSE_NAME> [TARGET]"
