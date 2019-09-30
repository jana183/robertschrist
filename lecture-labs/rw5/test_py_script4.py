import py_script4

def test_grievances():
        result = py_script4.grievances('Noone', 'will', 'notice')
        assert result != 'FUCK'
	assert "notice" in result
