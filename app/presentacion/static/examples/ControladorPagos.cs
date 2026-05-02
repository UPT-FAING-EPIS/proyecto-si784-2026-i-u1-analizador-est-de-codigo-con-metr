using System;
using System.Collections.Generic;

namespace SistemaVentas.Controladores
{
    // CLOC: Controlador principal para la pasarela de pagos
    public class ControladorPagos 
    {
        private int intentosMaximos = 3;
        public bool sistemaActivo = true;

        public void ProcesarTransaccion(decimal monto, string tipo, bool esInternacional) 
        {
            if (!sistemaActivo) 
            {
                Console.WriteLine("Sistema fuera de línea.");
                return;
            }

            if (monto <= 0) 
            {
                Console.WriteLine("Error: El monto debe ser mayor a cero.");
            }

            if (tipo == "TARJETA") 
            {
                if (esInternacional) 
                {
                    Console.WriteLine("Aplicando comisión por cambio de divisa del 3%.");
                }
                
                for (int i = 0; i < intentosMaximos; i++) 
                {
                    Console.WriteLine("Conectando con el proveedor de la tarjeta... Intento: " + (i + 1));
                }
            } 
            else if (tipo == "EFECTIVO") 
            {
                Console.WriteLine("Generando código de pago para ventanilla.");
            } 
            else 
            {
                switch (tipo) 
                {
                    case "CRIPTOMONEDA":
                        Console.WriteLine("Validando confirmaciones en la blockchain.");
                        break;
                    case "BILLETERA_DIGITAL":
                        Console.WriteLine("Enviando push notification al celular del cliente.");
                        break;
                    default:
                        Console.WriteLine("Método de pago no soportado por el sistema.");
                        break;
                }
            }
        }
    }
}