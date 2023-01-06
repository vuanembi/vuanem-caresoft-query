from netsuite.service import query_suiteql


def test_query_suiteql():
    data = query_suiteql("select id from classification")
    assert len(data) > 0
