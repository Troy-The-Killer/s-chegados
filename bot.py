#!/usr/bin/env python3
#-*- coding: UTF-8 -*-
#
# Autor: Troy Oliveira
#

import discord
import random

client = discord.Client()
vermelho = 0xFF0000

@client.event
async def on_ready():
    print('-------------- Online --------------')
    print('Nome: {}'.format(client.user.name))
    print('  ID: {}'.format(client.user.id))
    print('------------------------------------')

    await client.change_presence(game=discord.Game(name="=help", type=1))

############################################################################################################

# 1° Evento - Entrada no Servidor:
@client.event
async def on_member_join(member):

    # Sala de Entrada - Onde o bot vai se'manifestar:
    entrada = client.get_channel("459461285046910996")

    # Mensagens boas-vindas - Será a mensagem que o bot vai enviar:
    mensagem = "Olá {}, Bem-vindo ao `Só os chegados 2.0`.".format(member.mention)

    # Imprimindo a mensagem - Imprimindo mensagem à cima:
    await client.send_message(entrada, mensagem)

############################################################################################################

# 2° Evento - Saída do Servidor:
@client.event
async def on_member_remove(member):

    # Sala de saída:
    saida = client.get_channel("459461355498373130")

    # Mensagem de saída:
    mensagem = "Até nunca mais {}...".format(member.mention)

    # Imprimindo a mensagem de saída:
    await client.send_message(saida, mensagem)

@client.event
async def on_message(message):
    if message.content.lower().startswith('=amor'):
        global medidor
        
        Numeros = random.randrange(0, 99)
        Membro = message.mentions[0]
        Autor = message.author
        
        if Numeros <= 15:
            medidor = discord.Embed(
                color=vermelho,
                description='💞  **Medidor de amor** 💞\n\n💘 **{}**\n💘 **{}**\n\n» `{}%`\n\nMensagem: `Vocês não combinam um com o outro.`\n'.format(Autor, Membro, Numeros),
            )
            
        elif Numeros <= 30:
            medidor = discord.Embed(
                color=vermelho,
                description='💞  **Medidor de amor** 💞\n\n💘 **{}**\n💘 **{}**\n\n» `{}%`\n\nMensagem: `Apenas amigos, porém, leais.`\n'.format(Autor, Membro, Numeros),
            )

        elif Numeros <= 50:
            medidor = discord.Embed(
                color=vermelho,
                description='💞  **Medidor de amor** 💞\n\n💘 **{}**\n💘 **{}**\n\n» `{}%`\n\nMensagem: `Da para formar um belo casal.`\n'.format(Autor, Membro, Numeros),
            )
            
        elif Numeros <= 75:
            medidor = discord.Embed(
                color=vermelho,
                description='💞  **Medidor de amor** 💞\n\n💘 **{}**\n💘 **{}**\n\n» `{}%`\n\nMensagem: `Vai dar namoro, Vai dar namoro...` 🎵\n'.format(Autor, Membro, Numeros),
            )
            
        elif Numeros <= 100:
            medidor = discord.Embed(
                color=vermelho,
                description='💞  **Medidor de amor** 💞\n\n💘 **{}**\n💘 **{}**\n\n» `{}%`\n\nMensagem: `Juntos até a morte!`\n'.format(Autor, Membro, Numeros),
            )

    ############################################################################################################

    if message.content.lower().startswith('=py'):
        msg = message.content.strip('=py')
        await client.send_message(message.channel, message.author.mention+' enviou o segunte código:' + '\n```python\n{}\n```'.format(msg))

    if message.content.lower().startswith('=autor'):
        await client.send_message(message.channel, '`Troy Oliveira`')

    ############################################################################################################

    if message.content.lower().startswith('=help'):
        embed1 = discord.Embed(
            title="HELP:",
            color=0x4d0083,
            description='\n:small_blue_diamond: `=help`\t\tVocê está aqui agora!\n:small_blue_diamond: `=avatar`\tVer avatar do membro!\n:small_blue_diamond: `=avisos`\tAvisos de eventos ou algo do tipo!\n:small_blue_diamond: `=py`\t\t\t Imprimir códigos em python\n'
        )
        await client.send_message(message.channel, embed=embed1)


    ############################################################################################################

    if message.content.lower().startswith('=avatar'):
        try:
            membro = message.mentions[0]

            embed1 = discord.Embed(
                title="Avatar",
                color=0x4d0083,
                description='[Clique aqui]('+membro.avatar_url+') para acessar o link do avatar de {}!'.format(membro.name)
            )
            embed1.set_image(url=membro.avatar_url)
            await client.send_message(message.channel, embed=embed1)

        except:
            membro = message.author

            embed = discord.Embed(
                title='Seu avatar:'.format(membro.name),
                color=0x4d0083,
                description='[Clique aqui]('+membro.avatar_url+') para acessar o link do seu Avatar  '.format(membro.name)
            )
            embed.set_image(url=membro.avatar_url)
            await client.send_message(message.channel, embed=embed)

    ############################################################################################################

    if message.content.lower().startswith('=avisos'):
        role = discord.utils.get(message.server.roles, name='avisos')
        if not role in message.author.roles:
            embed1 = discord.Embed(
                title=':warning: Ocorreu um Erro!',
                color = 0xff0000,
                description="`Você não tem permissão:` Você precisa do cargo @avisos para utilizar."
            )
            embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            return await client.send_message(message.channel, embed=embed1)

        msg = message.content.strip('=avisos')

        embed2 = discord.Embed(
            title=':hourglass: Enviado Mensagem...',
            color=0x7289DA,
            description="`Mensagem: `\n**{}**".format(msg)
        )

        embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
        await client.send_message(message.channel, embed=embed2)

        x = list(message.server.members)
        s = 0
        
        for member in x:
            embed1 = discord.Embed(color=0x1ce1de, description=(msg))
            embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)

            try:
                await client.send_message(member, embed=embed1)
                print(member.name)
                s += 1

            except:
                pass
        print('\nAviso enviado para {} membros de {}'.format(s, len(x)))
        embed2 = discord.Embed(
            title=':thumbsup: Mensagem Enviada Com Sucesso!',
            color=0x42f445,
            description=":ok_hand:"
        )

        embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
        await client.send_message(message.channel, embed=embed2)

    ############################################################################################################

    if message.content.lower().startswith('=registro'):
        embed = discord.Embed(
            title="Faça seu Registro:",
            color=0xE91A21,
            description="👩  →  Mulher\n\n"
                        "👨  →  Homem\n\n"
                        "💻  →  Computador\n\n"
                        "📱  →  Celular\n\n"
                        "🔼  →  +18\n\n"
                        "🔽  →  -18",
        )

        botmsg = await client.send_message(message.channel, embed=embed)

        await client.add_reaction(botmsg, "👩")
        await client.add_reaction(botmsg, "👨")
        await client.add_reaction(botmsg, "💻")
        await client.add_reaction(botmsg, "📱")
        await client.add_reaction(botmsg, "🔼")
        await client.add_reaction(botmsg, "🔽")

        global msg_id
        msg_id = botmsg.id

        global msg_user
        msg_user = message.author

