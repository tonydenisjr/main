using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Runtime.Serialization;
using System.Text;
using System.Threading.Tasks;

namespace ex1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int bacon = 0;
            int estado = 1;
            int opcao_estado1 = 0;
            int opcao_estado2 = 0;


            if (estado == 1)
            {
                Console.WriteLine("##############################################################");
                Console.WriteLine("################## Escolha a opção ###########################");
                Console.WriteLine("                   1 - Novo Pedido");
                Console.WriteLine("                   2 - Cupons de desconto");
                Console.WriteLine("                   3 - Reconpensas");


                opcao_estado1 = int.Parse(Console.ReadLine());

                if (opcao_estado1 == 1)
                {
                    Console.WriteLine("Funcao em desenvolvimento");
                    //Função hamburgueres
                    estado = 2;
                }
                else if (opcao_estado1 == 2)
                {
                    Console.WriteLine("Funcao em desenvolvimento");
                    //Funcao cupom
                }
                else if (opcao_estado1 == 3)
                {
                    Console.WriteLine("Funcao em desenvolvimento");
                    //Funcao recompensa
                }
                else
                {
                    Console.WriteLine("Opcao invalida");
                }
            }
            if (estado == 2)
            {
                Console.WriteLine("##############################################################");
                Console.WriteLine("################## Escolha a opção ###########################");
                Console.WriteLine("                   1 - Hamburgueres de carne");
                Console.WriteLine("                   2 - Hamburgueres de frango");



                if (opcao_estado2 == 1)
                {
                    Console.WriteLine("Funcao em desenvolvimento");
                    //hamburguer de carne
                }
                else if (opcao_estado2 == 2)
                {
                    Console.WriteLine("Funcao em desenvolvimento");
                    //hamburguer de frango
                }
                else
                {
                    Console.WriteLine("Opcao invalida");
                }
            }
            if (estado == 3)
            {
                Console.WriteLine("Cumpons de desconto");
            }
            if (estado == 4)
            {
                Console.WriteLine("Recompensas");
            }


            Console.ReadLine();
        }        
       

    }
}
