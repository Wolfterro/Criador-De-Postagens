# Criador de Postagens
## Um simples criador de postagens para meu site pessoal no GitHub!

### Descrição:

###### Este é um simples programa escrito em Python e utiliza PyQt4 para a criação rápida de posts em meu site pessoal no GitHub.

###### Decidi criar este programa para facilitar a minha vida na hora de postar algo novo em meu site pessoal, já que antes eu tinha que editar manualmente o arquivo .html do novo post.

###### O programa ainda é bem simples e utiliza algumas tags para a criação de um post simples. Pretendo adicionar novas funcionalidades no futuro, para facilitar ainda mais a criação de novos posts e adicionar novas tags e funcionalidades.

###### É OBRIGATÓRIO que o arquivo 'model.html' esteja presente na pasta principal junto ao programa, este arquivo é usado como base para a criação de um novo post.

###### O arquivo 'model.html' NÃO PODE SER ALTERADO DE MANEIRA ALGUMA! O programa verifica o MD5 do arquivo modelo e faz uma comparação com a hash que ele possui do arquivo original. Se houver mudanças o programa NÃO IRÁ INICIAR, dando um aviso de que o arquivo modelo foi modificado ou corrompido!

###### Caso alguém achar útil o meu programa e quiser utilizar em seu próprio website, terá de usar um outro arquivo modelo e alterar a hash definida no programa para que ele possa aceitar o novo modelo!

### Requisitos:

#### Compilando:
- Python 2.7
- PyQt4 para Python 2.7
- PyInstaller
- Microsoft Visual C++ 2010 Redistributable (Windows apenas)

##### Para compilar o programa no Windows, basta executar o arquivo 'build.bat'.
##### Para compilar o programa no Linux, basta executar o arquivo 'build.sh'.
##### **OBS**: É necessário que o PyInstaller seja reconhecido como comando interno no prompt de comando (Windows) ou no shell que estiver utilizando (Linux).

### Download:

#### ***Binário:*** https://github.com/Wolfterro/Criador-De-Postagens/releases/tag/v1.0
#### ***Código-fonte:*** https://github.com/Wolfterro/Criador-De-Postagens/archive/master.zip
