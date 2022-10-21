from src.jobs import read


def get_unique_job_types(path: str):
    get_read = read(path)
    unique_job_type = set([job["job_type"] for job in get_read])
    return unique_job_type


def filter_by_job_type(jobs: list, job_type: str):
    if job_type == "":
        return []

    filtered = [job for job in jobs if job["job_type"] == job_type]

    return filtered


def get_unique_industries(path: str):
    get_read = read(path)
    unique_job_industries = set(
        [job["industry"] for job in get_read if job["industry"] != ""]
    )
    return unique_job_industries


def filter_by_industry(jobs: list, industry: str):
    if industry == "":
        return []

    filtered = [job for job in jobs if job["industry"] == industry]

    return filtered


def get_max_salary(path: str):
    get_read = read(path)
    max_salary = [job["max_salary"] for job in get_read if job["max_salary"]]
    conversion = [int(salary) for salary in max_salary if salary != "invalid"]

    return max(conversion)


def get_min_salary(path: str):
    get_read = read(path)
    min_salary = [job["min_salary"] for job in get_read if job["min_salary"]]
    conversion = [int(salary) for salary in min_salary if salary != "invalid"]

    return min(conversion)


def matches_salary_range(job: dict, salary: int):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("doesn't exists")
    elif type(job["min_salary"] or job["max_salary"]) != int:
        raise ValueError("aren't valid integers")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("minimum salary is greather than max salary")
    elif type(salary) != int:
        raise ValueError("isn't a valid integer")

    return salary >= job["min_salary"] and salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
