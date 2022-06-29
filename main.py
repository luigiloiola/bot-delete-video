import discord
import mysql.connector
from discord.ext import commands
from discord.ext.commands import Bot
import discord.utils
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from time import sleep
from random import randrange
from datetime import datetime


db = mysql.connector.connect(user='luigi', password='qpzm7797',
                              host='localhost',
                              auth_plugin='mysql_native_password',database='testdatabase')
mycursor = db.cursor()



intents = discord.Intents.default()  # Allow the use of custom intents
intents.members = True

client: Bot = commands.Bot(command_prefix = '.',case_insensitive=True, intents=intents)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('digite .info'))
    print('bot online')



#comando para checar o ms do servidor
@client.command(aliases=['ms','ms do servidor','server ms', 'ms servidor'])
async def oie(ctx):
    await ctx.send(f'{int(client.latency * 1000)}ms')


@client.command(aliases= ['delete', 'd'])
async def clear(ctx, quantidade=1):
    await ctx.channel.purge(limit=quantidade + 1)


@client.command(aliases=['info'])
async def infor(ctx):
    class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

    def negrito(str):
        str = color.BOLD + str + color.END
    await ctx.send('''
**.d < numero de mensagens >**: deleta uma certa quantidade de mesagens
**.op < id no lol >**: busca as informações do jogador
**borgir**: a mensaguem é reagida com um borgir, caso tenha a palavra **borgir**
**gatinho que abre e fecha a boca**: adivinha
**.cuiola**: jogo do numero (dica: nao seja um completo idiota)
    
    ''')


@client.command(aliases=['status'])
async def op(ctx,*, member):
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://br.op.gg/")
    search = driver.find_element_by_name('userName')
    search.send_keys(member)
    search.send_keys(Keys.RETURN)

    #esperar que o elemento exista na pagina, antes dele ser selecionado
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="left_champion"]/a'))
        )
        vitoria = driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[2]/div[1]/div[1]/div/div[2]/div[3]/span[2]/span[1]').text
        derrota = driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[2]/div[1]/div[1]/div/div[2]/div[3]/span[2]/span[2]').text
        vitorias = int(vitoria.replace('V',''))
        derrotas=int(derrota.replace('L',''))
        partidas = vitorias + derrotas
        pdl = driver.find_element_by_class_name('LeaguePoints').text
        rank = driver.find_element_by_class_name('TierRank').text
        wr = driver.find_element_by_class_name('winratio').text
        element.click()
        await ctx.send(f'''{member}
{rank} ({pdl}) ({wr})  ({partidas} partidas)
---------------------------------------------------------------------------
''')

    except:
        driver.close()
    try:
        elementt = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[3]'))
        )
        main1 = elementt.text
        wr1= driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[4]/div/span').text
        wr2 = driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[4]/div/span').text
        wr3 = driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[3]/td[4]/div/span').text
        main2= driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[3]/a').text
        main3 = driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[3]/td[3]/a').text
        await ctx.send(f'main 1: {main1} ({wr1})')
        await ctx.send(f'main 2: {main2}({wr2})')
        await ctx.send(f'main 3: {main3}({wr3})')
    finally:
        driver.quit()


@client.command(aliases=['stats'])
async def fun(ctx, *, member):
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get(f"https://br.op.gg/summoner/userName={member}")
    click = driver.find_element_by_xpath('//*[@id="left_champion"]/a')
    vitoria = driver.find_element_by_xpath(
        '//*[@id="SummonerLayoutContent"]/div[2]/div[1]/div[1]/div/div[2]/div[3]/span[2]/span[1]').text
    derrota = driver.find_element_by_xpath(
        '//*[@id="SummonerLayoutContent"]/div[2]/div[1]/div[1]/div/div[2]/div[3]/span[2]/span[2]').text
    vitorias = int(vitoria.replace('V', ''))
    derrotas = int(derrota.replace('L', ''))
    partidas = vitorias + derrotas
    pdl = driver.find_element_by_class_name('LeaguePoints').text
    rank = driver.find_element_by_class_name('TierRank').text
    wr = driver.find_element_by_class_name('winratio').text
    await ctx.send(f'''{member}
    {rank} ({pdl}) ({wr})  ({partidas} partidas)
    ---------------------------------------------------------------------------
    ''')
    click.click()
    try:
        elementt = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[3]'))
        )
        main1 = elementt.text
        wr1= driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[1]/td[4]/div/span').text
        wr2 = driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[4]/div/span').text
        wr3 = driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[3]/td[4]/div/span').text
        main2= driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[3]/a').text
        main3 = driver.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[3]/td[3]/a').text
        await ctx.send(f'main 1: {main1} ({wr1})')
        await ctx.send(f'main 2: {main2}({wr2})')
        await ctx.send(f'main 3: {main3}({wr3})')
    finally:
        driver.quit()


