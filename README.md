# Script para Remover Zone.Identifier

Este script foi desenvolvido para facilitar a remoção automática de arquivos com a extensão `.Zone.Identifier` que são criados ao copiar arquivos do Windows para a WSL (Windows Subsystem for Linux). Esses arquivos podem causar problemas ao serem submetidos ao GitHub, especialmente em branches.

## Problema

Ao transferir arquivos baixados do Windows para a WSL, um arquivo com a extensão `:Zone.Identifier` é gerado. Esse arquivo pode interferir no funcionamento do seu repositório Git, resultando em conflitos e problemas de branch.

## Solução

O script abaixo percorre todas as pastas do projeto e remove automaticamente os arquivos que seguem o padrão `.*:Zone.Identifier` e `*:Zone.Identifier`.

### Código do Script

Você pode encontrar o código do script [neste link](https://github.com/dossantoscarlos/zone_identifier/blob/main/remove_zoneIdentifier.sh).

## Como Usar

1. Salve o script em um arquivo, por exemplo, `remove_zone.sh`.
2. Dê permissão de execução ao script:
   ```bash
   chmod +x remove_zone.sh
   ```
3. Execute o script no diretório desejado:
   ```bash
   ./remove_zone.sh
   ```

## Observações

- Certifique-se de que você tem as permissões necessárias para remover arquivos nos diretórios que o script irá percorrer.
- Use este script com cautela, pois ele removerá arquivos permanentemente.
