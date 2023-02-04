from controle import * 

tv =  Televisor('Samsung','Samsung series 6' )

controle = ControleRemoto(tv)

controle.adicionaCanal('GLOBO')
controle.trocaCanal('GLOBO')



print(tv.canal_atual)