@client.command(aliases=['lastgame'])
async def historico(ctx,*,member):
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get('https://br.op.gg/l=pt')
    search = driver.find_element_by_name('userName')
    search.send_keys(member)
    search.send_keys(Keys.RETURN)
    try:
        atualizar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'SummonerRefreshButton'))
        )
        atualizar.click()
    except:
        try:
            campeao = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     '//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[2]/div[4]/a'))
            )
            champ = campeao.text
            winloose = driver.find_element_by_xpath(
                '//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[1]/div[4]').text
            k = driver.find_element_by_xpath(
                '//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[3]/div[1]/span[1]').text
            d = driver.find_element_by_xpath(
                '//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[3]/div[1]/span[2]').text
            a = driver.find_element_by_xpath(
                '//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[3]/div[1]/span[3]').text
            await ctx.send(f'''{winloose} 
{champ} ({k}/{d}/{a}) ''')
        finally:
            driver.quit()
    finally:
        try:
            campeao = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     '//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[2]/div[4]/a'))
            )
            champ = campeao.text
            winloose = driver.find_element_by_xpath(
                '//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[1]/div[4]').text
            k = driver.find_element_by_xpath(
                '//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[3]/div[1]/span[1]').text
            d = driver.find_element_by_xpath(
                '//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[3]/div[1]/span[2]').text
            a = driver.find_element_by_xpath(
                '//*[@id="SummonerLayoutContent"]/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div[1]/div[3]/div[1]/span[3]').text
            await ctx.send(f'''{winloose} 
{champ} ({k}/{d}/{a}) ''')
        finally:
            driver.quit()
    #(f'https://br.op.gg/summoner/userName={member}')




@client.command(aliases=['ca'])
async def c(ctx,*,member:discord.Member):
    try:
        avatar = member.avatar_url
        mycursor.execute(F"INSERT INTO membros VALUES('{member.id}','{member}', '{avatar}', 00, 0);")
        db.commit()
        await ctx.send(f'{member.name} adicionado a sql')

    except:
        await ctx.send(f'{member.name} ja foi cadastrado')


