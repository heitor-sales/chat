import flet as ft

#função principal
def main(pagina):
    #criação do chat
    chat = ft.Column()

    #criação do túnel de comunicação
    def enviar_mensagem_no_tunel(mensagem):
        #adicionar mensagem no chat
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)

        #atualização da página
        pagina.update()

    #criação do túnel de comunicação
    pagina.pubsub.subscribe(enviar_mensagem_no_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}")

        #limpe o campo mensagem
        campo_mensagem.value = "" 
        
        #atualização da página
        pagina.update()

    #para enviar que o usuário está digitando, use on_change=
    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    #função para entrar no chat
    def entrar_chat(evento):
        #fechar o popup
        popup.open=False

        #fechar o botão iniciar chat
        pagina.remove(botao_iniciar)
        
        #tirar o título hashzap
        pagina.remove(texto)
        
        #adição do chat na página
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        #adição do campo de digitar mensagem e do botão de enviar
        pagina.add(linha_enviar)

        #atualização da página para a exibição das alterações feitas
        pagina.update()

    #criação dos elementos da página
    texto = ft.Text("Hashzap")
    titulo_popup = ft.Text("Bem-vindo ao Hashzap")
    
    #usando on_submit= para enviar usando enter 
    nome_usuario = ft.TextField(label="Escreva seu nome no chat", on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton("Entar no chat", on_click=entrar_chat)
    popup = ft.AlertDialog(open=False, modal=True, title=titulo_popup, content=nome_usuario, actions=[botao_entrar])

    #criação da função para o evento que acontecerá ao aperta o botão "Iniciar chat"
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True

        #atualização da página para a exibição das alterações feitas
        pagina.update()
    
    #criação do botão para iniciar o chat
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)
    
    #alinhar o campo de mensagem e o botão de enviar fiquem na mesma linha, um ao lado do outro
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])

    #adicionando elemento à página
    pagina.add(texto)
    pagina.add(botao_iniciar)

#criar o app chamando a função princial e usando parâmetro para tornar o app em site
ft.app(target=main, view=ft.WEB_BROWSER)