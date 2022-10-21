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


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


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
