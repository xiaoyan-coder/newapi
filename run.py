from unittestreport import TestRunner
import unittest
import os

from common.handle_path import CASE_DIR

suit = unittest.defaultTestLoader.discover(os.path.join(CASE_DIR))
runner = TestRunner(suit)
runner.run()

