import requests

def get_github_jobs(location, description, page=1, per_page=50):
    base_url = 'https://jobs.github.com/positions.json'
    params = {'location': location, 'description': description, 'page': page, 'per_page': per_page}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def extract_skills(jobs):
    skills = {}

    for job in jobs:
        job_skills = job.get('description', '').lower().split()
        for skill in job_skills:
            if len(skill) > 2:
                skills[skill] = skills.get(skill, 0) + 1

    return skills

def main():
    location = input("Enter the location: ")
    description = input("Enter the job description: ")

    jobs = get_github_jobs(location, description)

    if jobs:
        skills = extract_skills(jobs)
        
        # Sort skills by frequency
        sorted_skills = sorted(skills.items(), key=lambda x: x[1], reverse=True)

        total_jobs = len(jobs)
        top_skills = sorted_skills[:20]

        for skill, count in top_skills:
            percentage = (count / total_jobs) * 100
            print(f"{skill}: {count} occurrences ({percentage:.2f}% of jobs)")

if __name__ == "__main__":
    main()
