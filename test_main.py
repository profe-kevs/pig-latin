from main import first_condition, translate


def test_first_condition():
    assert first_condition("ad") == True
    assert first_condition("xr") == True
    assert first_condition("yt") == True

def test_translate_with_first_condition():
    assert translate("adjective") == "adjectiveay"
    assert translate("xray") == "xrayay"
    assert translate("yttria") == "yttriaay"