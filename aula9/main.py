#nome de um arquivo que da inicio a um projeto

import menu

while True:
    menu.menu_principal()
    
    #aq pode dar break, return e tals pra sair
    
    #precisa usar dicionario pra todo tipo de dado
    #nao quer dizer que dentro de um dicionario n tenha outro dicionario
    #ex, o dicionario end de aluno deve ser outro com a rua, numero, bairro e tals
    """ 
    outra opção
    import menu as m
    
    e depois 
    
    m.menu_principal()
    
    renomear é sugerido quando tem um arquivo com o nome muito grande
    
    tb é sossivel fazer
    
    from menu import menu_princiap()  
    e ai nao precisa por nada na frente la (menu.menu_principal() tipo esse menu.)
    
    """