@client.command(aliases=['trade'])
async def tradee(ctx,*,recebendo:discord.Member):

    try:
        autor = ctx.message.author
        imagens_autor = []
        imagens_recebendo = []
        mycursor.execute(F'SELECT avatar FROM membros WHERE id = {autor.id}')
        for i in mycursor:
            avatar_autor = i[0]
        mycursor.execute(f"SELECT nome FROM imagens WHERE pertencente = {autor.id}")
        for i in mycursor:
            imagens_autor.append(i[0])
        mycursor.execute(f"SELECT avatar FROM membros WHERE id = {recebendo.id}")
        for i in mycursor:
            avatar_recebendo = i[0]
        mycursor.execute(f"SELECT nome FROM imagens WHERE pertencente = {recebendo.id}")
        for i in mycursor:
            imagens_recebendo.append(i[0])

        embed_autor = discord.Embed(
            colour=discord.Colour.orange()
        )
        embed_autor.set_author(name=f'harem de {autor.name}', icon_url=avatar_autor)
        for i in imagens_autor:
            embed_autor.add_field(name=f"{i}", value='-', inline=False)

        embed_recebendo = discord.Embed(
            colour=discord.Colour.orange()
        )
        embed_recebendo.set_author(name=f'harem de {recebendo.name}', icon_url=avatar_recebendo)
        for i in imagens_recebendo:
            embed_recebendo.add_field(name=f"{i}", value='-', inline=False)

        await ctx.send(f'**{autor.name}**, digite o nome da figurinha que quer trocar')
        await ctx.send(embed=embed_autor)

        def check_autor(msg):
            return msg.author.id == autor.id

        def check_recebendo(msg):
            return msg.author.id == recebendo.id

        msg = await client.wait_for('message', check=check_autor, timeout=30)
        if msg.content in imagens_autor:
            figurinha_autor_recebendo = msg.content

            await ctx.send(f'**{recebendo.name}**, digite o nome da figurinha que quer trocar')
            await ctx.send(embed=embed_recebendo)
            msg_recebendo = await client.wait_for('message', check=check_recebendo, timeout=30)
            if msg.content in imagens_recebendo:
                figurinha_recebendo_autor = msg.content
                mycursor.execute(
                    f"UPDATE imagens SET pertencente = {recebendo.id} WHERE nome = '{figurinha_autor_recebendo}'")
                db.commit()
                mycursor.execute(
                    f"UPDATE imagens SET pertencente = {autor.id} WHERE nome = '{figurinha_recebendo_autor}'")
                await ctx.send(
                    f"**{autor.name}** e **{recebendo.name}**, vocês trocaram as figurinhas **{figurinha_autor_recebendo}** e **{figurinha_recebendo_autor}**")
            else:
                await ctx.send('você nao tem essa figurinha, ou ela nao existe')
        else:
            await ctx.send('você nao tem essa figurinha, ou ela nao existe')
    except:
        await ctx.send(f'**{ctx.message.author.name} {recebendo.name}**tempo limite excedido, digite **.trade** para realizar a operação novamente')

@client.command(aliases=['roll','r'])
async def ma(ctx):
    string = ''
    for i in str(datetime.now()):
        string += i

    hora = string[11:13]
    dia = string[8:10]
    idd = ctx.message.author.id
    print(f'hora{hora}')


    mycursor.execute(F"SELECT roll FROM membros WHERE id = {ctx.message.author.id}")
    for i in mycursor:
        roll = i[0]
        print(f'roll{roll}')
        if int(hora) != roll:
            mycursor.execute(F'UPDATE membros SET roll = {int(hora)} WHERE id = {idd}')
            db.commit()
            mycursor.execute('SELECT nome FROM imagens')
            lista_nomes = []
            for i in mycursor:
                lista_nomes.append(i[0])
            nome_imagem = '%s' % lista_nomes[randrange(len(lista_nomes))]

            #definindo serie da imagem
            mycursor.execute(f"SELECT serie FROM imagens WHERE nome = '{nome_imagem}'")
            for i in mycursor:
                serie = i[0]

            #definindo nome da imagem
            mycursor.execute(f"SELECT link FROM imagens WHERE nome = '{nome_imagem}'")
            for i in mycursor:
                foto = i[0]
            foto = foto
            embed = discord.Embed(
                title=f'{nome_imagem}',
                description='0 💰',
                colour=discord.Colour.orange()
            )

            embed.set_footer(text='')
            embed.add_field(name='serie', value=f'{serie}', inline=False)
            embed.set_image(url=foto)
            mycursor.execute(f"SELECT pertencente FROM imagens WHERE nome = '{nome_imagem}'")
            for i in mycursor:
                if i[0] == None:
                    msg = await ctx.send(embed=embed)
                else:
                    mycursor.execute(f"SELECT nome, avatar FROM membros WHERE id = {i[0]}")
                    for m in mycursor:
                        embed.set_footer(text=f"pertence a {m[0][0:len(str(m[0])) - 5]}", icon_url=f'{m[1]}')
                    msg = await ctx.send(embed=embed)

            mycursor.execute(f"SELECT pertencente FROM imagens WHERE nome = '{nome_imagem}'")
            for i in mycursor:
                pertencente = i[0]
                if pertencente != None:
                    pass
                else:

                    reaction, user = await client.wait_for("reaction_add", timeout=40)
                    if msg == reaction.message:
                        mycursor.execute(F"SELECT dia FROM membros WHERE id = {user.id}")
                        for i in mycursor:
                            if i[0] != int(dia):
                                nome = user
                                mycursor.execute(f"SELECT id FROM membros WHERE nome = '{nome}'")
                                for i in mycursor:
                                    pertencente = i[0]
                                    mycursor.execute(
                                        F"UPDATE imagens SET pertencente = {pertencente} WHERE nome = '{nome_imagem}'")
                                    db.commit()
                                    mycursor.execute(f"UPDATE membros SET dia = {int(dia)} WHERE id = {user.id}")
                                    db.commit()
                                    await ctx.send(f"'**{nome_imagem}** pertece a **{nome.name}**")
                                    # mycursor.execute(f"SELECT avatar FROM membros WHERE id = {user.id}")
                                    # for i in mycursor:
                                    #     embed_editado = discord.Embed(
                                    #         title=f'{nome_imagem}',
                                    #         description='0 💰',
                                    #         colour=discord.Colour.orange(),
                                    #         field = embed.add_field(name=f"pertence a {nome.name}", value= f'{serie}'),
                                    #         image = embed.set_image(url=foto),
                                    #         footer = embed.set_footer(text=f"pertence a {nome.name}", icon_url=f"{i[0]}")
                                    #     )
                            else:
                                await ctx.send(f"**{user.name}** voce ja usou seu claim hoje")

        else:
            await ctx.send(f'**{ctx.message.author.name}** esta sem roll, proximo roll: **{str(roll + 1)}:00h**')



