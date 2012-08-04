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

import os

from testtools import TestCase
from testtools.matchers import (
    DirContains,
    DirExists,
    FileContains,
    Mismatch,
    Not,
    )

from treeshape import FileTree


class HasNoAttribute(object):
    """For asserting that an object does not have a particular attribute."""

    def __init__(self, attr_name):
        self._attr_name = attr_name

    def __str__(self):
        return 'HasNoAttribute(%s)' % (self._attr_name,)

    def match(self, obj):
        sentinel = object()
        value = getattr(obj, self._attr_name, sentinel)
        if value is not sentinel:
            return Mismatch(
                "%s is an attribute of %r: %r" % (
                    self._attr_name, obj, value))


class TestFileTree(TestCase):

    def test_no_path_at_start(self):
        # FileTree fixture doesn't create a path at the beginning.
        fixture = FileTree([])
        self.assertThat(fixture, HasNoAttribute('path'))

    def test_creates_directory(self):
        # It creates a temporary directory once set up.  That directory is
        # removed at cleanup.
        fixture = FileTree([])
        fixture.setUp()
        try:
            self.assertThat(fixture.path, DirExists())
        finally:
            fixture.cleanUp()
            self.assertThat(fixture.path, Not(DirExists()))

    def test_out_of_order(self):
        # If a file or a subdirectory is listed before its parent directory,
        # that doesn't matter.  We'll create the directory first.
        fixture = FileTree(['a/b/', 'a/'])
        with fixture:
            path = fixture.path
            self.assertThat(path, DirContains(['a']))
            self.assertThat(os.path.join(path, 'a'), DirContains(['b']))
            self.assertThat(os.path.join(path, 'a', 'b'), DirExists())

    def test_not_even_creating_parents(self):
        fixture = FileTree(['a/b/foo.txt', 'c/d/e/'])
        with fixture:
            path = fixture.path
            self.assertThat(
                os.path.join(path, 'a', 'b', 'foo.txt'),
                FileContains("The file 'a/b/foo.txt'."))
            self.assertThat(os.path.join(path, 'c', 'd', 'e'), DirExists())
