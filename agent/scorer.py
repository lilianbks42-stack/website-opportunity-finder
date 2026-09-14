def score_opportunity(
    explicit_website_request=False,
    landing_page_request=False,
    no_website_found=False,
    active_business_presence=False,
    public_business_contact=False,
    established_business=False,
):
    score = 0

    if explicit_website_request:
        score += 35
    if landing_page_request:
        score += 40
    if no_website_found:
        score += 25
    if active_business_presence:
        score += 15
    if public_business_contact:
        score += 10
    if established_business:
        score += 10

    return min(score, 100)


def score_label(score):
    if score >= 90:
        return "HOT"
    if score >= 70:
        return "WORTH REVIEW"
    if score >= 50:
        return "POTENTIAL"
    return "LOW PRIORITY"
