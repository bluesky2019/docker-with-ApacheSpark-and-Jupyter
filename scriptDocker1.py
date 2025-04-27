import subprocess

def run_spark_with_jupyter():
    subprocess.run(["docker", "rm", "-f", "meu_spark"], stderr=subprocess.DEVNULL)
    
    try:
        subprocess.run([
            "docker", "run", "-d",
            "-p", "8888:8888",
            "-p", "4040:4040",
            "-e", "JUPYTER_TOKEN=senha123",  # ← Define senha fácil
            "--name", "meu_spark",
            "jupyter/all-spark-notebook"
    ], check=True)
        
        print("Container iniciado com Jupyter Notebook")
        print("Acesse http://localhost:8888")
        
    except subprocess.CalledProcessError as e:
        print(f"Erro: {e.stderr}")

run_spark_with_jupyter()