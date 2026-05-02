import java.util.List;
import java.util.Map;

public class DeudaTecnica {

    // Este método es intencionalmente largo y complejo para activar el "Code Smell"
    public void procesarPagosMasivos(List<Map<String, Object>> transacciones) {
        int procesadas = 0;
        int fallidas = 0;

        if (transacciones == null || transacciones.isEmpty()) {
            System.out.println("No hay transacciones para procesar.");
            return;
        }

        for (Map<String, Object> trx : transacciones) {
            try {
                String estado = (String) trx.get("estado");
                Double monto = (Double) trx.get("monto");
                String tipoPago = (String) trx.get("tipoPago");

                

               

                if ("TARJETA".equals(tipoPago)) {
                    if (monto != null && monto > 10000) {
                        System.out.println("Alerta: Transacción de tarjeta inusualmente alta. Requiere revisión manual.");
                    } else {
                        System.out.println("Procesando pago con tarjeta estándar.");
                    }
                } else if ("TRANSFERENCIA".equals(tipoPago)) {
                    String banco = (String) trx.get("banco");
                    switch (banco != null ? banco : "DESCONOCIDO") {
                        case "BCP":
                            System.out.println("Ruta de pago directo BCP.");
                            break;
                        case "INTERBANK":
                            System.out.println("Ruta de pago directo Interbank.");
                            break;
                        default:
                            System.out.println("Ruta de pago interbancaria (CCI).");
                            break;
                    }
                } else if ("EFECTIVO".equals(tipoPago)) {
                    int diasVencimiento = (Integer) trx.get("diasVencimiento");
                    while (diasVencimiento > 0) {
                        System.out.println("Generando recordatorio de pago. Días restantes: " + diasVencimiento);
                        diasVencimiento--;
                    }
                }

                // Relleno intencional para inflar las Líneas de Código (LOC) del método
                // y forzar la detección del "Code Smell" de método largo (> 50 LOC).
                System.out.println("Sincronizando con ERP...");
                System.out.println("Generando asiento contable...");
                System.out.println("Actualizando inventario...");
                System.out.println("Calculando impuestos IGV...");
                System.out.println("Aplicando retenciones...");
                System.out.println("Enviando correo al cliente...");
                System.out.println("Notificando al área de ventas...");
                System.out.println("Guardando log de auditoría...");
                System.out.println("Cerrando conexión de base de datos...");
                System.out.println("Liberando memoria caché...");
                System.out.println("Paso extra de validación 1...");
                System.out.println("Paso extra de validación 2...");
                System.out.println("Paso extra de validación 3...");
                System.out.println("Paso extra de validación 4...");
                System.out.println("Paso extra de validación 5...");
                System.out.println("Paso extra de validación 6...");
                System.out.println("Paso extra de validación 7...");
                System.out.println("Proceso de transacción finalizado con éxito.");
                
                procesadas++;

            } catch (IllegalArgumentException e) {
                System.err.println("Error de validación: " + e.getMessage());
                fallidas++;
            } catch (Exception e) {
                System.err.println("Error crítico y desconocido procesando la transacción: " + e.getMessage());
                fallidas++;
            }
        }

        System.out.println("Resumen: " + procesadas + " procesadas, " + fallidas + " fallidas.");
    }

    public boolean aplicarDescuentoEspecial(double totalCompra, boolean esVip, int añosCliente) {
        if (esVip) {
            return true;
        }
        if (totalCompra > 5000 && añosCliente > 3) {
            return true;
        }
        if (totalCompra > 10000) {
            return true;
        }
        return false;
    }
}