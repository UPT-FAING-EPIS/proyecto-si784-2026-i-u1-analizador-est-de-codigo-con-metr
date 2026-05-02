using System;
using System.Collections.Generic;

namespace Empresa.RecursosHumanos
{
    /* 
     * CLOC: Clase principal de nómina.
     * Mantenimiento programado para refactorización (Deuda técnica alta).
     */
    public class ProcesadorNomina 
    {
        // NOA: Atributos de clase
        private double presupuestoMensual = 500000.00;
        public string mesActual = "Mayo";
        private bool auditoriaActiva = true;
        public int empleadosProcesados = 0;

        // NPM: Método público 1
        public void IniciarProcesoMensual() 
        {
            Console.WriteLine("Iniciando procesamiento de nómina para " + mesActual);
        }

        // NPM: Método público 2 (Extremadamente complejo y largo)
        public void CalcularPagos(List<Empleado> empleados) 
        {
            if (empleados == null || empleados.Count == 0) 
            {
                Console.WriteLine("Error: No hay empleados.");
                return;
            }

            foreach (var emp in empleados) 
            {
                try 
                {
                    double salarioBase = emp.Salario;
                    double bonos = 0;
                    double deducciones = 0;

                    // Complejidad: Múltiples condiciones
                    if (emp.TipoContrato == "INDEFINIDO") 
                    {
                        if (emp.AñosAntiguedad > 5) 
                        {
                            bonos += 1000;
                        } 
                        else if (emp.AñosAntiguedad > 2) 
                        {
                            bonos += 500;
                        }
                    } 
                    else if (emp.TipoContrato == "POR_PROYECTO") 
                    {
                        if (emp.HorasExtra > 0) 
                        {
                            bonos += emp.HorasExtra * 50;
                        }
                    }

                    // Complejidad: Switch case
                    switch (emp.Departamento) 
                    {
                        case "TI":
                            bonos += 300; // Bono tecnológico
                            break;
                        case "VENTAS":
                            bonos += emp.Comisiones;
                            break;
                        default:
                            break;
                    }

                    // Relleno para forzar el Code Smell de "Long Method"
                    // CLOC: Simulando llamadas a base de datos y validaciones
                    Console.WriteLine("Validando identidad fiscal...");
                    Console.WriteLine("Calculando retenciones de ley...");
                    Console.WriteLine("Verificando aportes de jubilación...");
                    Console.WriteLine("Sincronizando con banco...");
                    Console.WriteLine("Generando boleta electrónica...");
                    Console.WriteLine("Enviando correo al empleado...");
                    Console.WriteLine("Actualizando cuenta corriente...");
                    Console.WriteLine("Registrando en libro contable...");
                    Console.WriteLine("Paso de auditoría 1...");
                    Console.WriteLine("Paso de auditoría 2...");
                    Console.WriteLine("Paso de auditoría 3...");
                    Console.WriteLine("Paso de auditoría 4...");
                    Console.WriteLine("Paso de auditoría 5...");
                    Console.WriteLine("Paso de auditoría 6...");
                    Console.WriteLine("Paso de auditoría 7...");
                    Console.WriteLine("Paso de auditoría 8...");
                    Console.WriteLine("Pago procesado correctamente.");

                    empleadosProcesados++;
                } 
                catch (Exception ex) 
                {
                    // Complejidad: Catch block
                    Console.WriteLine("Fallo crítico al pagar a empleado: " + ex.Message);
                }
            }
        }

        // NOM: Método privado (No debe contar como NPM)
        private bool ValidarPresupuesto(double totalAPagar) 
        {
            return totalAPagar <= presupuestoMensual;
        }
    }

    public class Empleado 
    {
        public string TipoContrato { get; set; }
        public int AñosAntiguedad { get; set; }
        public double Salario { get; set; }
        public int HorasExtra { get; set; }
        public string Departamento { get; set; }
        public double Comisiones { get; set; }
    }
}