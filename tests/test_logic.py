from mylib.logic import wiki, summary

def test_wiki():
    assert "List of Germanic deities" in wiki()
 
def test_summary():
    assert len(summary('Nelson Muntz'))> 10
    