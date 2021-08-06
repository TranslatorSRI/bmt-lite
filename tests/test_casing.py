"""Test case conversions."""
import pytest

from bmt.util import pascal_to_snake, snake_to_pascal, guess_casing

cases = [
    ("PhenotypicFeature", "phenotypic_feature"),
    ("RNAProduct", "RNA_product"),
    ("ACamel", "a_camel"),
    ("FeedACamel", "feed_a_camel"),
    ("ProfessorX", "professor_x"),
    ("TheFBI", "the_FBI"),
    ("ABCDefGHI", "ABC_def_GHI"),
    ("TheXYZCompany", "the_XYZ_company"),
]


@pytest.mark.parametrize("original,target", cases)
def test_pascal_to_snake(original, target):
    """Test pascal_to_snake()."""
    assert pascal_to_snake(original) == target


@pytest.mark.parametrize("target,original", cases)
def test_snake_to_pascal(original, target):
    """Test snake_to_pascal()."""
    assert snake_to_pascal(original) == target


cases = [
    ("Disease", "pascal"),
    ("PhenotypicFeature", "pascal"),
    ("treated_by", "snake"),
    ("call_the_FBI", "snake"),
    ("affects", "snake"),
    ("TheFBI", "pascal"),
    ("RNA", "pascal"),
]


@pytest.mark.parametrize("name,case", cases)
def test_guess_casing(name, case):
    """Test guess_casing()."""
    assert guess_casing(name) == case
