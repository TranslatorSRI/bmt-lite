"""Test bmt-lite."""
from bmt import Toolkit


def test_get_element():
    """Test get_element()."""
    BMT = Toolkit()

    el = BMT.get_element("causes")
    assert el.inverse == "caused by"

    el = BMT.get_element("disease")
    assert "MONDO" in el.id_prefixes

    el = BMT.get_element("biolink:Disease")
    assert "MONDO" in el.id_prefixes

    el = BMT.get_element("biolink:PhenotypicFeature")
    assert "HP" in el.id_prefixes

    el = BMT.get_element("biolink:affected_by")
    assert "affects" in el.inverse

    el = BMT.get_element("biolink:not_a_real_predicate")
    assert el is None


def test_get_descendants():
    """Test get_descendants()."""
    BMT = Toolkit()

    descendants = BMT.get_descendants("disease or phenotypic feature", reflexive=False)
    assert "disease" in descendants
    assert "disease or phenotypic feature" not in descendants

    descendants = BMT.get_descendants("disease", reflexive=True)
    assert "disease" in descendants

    descendants = BMT.get_descendants("disease or phenotypic feature", reflexive=True, formatted=True)
    assert "biolink:DiseaseOrPhenotypicFeature" in descendants

    descendants = BMT.get_descendants("affects", reflexive=True, formatted=True)
    assert "biolink:decreases_expression_of" in descendants

    descendants = BMT.get_descendants("biolink:not_a_real_predicate", reflexive=True)
    assert descendants == ["not a real predicate"]


def test_get_ancestors():
    """Test get_ancestors()."""
    BMT = Toolkit()

    ancestors = BMT.get_ancestors("disease", reflexive=False)
    assert "disease or phenotypic feature" in ancestors
    assert "disease" not in ancestors

    ancestors = BMT.get_ancestors("disease", reflexive=True)
    assert "disease" in ancestors


def test_get_all_slots():
    """Test get_all_slots()."""
    BMT = Toolkit()

    slots = BMT.get_all_slots()
    
    assert "contraindicated for" in slots


def test_dict_like():
    """Test dict-like features."""
    BMT = Toolkit()

    element = BMT.get_element("disease")
    element.foo = "bar"
    assert "foo" in element
    assert element["foo"] == "bar"
