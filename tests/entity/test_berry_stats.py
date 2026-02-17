from app.entity.berry_stats import BerryStats


def test_berry_stats_entity():
    stats = BerryStats(
        berries_names=["A", "B"],
        min_growth_time=1,
        median_growth_time=2,
        max_growth_time=3,
        variance_growth_time=1.5,
        mean_growth_time=2,
        frequency_growth_time={1: 1}
    )

    assert stats.mean_growth_time == 2
    assert stats.berries_names == ["A", "B"]
