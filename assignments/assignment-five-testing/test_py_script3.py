import py_script3

def test_idgaf():
	result = py_script3.idgaf()
	assert result != 'FUCK'
	assert 'fail' in result
