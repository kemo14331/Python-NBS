import python_nbs.nbs as nbs
import unittest

ns = nbs.NBS('tests/Test.nbs')

print(ns.song_name)
print(str(ns.note_blocks))

unittest.main()