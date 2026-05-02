public class Prueba {
	public static void main(String[] args) {
		int suma = 0;

		for (int i = 1; i <= 5; i++) {
			if (i % 2 == 0) {
				System.out.println(i + " es par");
			} else {
				System.out.println(i + " es impar");
			}
			suma += i;
		}

		if (suma > 10) {
			System.out.println("La suma es mayor que 10: " + suma);
		} else {
			System.out.println("La suma es 10 o menor: " + suma);
		}
	}
}
