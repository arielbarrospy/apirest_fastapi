# apirest_fastapi
1 - criar/atualizar/deletar/fazer login de usuario
2 - criar/atualizar/listar produtos
3 - fazer pedidos ver vendas e ver compras
4 - criptografia de senha 
5 - geração de JWT token Bearer authentication, após login  

para que tudo rode bem, rode o comado em seu terminal pip install fastapi[all]
isso irá baixar e instalar todas dependências do fastapi na sua maquina

para iniciar o projeto basta ir ate o diretório do arquivo server.py 
e prosseguir com o seguinte comando  uvicorn server:app --reload 
e pronto tera uma api rodando seu localhost !

para fazer requisições para essa api depois de inicia-la mande suas requisições
para o endereço http://127.0.0.1:8000/ dentro da pasta routers terá arquivos .py com
nomer de router_user router_product router_orders dentro desses arquivos poderá
ver as rotas das quais poderá mandar requisições !
as rotas são:

    /usuarios GET para listar todos usuarios
    /usuarios POST para criar um novo usuario
    /usuarios/{id} GET para obter um usuario com determinado ID
    /usuarios/{id} PUT para atualizar um usuario sendo que ara esta também é necessari mandar um objeto do tipo json com os dados a serem atualizado :)
    /usuarios/{id} DELETE para deletar um usuario utilizando seu ID
    /token POST login de usuario retorna um objeto json contendo o usuario logado e um novo JWT token Bearer
    /me para listar suas vendas e seus produtos
    
    
    /pedidos GET listar todos os pedidos realizados
    /pedidos POST criar um novo pedido
    /vendas/{usuario_id} GET obter todas vendas de determinado usuario tilizando seu ID
    
    /produtos GET listar todos produtos cadastrados no banco de dados
    /produtos POST criar novo produto

qualquer duvida so chamar (11)91717-0528 gosto de fazer novos projetos para estudar e ficarei feliz em poder estudar junto com você !(:
