"""Automate your Test Tutorial:

https://glenjarvis.com/interactions/automate-your-tests/
"""

def inc(initial_value):
	"""Return arithmetic increase of 1 to initial_value"""
	print "In inc() subroutine now"
	return initial_value + 1
	
def test_answer():
	"""Sample test for our repository
	
	We expect this test to pass
	"""
	print "about to call assertion"
	assert inc(4) == 5
	print "exiting assertion"
"""Line at end of file
"""
