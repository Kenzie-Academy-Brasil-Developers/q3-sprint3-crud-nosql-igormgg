# CRUD REST NoSQL


| Critérios | Pts. |
|---|---|
| [GET] **/posts**. Retorna todos os posts do banco de dados. | 1 |
| [GET] **/posts/\<id>**. Retorna 404 para um id não existente no banco. | 1 |
| [POST] **/posts**. Retorna o status code mais indicado caso esteja faltando alguma chave no JSON enviado. | 2 |
| [POST] **/posts**. Ao receber uma requisição correta, salva os dados no banco de dados e retorna o status 201. | 2 |
| [PATCH] **/posts/\<id>**. Retorna o status code mais indicado caso o JSON enviado não seja válido. | 1 |
| [PATCH] **/posts/\<id>**. Tentativa de editar post inexistente retorna **404**. | 1 |
| [PATCH] **/posts/\<id>**. Retorna o objeto atualizado e status **200** em caso de sucesso na atualização. | 1 |
| [DELETE] **/posts/\<id>**. Retorna o objeto deletado e o status code correto. Deletando o post indicado do banco de dados. | 1 |
| [DELETE] **/posts/\<id>**. Tentativa de deletar post inexistente retorna **404**. | 1 |
| **id auto incrementável**. A cada novo post criado o id é incrementado automaticamente. Mesmo reiniciando a aplicação. | 2 |
| **Arquitetura** e **Design Pattern**. Organização do projeto de acordo com o padrão **MVC** e uso do Design Pattern **Factory**. | 2 |
| **POO**. Utilização dos tipos corretos de atributos e métodos nas classes. (Instância, Classe, estáticos). E uso dos métodos especiais corretamente. | 2 |
| **MongoDB**. Conexão com o banco seguindo boas práticas e uso correto das funções disponibilizadas pelo **Pymongo**. | 2 |
| Arquivos **requirements.txt**, **.env**, **.env.example** e **.gitignore** (**venv** e **.env** adicionados) | 1 |