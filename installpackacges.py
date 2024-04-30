import subprocess
import datetime

def install_packages_from_requirements(requirements_file, log_file):
    with open(requirements_file, 'r') as file:
        packages = file.readlines()
        with open(log_file, 'a') as log:
            log.write(f"Installation started at {datetime.datetime.now()}\n")
            for package in packages:
                package = package.strip()
                log.write(f"Attempting to install {package}...\n")
                try:
                    result = subprocess.run(['pip', 'install', package], capture_output=True, text=True, check=True)
                    log.write(result.stdout + "\n")
                    log.write(f"{package} installed successfully.\n")
                except subprocess.CalledProcessError as e:
                    log.write(f"Error installing {package}: {e}\n")
                    log.write(f"Continuing with the next package...\n")
            log.write(f"Installation completed at {datetime.datetime.now()}\n\n")

if __name__ == "__main__":
    requirements_file = "requirements.txt"
    log_file = "installation_log.txt"
    install_packages_from_requirements(requirements_file, log_file)
