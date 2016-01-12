===========
 treeshape
===========

treeshape allows you to quickly make file and directory structures on disk.

For example::

    from treeshape import make_tree

    make_tree('.', [
        'logs/',
        ('README', "A simple directory layout\n"),
        ('data/input', "All of our input data\n"),
    ])

Will create a directory structure that looks like this::

    $ find .
    .
    ./logs
    ./data
    ./data/input
    ./README
    $ cat README
    A simple directory layout
    $ cat data/input
    All of our input data

This is particularly useful for tests that touch the disk. For example::

    from testtools import TestCase
    from testtools.matchers import DirExists, FileContains, FileExists
    from treeshape import FileTree

    class MyTests(TestCase):

        def test_files(self):
            tree = self.useFixture(FileTree([
                'logs/',
                ('README', "A simple directory layout\n"),
                ('data/input', "All of our input data\n"),
            ])
            self.assertThat(
                os.path.join(tree.path, 'data/input'),
                FileContains("All of our input data\n"))
            self.assertThat(os.path.join(tree.path, 'logs'), DirExists())
            self.assertThat(os.path.join(tree.path, 'README'), FileExists())

The ``FileTree`` fixture can also be used as a context manager::

    from treeshape import FileTree

    with FileTree([('directory/newfile', 'data')]) as tree:
        newfile_path = os.path.join(tree.path, 'directory/newfile')
        with open(newfile_path) as newfile:
            assert newfile.read() == 'data'
