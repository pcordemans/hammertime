from src.unit import Unit
from src.unit import Model

def test_unit_size():
    unit = Unit(5)
    assert(unit.size() == 0)

def test_add_model_to_unit():
    unit = Unit(5)
    unit.add(Model(4,20,20), 1)
    assert(unit.size() == 1)
    unit.add(Model(4,20,20), 4)
    assert(unit.size() == 5)

def test_number_of_ranks():
    unit = Unit(5)
    assert(unit.ranks() == 0)
    unit.add(Model(4,20,20), 4)
    assert(unit.ranks() == 0)
    unit.add(Model(4,20,20), 4)
    assert(unit.ranks() == 1)

def test_number_of_models_in_last_rank():
    unit = Unit(5)
    assert(unit.lastRank() == 0)
    unit.add(Model(4,20,20), 2)
    assert(unit.lastRank() == 2)
    unit.add(Model(4,20,20), 3)
    assert(unit.lastRank() == 0)
    unit.add(Model(4,20,20), 3)
    assert(unit.lastRank() == 3)