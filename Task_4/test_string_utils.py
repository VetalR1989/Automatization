import pytest
from string_utils import StringUtils

stringutils = StringUtils()

@pytest.mark.positive_test
@pytest.mark.parametrize('string, result', [("smile", "Smile"), ("улыбка", "Улыбка"), ("ta xi", "Ta xi")])
def test_capitilize_positive(string: str, result: str):
    stringutils = StringUtils()
    res = stringutils.capitilize(string)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('string, result', [("", ""), (" ", " "), ("88", "88"), ("0", "0"), ("%-+", "%-+")])
def test_capitilize_negative(string: str, result: str):
    stringutils = StringUtils()
    res = stringutils.capitilize(string)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize('string, result', [(" smile", "smile"), ("      улыбка", "улыбка"), (" ta xi", "ta xi"), (" 88", "88"), (" 0", "0")])
def test_trim_positive(string: str, result: str):
    stringutils = StringUtils()
    res = stringutils.trim(string)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('string, result', [("", ""), (" ", ""), (" #$%^&", "#$%^&")])
def test_trim_negative(string: str, result: str):
    stringutils = StringUtils()
    res = stringutils.trim(string)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize('string, result', [("s,m,i,l,e", ["s","m","i","l","e"]), ("у,л,ы,б,к,а", ["у","л","ы","б","к","а"]), ("8,8", ["8","8"]), ("0", ["0"])])
def test_to_list_positive(string: str, result: list):
    stringutils = StringUtils()
    res = stringutils.to_list(string)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('string, result', [("", []), (" ", []), ("#,$,%,^,&", ["#","$","%","^","&"])])
def test_to_list_negative(string: str, result: list):
    stringutils = StringUtils()
    res = stringutils.to_list(string)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize('string, symbol, result', [("Smile", "m", True), ("улыбка", "и", False), ("ta xi", "x", True), ("88", "4", False), ("0", "0", True)])
def test_contains_positive(string: str, symbol: str, result: bool):
    stringutils = StringUtils()
    res = stringutils.contains(string, symbol)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('string, symbol, result', [("", "", True), (" ", "", True), ("#$%^&", "%", True)])
def test_contains_negative(string: str, symbol: str, result: bool):
    stringutils = StringUtils()
    res = stringutils.contains(string, symbol)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize('string, symbol, result', [("Smile", "m", "Sile"), ("Smile", "Smi", "le"), ("улыбка", "лы", "убка"), ("ta xi", "x", "ta i"), ("88", "8", ""), ("0", "0", "")])
def test_delete_symbol_positive(string: str, symbol: str, result: str):
    stringutils = StringUtils()
    res = stringutils.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('string, symbol, result', [("", "", ""), (" ", "", " "), ("#$%^&*", "&", "#$%^*")])
def test_delete_symbol_negative(string: str, symbol: str, result: str):
    stringutils = StringUtils()
    res = stringutils.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize('string, symbol, result', [("Smile", "S", True), ("улыбка", "и", False), ("ta xi", "t", True), ("88", "4", False), ("0", "0", True)])
def test_starts_with_positive(string: str, symbol: str, result: bool):
    stringutils = StringUtils()
    res = stringutils.starts_with(string, symbol)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('string, symbol, result', [("", "", True), (" ", "", True)])
def test_starts_with_negative(string: str, symbol: str, result: bool):
    stringutils = StringUtils()
    res = stringutils.starts_with(string, symbol)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize('string, symbol, result', [("Smile", "e", True), ("улыбка", "и", False), ("ta xi", "i", True), ("88", "4", False), ("0", "0", True)])
def test_end_with_positive(string: str, symbol: str, result: bool):
    stringutils = StringUtils()
    res = stringutils.end_with(string, symbol)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('string, symbol, result', [("", "", True), (" ", "", True)])
def test_end_with_negative(string: str, symbol: str, result: bool):
    stringutils = StringUtils()
    res = stringutils.end_with(string, symbol)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize('string, result', [("Smile", False), ("улыбка", False), ("ta xi", False), ("", True), (" ", True), ("88", False), ("0", False)])
def test_is_empty_positive(string: str, result: bool):
    stringutils = StringUtils()
    res = stringutils.is_empty(string)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('string, result', [("       ", True), ("-=^&", False)])
def test_is_empty_negative(string: str, result: bool):
    stringutils = StringUtils()
    res = stringutils.is_empty(string)
    assert res == result


@pytest.mark.positive_test
@pytest.mark.parametrize('list, result', [(["s","m","i","l","e"], "s, m, i, l, e"), (["у","л","ы","б","к","а"], "у, л, ы, б, к, а"), (["8","8"], "8, 8"), (["0"], "0")])
def test_list_to_string_positive(list, result: str):
    stringutils = StringUtils()
    res = stringutils.list_to_string(list)
    assert res == result


@pytest.mark.negative_test
@pytest.mark.parametrize('list, result', [([], ""), ([      ], ""), (["-","+"], "-, +")])
def test_list_to_string_negative(list, result: str):
    stringutils = StringUtils()
    res = stringutils.list_to_string(list)
    assert res == result