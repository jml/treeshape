#  treeshape: quickly make file and directory structures.
#
# Copyright (c) 2012, Jonathan Lange <jml@mumak.net>
#
# Licensed under either the Apache License, Version 2.0 or the BSD 3-clause
# license at the users choice. A copy of both licenses are available in the
# project source as Apache-2.0 and BSD. You may not use this file except in
# compliance with one of these two licences.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under these licenses is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# license you chose for the specific language governing permissions and
# limitations under that license.

from fixtures import (
    Fixture,
    TempDir,
    )

from ._treeshape import make_tree


class FileTree(Fixture):
    """A structure of files and directories on disk."""

    def __init__(self, shape):
        """Create a ``FileTree``.

        :param shape: A list of descriptions of files and directories to make.
            Generally directories are described as ``"directory/"`` and
            files are described as ``("filename", contents)``.  Filenames can
            also be specified without contents, in which case we'll make
            something up.

            Directories can also be specified as ``(directory, None)`` or
            ``(directory,)``.
        """
        super(FileTree, self).__init__()
        self.shape = shape

    def setUp(self):
        super(FileTree, self).setUp()
        tempdir = self.useFixture(TempDir())
        self.path = tempdir.path
        make_tree(self.path, self.shape)
