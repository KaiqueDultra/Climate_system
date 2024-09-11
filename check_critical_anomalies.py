import subprocess

def check_critical_files():
    result = subprocess.run(['git', 'diff', '--name-only', 'HEAD~1', 'HEAD'], capture_output=True, text=True)
    changed_files = result.stdout.strip().split('\n')

    # Defina aqui os arquivos críticos para o seu projeto
    critical_files = {'requirements.txt', 'setup.py', 'config.yaml', '.env', 'main.py', 'app.py'}
    
    anomalies = [f"Critical file changed: {file}" for file in changed_files if file in critical_files]

    if anomalies:
        print("Anomalies found:")
        for anomaly in anomalies:
            print(anomaly)
        return 1
    else:
        print("No critical file anomalies detected.")
        return 0

if __name__ == "__main__":
    exit(check_critical_files())
