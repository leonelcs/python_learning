from .context import phonebook as pb
import pytest

@pytest.fixture
def phonebook():
    return pb.Phonebook()

def test_phone_add(phonebook):
    phonebook.add("Leonel","0687961232")
    assert "0687961232" == phonebook.lookup("Leonel")

def test_phone_lookup_wrong(phonebook):
    phonebook.add("Leonel","0687961232")
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")