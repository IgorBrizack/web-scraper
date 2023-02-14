# :snake: Web-scraper

Esse projeto foi criado com intenção de utilizar um crawler para raspar os dados de noticias do blog da TRYBE.

Desafios propostos:
   - Coletar os dados HTML da página web.
   - Armazenar os dados no banco de dados (MongoDB).
   - Criar menu interativo com terminal do Python.
   - Desenvolver os testes da Aplicação com o pytest.
   
 
 <details>
 <summary><strong> :desktop_computer: Ambiente virtual python:</strong></summary><br />
 
 * Use o comando: `git@github.com:IgorBrizack/web-scraper.git`
 
  1. **criar o ambiente virtual**

  ```bash
python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
python3 -m pip install -r dev-requirements.txt
  ```
 </details>
 
 <details>
 <summary><strong> :floppy_disk: Iniciando o banco de dados com Docker:</strong></summary><br />

<code>docker-compose up -d mongodb</code>

 </details>
 
 ## Rodando a aplicação:
 
 Ao finalizar os demais passos você poderá interagir com a aplicação através do terminal interativo apenas digitando a chamada abaixo:
 
 <code>python3 -m tech_news.main.</code>

 
