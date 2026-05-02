using System;

namespace SistemaVentas.Modelos
{
    public class ClienteDTO 
    {
        public int Id { get; set; }
        public string Nombres { get; set; }
        public string Apellidos { get; set; }
        public string CorreoElectronico { get; set; }
        public DateTime FechaRegistro { get; set; }
        public bool EsClienteFrecuente { get; set; }

        public string ObtenerNombreCompleto() 
        {
            return Nombres + " " + Apellidos;
        }
    }
}