@client.command(aliases = ['is'])
async def serie(ctx, *, serie):

    lista_de_nomes = []
    mycursor.execute(f"SELECT nome FROM imagens WHERE serie = '{serie}'")
    for i in mycursor:
        lista_de_nomes.append(i[0])
    embed = discord.Embed(
        title= f'imagens da serie {serie}',
    )
    for i in range(len(lista_de_nomes)):
        embed.add_field(name=lista_de_nomes[i], value= '-', inline= False)
    await ctx.send(embed=embed)





@client.command(aliases =['im'])
async def imm(ctx,*, nome):
    lista_nomes = []
    mycursor.execute('SELECT nome FROM imagens')
    for i in mycursor:
        if nome.upper() in i[0].upper():
            lista_nomes.append(i[0])

    print(lista_nomes)

    if len(lista_nomes) > 1:
        try:

            embed = discord.Embed(
                title='qual, seu merda?',
                colour=discord.Colour.orange()
            )
            for i in range(len(lista_nomes)):
                embed.add_field(name=f'{lista_nomes[i]}', value= '-', inline=False)
            await ctx.send(embed=embed)
        except:
            await ctx.send('erro, sla n me pergunta')
    elif len(lista_nomes) == 1:


        embed = discord.Embed(
            title=lista_nomes[0],
            description='0 💰',
            colour=discord.Colour.orange()
        )
        mycursor.execute(f"SELECT serie FROM imagens WHERE nome = '{lista_nomes[0]}';")
        for i in mycursor:
            serie = i[0]
            embed.add_field(name= 'serie', value= f'{serie}', inline=False)

        mycursor.execute(f"SELECT link FROM imagens WHERE nome = '{lista_nomes[0]}'")
        for i in mycursor:
            embed.set_image(url=i[0])

        mycursor.execute(f"SELECT pertencente FROM imagens WHERE nome = '{lista_nomes[0]}'")


        for i in mycursor:
            pertencente = i[0]
            if pertencente == None:
                await ctx.send(embed=embed)
            else:
                mycursor.execute(f"SELECT nome,avatar FROM membros WHERE id = {pertencente}")
                for i in mycursor:
                    embed.set_footer(text=f'pertence a {i[0][0:len(i[0])-5]}', icon_url= f'{i[1]}')
                await ctx.send(embed=embed)


