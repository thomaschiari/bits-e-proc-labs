## Configurando seu plugin

É feito um acompanhamento do progresso nos labs via um plugin do pytest. Para configurá-lo você deverá adicionar essas linhas no fim do arquivo `~/.bashrc`.

```
export AUTH_TOKEN=(token recebido por email)
export AUTH_HOSTNAME=https://devlife.insper-comp.com.br
```

Além disso, você precisa ter o quartus 21.1 light instalado e configurado no `bashrc`:

```
export PATH=$PATH:$HOME/intelFPGA_lite/21.1/quartus/bin/
```
