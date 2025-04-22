#!/bin/bash

# Função para remover arquivos com o padrão .*:Zone.* em todos os diretório
remove_zone_files() {
 local dir=$1
 echo "Entrando no diretório: $dir"
 ls $dir

 # Verifica se o diretório existe e se está acessível
 if [ -d "$dir" ]; then
 # Executa o comando de remoção no diretório atual 
 echo "Removendo arquivos e diretórios com o padrão .*:Zone.Identifier e *:Zone.Identifier em $dir"

 rm -R "$dir"/*:Zone.Identifier 2>/dev/null hashtag#remove arquivos com o zone sem ser arquivos ocultos

 rm -R "$dir"/.*:Zone.Identifier 2>/dev/null # remove os arquivos ocultos 
 fi
}

# Função recursiva para explorar todos os diretórios
explore_directories() {
 local start_dir=$1

 # Encontrar todos os diretórios a partir de start_dir
 find "$start_dir" -type d | while read dir; do
 # Para cada diretório encontrado, chama a função de remoção
 remove_zone_files "$dir"
 ls $dir
 done
}

# Iniciar a exploração do diretório atual
explore_directories "$(pwd)"