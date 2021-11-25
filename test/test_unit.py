from src.unit import Unit

def test_unit_size():
    unit = Unit(5)
    assert(unit.size() == 0)