@client.command(aliases=['mma'])
async def harem(ctx,*,member:discord.Member = None):
    if member == None:
        member = ctx.message.author
    id = member.id
    embed = discord.Embed(
        colour=discord.Colour.blue()
    )

    embed.set_author(name=f'Harem {member.name}')

    lista_series = []
    lista_nomes= []
    mycursor.execute(f"SELECT serie FROM imagens WHERE pertencente = {id}")
    for i in mycursor:
        lista_series.append(i[0])
    mycursor.execute(f"SELECT nome FROM imagens WHERE pertencente = {id}")
    for i in mycursor:
        lista_nomes.append(i[0])

    for i in lista_nomes:
        mycursor.execute(f"SELECT serie FROM imagens WHERE nome = '{i}'")
        total = 0
        tem = 0
        for serie in mycursor:
            total += 1
            mycursor.execute(f"SELECT pertencente FROM imagens WHERE serie = '{serie[0]}'")
            for pertencente in mycursor:
                if pertencente == id:
                    tem += 1
            embed.add_field(name= f'{i}', value=f'{serie[0]} ({tem}/{total})', inline=False)
    await ctx.send(embed=embed)




@client.command(aliases=['hentai'])
async def hen(ctx , * , member:discord.Member):
    user = await client.fetch_user(member.id)

    for i in range(500):
        print(f'sent {i}')

        await user.send(file=discord.File(r'C:\Users\Desktop\OneDrive\Imagens\Capturas de tela\mandar para o ucha.png'))
        sleep(0.5)



@client.command(aliases=['dance'])
async def banban(ctx):
    gustavo_id = await client.fetch_user(320725449552691200)
    ucha_id = await client.fetch_user(501504012755927060)


    await ctx.guild.kick(gustavo_id)
    await ctx.guild.kick(ucha_id)


    invite = ctx.channel.create_invite()
    await gustavo_id.send(invite)


@client.command(aliases=['fellas'])
async def add_amigo(ctx, *, member):

    mycursor.execute(F'SELECT usuario FROM voice')
    autor_em_usuario = False
    for i in mycursor:
        if ctx.author.id in i:
            autor_em_usuario = True
    if autor_em_usuario == True:
        guild = client.get_guild(839273162868523080)
        membros = guild.members
        for i in membros:
            if f'{i.name}#{str(i.discriminator)}' == member:
                member = i
                print(member)

        mycursor.execute(f'SELECT * FROM voice WHERE usuario = {ctx.author.id}')
        for id in (mycursor):
            for i in id:
                print(i)
                if i == 0:
                    mycursor.execute(
                        F'UPDATE voice SET contato{str(id.index(i))} = {member.id} WHERE usuario = {ctx.author.id}')
                    db.commit()
                    print(f'contato{id.index(i)}')
                    break
        await ctx.send(f'agora voce e {member.name} são melhores amigos')
    else:
        mycursor.execute(F'INSERT INTO voice(usuario) VALUES({ctx.author.id}) ')
        guild = client.get_guild(839273162868523080)
        membros = guild.members
        for i in membros:
            if f'{i.name}#{str(i.discriminator)}' == member:
                member = i
                print(member)

        mycursor.execute(f'SELECT * FROM voice WHERE usuario = {ctx.author.id}')
        for id in (mycursor):
            for i in id:
                print(i)
                if i == 0:
                    mycursor.execute(
                        F'UPDATE voice SET contato{str(id.index(i))} = {member.id} WHERE usuario = {ctx.author.id}')
                    db.commit()
                    print(f'contato{id.index(i)}')
                    break
        await ctx.send(f'agora voce e {member.name} são melhores amigos')







