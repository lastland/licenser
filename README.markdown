## What is licenser?

Licenser is a program inspired by [licentious][].
But rather than building a web application associated with GitHub,
I prefer simple command line program that does simple, stupid operations.

At now, licenser is nothing more than copy some files into a directory.
However, I would like to add some other features, 
like adding copyright declarations, in the future.

[licentious]: https://github.com/pufuwozu/licentious

## Usage

``python /path/to/licenser/licenser.py <LICENSE_NAME> [TARGET_DIR]``

For example, if you want to add LGPL license into your current directory,
simply type the following command in your shell:

``python /path/to/licenser/licenser.py LGPL``

Then you would be able to see a file named `COPYING.LESSER`
in your current directory.

At now there're only GPL and LGPL licenses,
feel free to add licenses to your `~/.licenses` directory,
or checkin other public licenses to the program's `.licenses` directory.
For any of these two cases, 
you need to edit the file `index.yaml` manually.

## Copyright

Copyright (C) 2012, Yao Li (hnkfliyao@gmail.com).

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this program.  
If not, see <http://www.gnu.org/licenses/>.
