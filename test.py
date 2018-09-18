import pytest
from main import Soma_numeros

def test_Soma_numeros():
    assert Soma_numeros(5, 5) == 10
    assert Soma_numeros(6, 3) == 9