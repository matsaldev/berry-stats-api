from app.entity.berry_growth import BerryGrowth


def test_berry_growth_entity():
    berry = BerryGrowth(name="Test", growth_time=5)
    assert berry.name == "Test"
    assert berry.growth_time == 5
