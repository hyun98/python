if __name__ == "__main__":
    from indeed import get_jobs as get_indeed_jobs
    from stackoverflow import get_jobs as get_stackof_jobs
    from save import save_to_file

    indeed_jobs = get_indeed_jobs()
    stackoverflow_jobs = get_stackof_jobs()

    all_jobs = indeed_jobs + stackoverflow_jobs

    save_to_file(all_jobs)