@client.event
async def on_reaction_add(reaction, user):

    msg = reaction.message

    if reaction.emoji == "👩" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Mulher", msg.server.roles)
        await client.add_roles(user, role)

    if reaction.emoji == "👨" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Homem", msg.server.roles)
        await client.add_roles(user, role)

    if reaction.emoji == "💻" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Computador", msg.server.roles)
        await client.add_roles(user, role)

    if reaction.emoji == "📱" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Celular", msg.server.roles)
        await client.add_roles(user, role)

    if reaction.emoji == "🔼" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "+18", msg.server.roles)
        await client.add_roles(user, role)

    if reaction.emoji == "🔽" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "-18", msg.server.roles)
        await client.add_roles(user, role)

@client.event
async def on_reaction_remove(reaction, user):

    msg = reaction.message

    if reaction.emoji == "👩" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Mulher", msg.server.roles)
        await client.remove_roles(user, role)

    if reaction.emoji == "👨" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Homem", msg.server.roles)
        await client.remove_roles(user, role)

    if reaction.emoji == "💻" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Computador", msg.server.roles)
        await client.remove_roles(user, role)

    if reaction.emoji == "📱" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Celular", msg.server.roles)
        await client.remove_roles(user, role)

    if reaction.emoji == "🔼" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "+18", msg.server.roles)
        await client.remove_roles(user, role)

    if reaction.emoji == "🔽" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "-18", msg.server.roles)
        await client.remove_roles(user, role)

        
client.run('NDU5NDE1NjgzOTkwODE0NzQw.Dg2Pzw.LEzta0HWqBmHGvXohe1IPvxbICc')