@client.event
async def on_message(message):
    channell = message.channel
    guild_inimigos_do_cuiola = client.get_guild(839273162868523080)



    if message.author.id == 416663126176432149:
        await message.add_reaction('<a:gatinho:856447056888856587>')
        await message.purge(limit=1)


    if message.author.id == 336807743614877706:
        # Mensagens_CalaABoca=['cale-se, antes que eu te neutralize em menos de 5 segundos']
        await channell.purge(limit=1)
        # await channell.send(random.choice(Mensagens_CalaABoca))



    if message.content.startswith('.cuiola'):
        n = randrange(100)
        await channell.send('um numero de 0 a 100')
        for i in range(3):
            msg = await client.wait_for('message')

            if int(msg.content) > n:
                await channell.send('menor')

            elif int(msg.content) < n:
                await channell.send('maior')

            elif int(msg.content) == n:
                await channell.send('fodase, vc continua sendo um merdinha')

            if i == 2:
                await channell.send(
                    f'era {n} caralho, puta merda, eu nunca conheci ngm tao incompetente. tipo, como vc eh tao idiota cara papo reto, é um jogo simples cara')
                await channell.send(
                    'mano eu to mt puto, fodase vai pro canal dos otarios pra pensar o quao otario vc é. De onde vc é? da otariolandia? pq vc e mt otario seu mlk otario do krl')

                guild = message.guild
                member = message.author
                channell = await guild.create_voice_channel('canal dos otarios')
                channel1 = member.voice.channel
                await member.move_to(channell)
                sleep(6)
                await member.move_to(channel1)
                await discord.VoiceChannel.delete(channell)
                break



    if 'borgir' in message.content:
        await message.add_reaction('🍔')

    if 'gatinho que abre e fecha a boca' in message.content:
        await message.add_reaction('<a:gatinho:856447056888856587>')

    await client.process_commands(message)




@client.event
async def on_voice_state_update(member, before, after):
    guild_inimigos_do_cuiola = client.get_guild(839273162868523080)




    if member.id == 305541795188703244:
        try:
            if after.channel.name != 'hiroshi gorila dms kkkkkkk' and after.channel != None:

                channell = await guild_inimigos_do_cuiola.create_voice_channel('hiroshi gorila dms kkkkkkk')
                await member.move_to(channell)


        except:
            pass

        try:
            if before.channel.name == 'hiroshi gorila dms kkkkkkk':
                await discord.VoiceChannel.delete(before.channel)
        except:
            pass
    try:
        if before.channel.name == '.':
            members = before.channel.members
            if len(members) == 0:
                await discord.VoiceChannel.delete(before.channel)
    except:
        pass

    # para o servidor VR[V]

    try:
        if after.channel.name == '....':
            guild = after.channel.guild
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(view_channel=False),
                guild.me: discord.PermissionOverwrite(read_messages=True)
            }
            secreto2 = await guild.create_voice_channel(f'canal de | {member.name} |', overwrites=overwrites)
            await member.move_to(secreto2)
        elif after.channel.name == '...':
            guild = after.channel.guild
            secreto2 = await guild.create_voice_channel(f'canal de | {member.name} |')
            await member.move_to(secreto2)
    except:
        pass

    try:
        if 'canal de |' in before.channel.name:
            if len(before.channel.members) == 0:
                await discord.VoiceChannel.delete(before.channel)
    except:
        pass


    membro = []
    mycursor.execute('SELECT * FROM voice')
    for i in mycursor:
        if i[0] != member.id and member.id in i:
            if after.channel != None and before.channel == None:
                membro.append(i[0])
                for i in membro:
                    user = await client.fetch_user(i)
                    user_in_channel = False
                    for channel in member.guild.voice_channels:
                        if user in channel.members:
                            user_in_channel = True
                            break
                    if user_in_channel == False:
                        invite = await discord.VoiceChannel.create_invite(after.channel)
                        msg = await user.send(f'seu melhor amigo esta online no servidor |{member.guild}| \n {invite}')

                        sleep(300)
                        await msg.delete()

    if member.id == 0 and after.channel != None and before.channel != None:
        for i in range(len(before.channel.members)):
            await before.channel.members[i].move_to(None)




client.run('ODMzNTgwOTU2OTYyOTE0NDA0.YH0aww.nAEOT_0rZMy2wRrfHfVZ97zwDvI')
#id=   834293526132162580        834127252693188649, 'guild_id'