
# DIO | NTT DATA | Resumos Git e Github

Repositório para armazenar resumos sobre Git e Github do curso de Versionamento de Código com Git e Github da DIO/NTT DATA.

## 📒 Documentação
- [Documentação Git](https://git-scm.com/doc)
- [Documentação Github](https://docs.github.com/)

## 💻 Comandos

| criando e Clonando Repos |
|----------|
**cat** - Exibe o conteúdo do arquivo
**git clone "URL"** - Copia de um repositório remoto. Ex: git clone https://github.com/hello-word.git
**git clone "URL" "novo nome do repositório"** - Copia um repositório remoto e salva com outro nome (novo nome do repositório). Ex: git clone https://github.com/hello-word.git repo-clonado


| Salvando alterações no Repo Local |
|----------|
**git init** - inicializa o Repositório
**git status** - Mostra o status da arvore de trabalho e da área de preparação (staging area)
**touch** - Cria um arquivo vazio. Ex: touch Novo Repo
**git add "nome do arquivo"** - Adiciona arquivo para a stagging área. Ex: git add README.md
**git add .** - Adiciona todos arquivos "desconhecidos" para área de staging.
**git commit -m"adiciona configuração de classes"** - Efetiva a mudança nos arquivos da "staging area" no repositório, e adiciona uma informação/nota com o que está entre os parênteses "".
**git log** - Mostra o histórico dos commits


| Desfazendo alterações no Repo Local |
|----------|
**git commit** --ammend -m"alterando o nome do ultimo commit" - Altera a mensagem do ultimo commit
**git reset --soft "hash do commit do arquivo a ser desfeita a alteração"** - Desfaz as alterações do último commit do arquivo informado pela hash, devolvendo o arquivo para a staging area. Ex: git reset --soft 54d987ert94984ds59dsv98195125df
**git reset --mixed "hash do arquivo"** - Faz com que os arquivos da ultima modificação, voltem para o estado anterior ao staging.
**git reset --hard "hash do arquivo"** - Apaga todos os commits e arquivos posteriores a versão do hash escolhido, não devolvendo para staging ou anterior a isso. 
**git reflog** - Mostra todas as alterações feitas nos commits
**git reset "nome do arquivo"** - Remove os arquivos da staging área
*git restore --staged "nome do arquivo"** - Remove os arquivos da staging área


| Enviando e baixando alterações no Repo Remoto |
|----------|
**git remote add origin https://github.com/Hello-World.git** - add o repositório remoto.
**git push -u origin main** - define onde vai fazer o upload dentro do repositório, no caso, na branche main.

