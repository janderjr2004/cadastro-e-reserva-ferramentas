# cadastro-e-reserva-ferramentas
Projeto da faculdade que consiste em criar um aplicativo desktop para uma empresa contendo a reserva de ferramentas, também contando com cadastro de técnicos e das próprias ferramentas.


----------------------------------------------------------------------  COMO FUNCIONA  ----------------------------------------------------------------------

O programa é dividido em duas telas principais, sendo uma dos administradores e outra dos funcionários, as telas contam com o seguinte:

    ADMINISTRADORES:

      TÉCNICOS:

        * Pode ser efetuado o cadastro dos técnicos a partir da tela principal dos administradores, sendo cadastrado seu CPF, nome, telefone, turno e equipe. 
        * O cadastro do técnico só poderá ser realizado se o CPF for verdadeiramente válido, e sendo validado na hora do cadastro, assim como os outros campos só contarão se forem válidos.
        * Cada técnico pode ser excluído do cadastro quando for necessário, assim como pode ser gerado uma tabela através de um treeview do TKinter puxando os dados do banco de dados e consultar técnico por técnico ou todos juntos.
        * Um técnico vinculado a uma reserva não pode ser excluído a não ser que a ferramenta reservada já tenha sido devolvida.
        * Quando o técnico é cadastrado automaticamente é gerado um cadastro para o mesmo, utilizando um username com seu nome e sobrenome. Ex: Jander Júnior (janderjunior), e tendo como senha o CPF do técnico.

      FERRAMENTAS:

        * O cadastro das ferramentas é feito a partir da tela principal dos administradores também, sendo cadastrado um ID (gerado automaticamente pelo banco de dados), descrição da ferramenta, fabricante, voltagem de uso, part number, un. de medida, tamanho, tipo, material e tempo máximo de reserva (em horas).
        * O cadastro também só é feito se todos os campos marcados como essenciais estiverem preenchidos e não houver erro nos mesmos.
        * Uma ferramenta vinculada a uma reserva não pode ser excluída do cadastro a não ser que ela já tenha sido devolvida.

      RESERVAS:

        * A reserva só poderá ser feita se a ferramenta e o técnico que irá pegá-la estiverem registrados no sistema.
        * Para reservar uma ferramenta deve-se enviar um pedido diretamente pelo aplicativo, na aba dos funcionários, onde chegará um email até o(s) administrador(es) da ala das ferramentas e assim avaliará se a ferramenta pode ser reservada.
        * Se a ferramenta puder ser reservada, o administrador da ala irá retornar o email por conta própria e reservar a ferramenta pela aba dos administradores.
        * Se o tempo máximo de reserva da ferramenta for excedido ao reservá-la, a mesma não irá ser reservada e apresentará erro ao tentar,assim como todos os campos inválidos que existirem.
        * Ao se colocar o CPF do técnico é puxado automaticamente seu nome para o campo de nome da ala de registro de reservas.
        * Quando uma reserva estiver em atraso, ao abrir o aplicativo na parte dos administradores será mostrado um popup exibindo quais IDs de ferramentas estão em atraso.
    
    FUNCIONÁRIOS:
    
      * O funcionário pode logar no aplicativo através do seu login gerado quando é cadastrado no sistema.
      * É aberta uma tela apenas onde pode se fazer o pedido da reserva, que é enviado diretamente ao email do administrador da ala.
