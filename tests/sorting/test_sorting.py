from src.sorting import sort_by

jobs_list_mock = [
    {"max_salary": 28030, "min_salary": 2500, "date_posted": "2022-10-01"},
    {"max_salary": -1000, "min_salary": 1200, "date_posted": "2022-10-05"},
    {"max_salary": 39052, "min_salary": 2000, "date_posted": "2022-10-22"},
    {"max_salary": 10, "min_salary": 0, "date_posted": "2022-10-11"},
    {"max_salary": 20156, "min_salary": 1100, "date_posted": "2022-10-23"},
    {"max_salary": 10999, "min_salary": 1200, "date_posted": "2022-10-29"},
    {"max_salary": 12999, "min_salary": 1150, "date_posted": "2022-10-20"},
]

criteria_keys = ["min_salary", "max_salary", "date_posted"]


def test_sort_by_criteria():
    for criteria in criteria_keys:
        sort_by(jobs_list_mock, criteria)
        if criteria == "min_salary":
            assert jobs_list_mock[0][criteria] <= jobs_list_mock[1][criteria]
        else:
            assert jobs_list_mock[0][criteria] >= jobs_list_mock[1][criteria]
