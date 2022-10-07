#include <iostream>
#include <fstream>
#include <string>
#include <fast_food.h>
#include <menu_hamburguer.h>

using namespace std;

int main()
{
    /*
    int i = 0;
    cout << "Carregando\n";
    
    for (i=0; i<=1000000; i++)
    {
        if (i == 2500 || i == 5000 || i == 7500 || i == 10000)
        {
            cout << ".";
        }
    }
     */
    
    inicio_pedido();
}

void inicio_pedido()
{   
    int selecao_1;
    
    cout << "|| -------------- Burguer King ----------------- ||\n";
    cout << "|| ------------ Escoha uma opcao --------------- ||\n\n";
    cout << "   1 - Iniciar novo pedido\n";
    
    cin >> selecao_1;
    
    if (selecao_1 == 1)
    {
        menu_opcoes();
    }
    else
    {
        cout << "Selecao invalida";
    }    
    
}

void menu_opcoes()
{
    int selecao_2;
    
    cout << "|| -------------- Burguer King ----------------- ||\n\n";
    cout << "   1 - Cupons\n";
    cout << "   2 - Recompensas\n";
    cout << "   3 - Hamburgueres de carne\n";
    //cout << "   4 - Demais opcoes\n";
    
    cin >> selecao_2;
    
    if (selecao_2 == 1)
    {
        cupons();
    }
    else if (selecao_2 == 2)
    {
        recompensas();
    }
    else if (selecao_2 == 3)
    {
        menu_hamburguer();
    }
    else
    {
        cout << "Selecao invalida";
    }
}
void cupons()
{
    // adaptar para reconhecer string no lugar de um numero
    int codigo_cupom;
    cout << "Insira o codigo do cupom\n";
    
    cin >> codigo_cupom;
    
    //Verificar else if***
    if (codigo_cupom == 5)
    {
        tx_desconto = 0.05;
    }
    else if (codigo_cupom == 10)
    {
        tx_desconto = 0.10;
    }
    else if (codigo_cupom == 15)
    {
        tx_desconto = 0.15;
    }
    else
    {
        cout << "Cupom invalido";
    }
    
    menu_hamburguer();
}

void recompensas()
{
    cout << "Funcao em desenvolvimento";
}


