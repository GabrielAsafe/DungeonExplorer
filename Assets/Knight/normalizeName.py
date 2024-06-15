import os

def rename_files(directory):
    # Lista todos os arquivos no diretório fornecido
    files = os.listdir(directory)
    
    for file_name in files:
        # Verifica se o arquivo é uma imagem PNG e contém '-a' no nome
        if file_name.endswith(".png") and "-a" in file_name:
            # Remove o sufixo '-a' do nome do arquivo
            new_name = file_name.replace("-a", "")
            # Obtém o caminho completo para os arquivos original e novo
            old_file = os.path.join(directory, file_name)
            new_file = os.path.join(directory, new_name)
            # Renomeia o arquivo
            os.rename(old_file, new_file)
            print(f'Renamed: {file_name} to {new_name}')

def main():
    # Obtém o diretório de trabalho atual
    current_directory = os.getcwd()
    # Chama a função para renomear arquivos
    rename_files(current_directory)

if __name__ == "__main__":
    main()
