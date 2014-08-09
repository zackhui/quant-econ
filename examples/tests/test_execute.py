"""
Test all py files in directory execute without any runtime errors
"""

import subprocess as sb
import glob
from nose import with_setup


def test_execute():
	files = glob.glob("../*.py")
	files.sort()
	for fl in files:
	    exitcond = sb.call(["ipython", "--matplotlib=Qt4", fl])
	    if exitcond != 0:
	    	assert False, "File: %s ran with some errors\n" % (fl)