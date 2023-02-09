from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from unittest.mock import patch
from pytest import raises


mock1 = [
    {
        "title": "Notícia bacana1",
        "reading_time": 4,
    },
    {
        "title": "Notícia bacana2",
        "reading_time": 3,
    },
    {
        "title": "Notícia bacana3",
        "reading_time": 10,
    },
    {
        "title": "Notícia bacana4",
        "reading_time": 15,
    },
    {
        "title": "Notícia bacana5",
        "reading_time": 12,
    },
]


def test_reading_plan_group_news():
    with patch(
        "tech_news.analyzer.reading_plan.find_news", return_value=mock1
    ):
        data = ReadingPlanService.group_news_for_available_time(10)
        assert data["readable"] == [
            {
                "unfilled_time": 3,
                "chosen_news": [
                    (
                        "Notícia bacana1",
                        4,
                    ),
                    (
                        "Notícia bacana2",
                        3,
                    ),
                ],
            },
            {
                "unfilled_time": 0,
                "chosen_news": [
                    (
                        "Notícia bacana3",
                        10,
                    )
                ],
            },
        ]
        assert data["unreadable"] == [
            ("Notícia bacana4", 15),
            ("Notícia bacana5", 12),
        ]
    with raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        data = ReadingPlanService.group_news_for_available_time(0)
