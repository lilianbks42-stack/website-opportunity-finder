from agent.scorer import score_opportunity, score_label


def test_hot_score():
    score = score_opportunity(
        explicit_website_request=True,
        landing_page_request=True,
        no_website_found=True,
    )

    assert score == 100
    assert score_label(score) == "HOT"
