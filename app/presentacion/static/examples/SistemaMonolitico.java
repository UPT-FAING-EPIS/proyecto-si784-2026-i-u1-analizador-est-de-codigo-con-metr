import java.util.*;

// CLOC: Clase principal del sistema heredado
public class SistemaMonolitico {
    
    public String nombreSistema;
    public int version;
    public boolean activo;
    public List<String> usuariosConectados;
    public Map<String, Double> transacciones;

    // CLOC: Inicializa el sistema completo
    public SistemaMonolitico() {
        this.nombreSistema = "Legacy V1";
        this.version = 1;
        this.activo = true;
        this.usuariosConectados = new ArrayList<>();
        this.transacciones = new HashMap<>();
    }

    // Code Smell intencional: Long Parameter List
    public void registrarUsuarioYTransaccion(String nombre, String email, int edad, String dni, String direccion, double monto, String tipoPago) {
        if (activo) {
            usuariosConectados.add(nombre);
            if (monto > 0) {
                transacciones.put(dni, monto);
            }
        }
    }

    // Complejidad altísima intencional
    public void procesarCierreDiario() {
        double total = 0;
        for (Map.Entry<String, Double> entry : transacciones.entrySet()) {
            if (entry.getValue() > 1000) {
                if (entry.getKey().startsWith("A")) {
                    total += entry.getValue() * 0.9;
                } else if (entry.getKey().startsWith("B")) {
                    total += entry.getValue() * 0.8;
                } else {
                    total += entry.getValue();
                }
            } else {
                switch (version) {
                    case 1:
                        total += 10;
                        break;
                    case 2:
                        total += 20;
                        break;
                    default:
                        total += 5;
                }
            }
        }
        System.out.println("Total procesado: " + total);
    }
}