def cadastro():
    nome=input('digite seu nome: ')
    cpf=input('digite seu CPF')
    with open(r'C:\cpf_nome.txt','a') as f:
        if len(nome) < 30:
            f.write('\n')
            f.write(cpf +' '+ nome+' '*(30-len(nome))+' ')  #completar o nome com ' '
        elif len(nome)==30:
            f.write('\n')
            f.write(f'{nome} ')
        else:
            f.write('\n')
            f.write(f'{nome[0:30]} ')
        f.write('0')


def compra():
    valor = input('digite o valor com duas casas decimais: ')
    cpf = input('digite o cpf: ')
    data = input('digita a data')
    pontos = str(int(float(valor) // 100))
    if len(valor) < 8:
        valor = '0' * (8 - len(valor)) + valor      #completar o valor com '0', ate chegar em 8 caracteres
    if len(pontos) < 3:
        pontos = '0'*(3-len(pontos))+pontos
    for i in valor:
        if i ==',':
            i.replace(',','.')


    with open(r'C:\cpf_nome.txt','r') as f:
        r=0
        for i in f.readlines():
            if i[0:11] == cpf:
                nome = i[12:31]
                r=1
        if r ==0:
            print('este cliente ainda nao é cadastrado, preencha as informações abaixo: ')   #caso o nome nao esteja cadastrado
            cadastro()
            compra()


    with open(r'C:\historico de compras.txt', 'a') as f:
        f.write('\n')
        f.write(f'{cpf} {nome} {valor} {pontos} {data}')

    with open('C:\cpf_nome.txt','r') as cpf:
        with open(r'C:\historico de compras.txt','r') as historico:
            CpfLista = []
            PontosLista = []
            pontos = 0
            linhascpf = cpf.readlines()
            linha_da_compra = historico.readlines()[len(historico.readlines())-1]
            for i in range(len(linhascpf)):
                CpfLista.append(linhascpf[i][0:11])
                PontosLista.append(linhascpf[i][43:46])
                if CpfLista[i] == linha_da_compra[0:11]:
                    PontosLista[i] = str(int(PontosLista[i]) + int(linha_da_compra[42:45]))


            with open(r'C:\historico de compras.txt' , 'r') as historico:
                linha_da_compra = historico.readlines()[len(historico.readlines())-1]
                with open('C:\cpf_nome.txt','w') as cpfw:
                    for i in range(len(CpfLista)):
                        if linha_da_compra[0:11] == CpfLista[i]:
                            linhascpf[i] = linhascpf[i][0:43] + PontosLista[i] + '\n'
                    cpfw.writelines(linhascpf)
compra()