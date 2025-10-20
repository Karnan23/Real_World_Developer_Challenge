import os,json,requests,logging

try:
    with open("config.json","r") as f:
        config = json.load(f)
        github_users=config["github_users"]
        output_directory=config["output_directory"]
        log_file=config["log_file"]
        github_details=config["req_github_details"]
except Exception as e:
    logging.error(f"Error loading configuration: {e}")
    exit(1)


logging.basicConfig(filename="github_logs.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Script Started...")


def folder_check(output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        logging.info(f"Created directory: {output_directory}")
    else:
        logging.info(f"Directory already exists: {output_directory}")

def fetch_github_repos(github_users, output_directory):
    for user in github_users:
            try:
                response = requests.get(f"https://api.github.com/users/{user}/repos")
                if response.status_code != 200:
                    logging.error(f"Failed to fetch repositories for user {user}: {response.status_code}")
                    continue
                else:
                    logging.info(f"Successfully fetched repositories for user: {user}")
                repos = response.json()
                logging.info(f"Fetched {len(repos)} repositories for user: {user}")
                
                user_repo_details=[]
                for repo in repos:
                    repo_data={details:repo.get(details,'N/A') for details in github_details}
                    user_repo_details.append(repo_data)

                with open(os.path.join(output_directory, f"{user}_repos.json"), "w") as f:
                    json.dump(user_repo_details, f, indent=4)
                logging.info(f"Fetched and Saved {len(user_repo_details)} repos for user: {user}")

            except requests.exceptions.RequestException as e:
                logging.error(f"Error fetching repositories for user {user}: {e}")
            except Exception as e:
                logging.error(f"General error for user {user}: {e}")

    logging.info("Script Finished.")



if __name__ == "__main__":
    folder_check(output_directory)
    fetch_github_repos(github_users, output_directory)