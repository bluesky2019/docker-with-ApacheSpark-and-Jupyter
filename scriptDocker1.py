import subprocess

def run_spark_with_jupyter():
    # Verifica se o container existe
    check_container = subprocess.run(
        ["docker", "ps", "-a", "--filter", "name=meu_spark", "--format", "{{.Names}}"],
        capture_output=True,
        text=True
    )
    
    container_exists = check_container.stdout.strip() == "meu_spark"
    
    if container_exists:
        # Pergunta ao usuário se deseja remover o container existente
        resposta = input("O container 'meu_spark' já existe. Deseja removê-lo? (yes/no): ").strip().lower()
        
        if resposta == "yes":
            print("Removendo container existente...")
            subprocess.run(["docker", "rm", "-f", "meu_spark"], check=True)
        elif resposta == "no":
            print("Utilizando container existente.")
            # Verifica se o container está parado e inicia se necessário
            check_status = subprocess.run(
                ["docker", "ps", "-a", "--filter", "name=meu_spark", "--format", "{{.Status}}"],
                capture_output=True,
                text=True
            )
            if "Exited" in check_status.stdout:
                print("Iniciando container existente...")
                subprocess.run(["docker", "start", "meu_spark"], check=True)
            return
        else:
            print("Resposta inválida. Digite 'yes' ou 'no'.")
            return

    try:
        print("Criando novo container...")
        subprocess.run([
            "docker", "run", "-d",
            "-p", "8888:8888",
            "-p", "4040:4040",
            "-e", "JUPYTER_TOKEN=senha123",
            "--name", "meu_spark",
            "jupyter/all-spark-notebook"
        ], check=True)
        
        print("\nContainer iniciado com Jupyter Notebook")
        print("Acesse: http://localhost:8888")
        print("Senha: senha123")
        
    except subprocess.CalledProcessError as e:
        print(f"Erro: {e.stderr}")

run_spark_with_jupyter()