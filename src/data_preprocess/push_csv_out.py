import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing command: {command}")
        print(result.stderr)
    else:
        print(result.stdout)

commands = [         
    "dvc add ./csv_out",
    "git config --global user.email 'iheb.kesraoui@nanoz-group.com'",
    'git config --global user.name "IhebKesraoui"',
    "dvc add ./csv_out",
    "git add .",
    'git commit -m "push the csv-out"',
    "dvc push -r myremote2",
    "git push origin verified"
]

for command in commands:
    run_command(command)
