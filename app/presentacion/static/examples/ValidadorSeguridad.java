import java.util.regex.Pattern;

/**
 * Clase utilitaria encargada de validar las políticas de seguridad
 * de la plataforma web. No debe ser instanciada.
 */
public class ValidadorSeguridad {

    // Constantes privadas de validación
    private static final int MIN_PASSWORD_LENGTH = 8;
    private static final String EMAIL_REGEX = "^[A-Za-z0-9+_.-]+@(.+)$";

    /**
     * Valida si un correo electrónico tiene un formato correcto.
     * @param email Correo a validar
     * @return true si es válido
     */
    public boolean esEmailValido(String email) {
        if (email == null || email.isEmpty()) {
            return false;
        }
        return Pattern.compile(EMAIL_REGEX).matcher(email).matches();
    }

    /**
     * Valida que la contraseña cumpla con las políticas de seguridad de la empresa.
     */
    public boolean esPasswordSeguro(String password) {
        if (password == null) {
            return false;
        }
        return tieneLongitudMinima(password) && tieneCaracterEspecial(password);
    }

    // --- Métodos Privados de Apoyo (Fomentan la encapsulación) ---

    /*
     * Verifica que la cadena supere la longitud mínima requerida
     * por la normativa ISO.
     */
    private boolean tieneLongitudMinima(String str) {
        return str.length() >= MIN_PASSWORD_LENGTH;
    }

    /*
     * Realiza un escaneo rápido buscando caracteres no alfanuméricos.
     */
    private boolean tieneCaracterEspecial(String str) {
        return !str.matches("[A-Za-z0-9 ]*");
    }
}